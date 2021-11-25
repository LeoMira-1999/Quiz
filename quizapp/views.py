from django.shortcuts import render, redirect
from django.contrib import messages
from quizapp.forms import RegisterForm
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from .models import Question, Answer, Quiz, Images, Score
from numpy import random

scoreboard = None


# Create your views here.
# def foo(request,):
#     return render(request, "base.html")
#
# def foo1(request,):
#     return render(request, "template.html", {"name": "leo"})
#
# def foo2(request,):
#     return render(request, "bd.html", {"master": Master.objects.all()})


def register(request):
    """
    Description: Allows a user to register
    """

    if request.method == 'GET':
        form = RegisterForm()
        context = {'form': form}
        return render(request, 'registration/register.html', context)
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():

            # Log user when registration is successful
            new_user = form.save()
            messages.success(request, "Thanks for registering. You are now logged in.")
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect("main-view")
        else:
            print('Form is not valid')
            messages.error(request, 'Error Processing Your Request')
            context = {'form': form}
            return render(request, 'registration/register.html', context)

    return render(request, 'registration/register.html')


def get_score():
    """
    Description: get the score of a user
    Return: dictionary of score
    """
    scores = Score.objects.all()
    scoreboard = {}

    # Fill the scoreboard
    for score in scores:
        if score.user not in scoreboard:
            scoreboard[score.user] = score.score
        else:
            scoreboard[score.user] += score.score

    return scoreboard


def main(request):
    """
    Description: main page function where it will get every quiz and available images for carousel
    """
    quizs = Quiz.objects.all()
    images_all = Images.objects.all()
    images_active = []
    images_inactive = []

    ######### Carousel ############
    selected_image_set = random.choice(images_all, 3, replace=False)
    print(selected_image_set)
    for image in selected_image_set[0:1]:
        images_active.append(image)
    for image in selected_image_set[1:3]:
        images_inactive.append(image)

    ################################

    scoreboard = get_score()

    return render(request, "main.html", {"score": scoreboard, "quizs": quizs, 'images_active': images_active,
                                         'images_inactive': images_inactive})


def quiz_data_view(request, pk):
    """
    Description: Function activate by a JS window redirection which will get the primary key of the given quiz
    """

    quiz = Quiz.objects.get(pk=pk)
    questions = []
    scoreboard = get_score()

    # Get quiz questions
    for question in quiz.get_questions():
        answers = []
        images = []

        # Get images for question
        for image in question.get_images():
            images.append(image.processed_image.url)

        # Get answers for question
        for answer in question.get_answers():
            answers.append(answer.text)

        # Append Images, Question and Answer
        questions.append({str(question): {"images": images, "answers": answers}})

    return render(request, 'quiz.html', {"score": scoreboard, 'obj': questions, "name": quiz.name, "time": quiz.time,
                                         "required_score_to_pass": quiz.required_score_to_pass})


def save_quiz_view(request, pk):
    """
    Description: Function launched by hitting submit in a quiz which will trigger an Ajax response
    """
    if request.is_ajax():
        questions_points = {}
        data = request.POST
        data_ = dict(data.lists())

        # Remove CSRF protection
        data_.pop('csrfmiddlewaretoken')

        # Get data information in dictionary format
        for k in data_.keys():
            print('key: ', k)
            question = Question.objects.get(text=k)
            questions_points[question] = question.points

        user = request.user
        quiz = Quiz.objects.get(pk=pk)
        print(questions_points)
        score = 0
        results = []
        correct_answer = None

        # Cycle in received answers
        for question, score_unique in questions_points.items():
            a_selected = request.POST.get(question.text)

            # If answer is not nothing
            if a_selected != "":

                question_answers = Answer.objects.filter(question=question)

                # for each answer in question
                for answer in question_answers:

                    # if correct answer
                    if a_selected == answer.text:
                        if answer.correct:
                            score += score_unique
                            correct_answer = answer.text

                    # if not correct answer
                    else:
                        if answer.correct:
                            score -= score_unique
                            correct_answer = answer.text

                # append results to results
                results.append({str(question): {'correct_answer': correct_answer, 'answered': a_selected,
                                                'score': score_unique}})
            # if not answered
            else:
                score -= score_unique

                # append results to results
                results.append({str(question): {'not answered': True, 'score': score_unique}})

        # calculate score
        multiplier = 100 / quiz.number_of_questions
        score_ = score
        score = score_ * multiplier

        # add score for user in database
        Score.objects.create(quiz=quiz, user=user, score=score_)

        print(score)
        print(score_)
        print(results)

        # if score is greater that required score to pass
        if score >= quiz.required_score_to_pass:

            # return a Json response with results and True passed
            return JsonResponse({'passed': True, 'score': score_, 'results': results})
        else:

            # return a Json response with results and False passed
            return JsonResponse({'passed': False, 'score': score_, 'results': results})


def show_image_about_quiz(request, ):
    """
    Description: Get images from database for about html page
    """
    images = Images.objects.all()
    scoreboard = get_score()

    return render(request, 'about.html', {'images': images, "score": scoreboard})
