from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.

# Choose difficulty
DIFF_CHOICES = (
    ('easy', 'easy'),
    ('medium', 'medium'),
    ('hard', 'hard'),
)


class Quiz(models.Model):
    """
    Description: Table used to store Quizes
    """

    name = models.CharField(max_length=120)
    topic = models.CharField(max_length=120)
    number_of_questions = models.IntegerField()
    number_of_images = models.IntegerField()
    time = models.IntegerField(help_text="duration of the quiz in minutes")
    required_score_to_pass = models.IntegerField(help_text="required score in %")
    difficulty = models.CharField(max_length=6, choices=DIFF_CHOICES)

    def __str__(self):
        """
        Description: Shows what will be output in the admin page
        """
        return f"{self.name}-{self.topic}"

    def get_questions(self):
        """
        Description: Get every question from a quiz
        """
        return self.question_set.all()

    class Meta:

        # Change quiz name in admin page
        verbose_name_plural = 'Quizes'


class Question(models.Model):
    """
    Description: Table used to store Questions
    """
    text = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    points = models.IntegerField(null=True)

    def __str__(self):
        """
        Description: Shows what will be output in the admin page
        """
        return str(self.text)

    def get_answers(self):
        """
        Description: Get all answers from a question
        """
        return self.answer_set.all()

    def get_images(self):
        """
        Description: Get all images from a question
        """
        return self.images_set.all()


class Images(models.Model):
    """
    Description: Table used to store images
    """
    image = models.ImageField(upload_to="images/", null=False, blank=False, default=None)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    microscopy = models.CharField(max_length=100, null=True, blank=True)
    cell_type = models.CharField(max_length=100, null=True, blank=True)
    component = models.CharField(max_length=100, null=True, blank=True)
    doi = models.CharField(max_length=100, null=True, blank=True)
    organism = models.CharField(max_length=100, null=True, blank=True)

    # Resized image for quiz question
    processed_image = ImageSpecField(source='image',
                                     processors=[ResizeToFill(400, 400)],
                                     format='JPEG',
                                     options={'quality': 100})

    # Resized image for about and main web page
    processed_image_main = ImageSpecField(source='image',
                                          processors=[ResizeToFill(500, 400)],
                                          format='JPEG',
                                          options={'quality': 100})

    def __str__(self):
        """
        Description: Shows what will be output in the admin page
        """

        return str(self.image)

    class Meta:

        # Change name in the admin page
        verbose_name_plural = 'Images'


class Answer(models.Model):
    """
    Description: Table to store answers
    """
    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False, blank=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        """
        Description: Shows what will be output in the admin page
        """
        return f"question: {self.question.text}, answer: {self.text}, correct: {self.correct}"


class Score(models.Model):
    """
    Description: Table to store scores of users depending on quiz
    """
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        """
        Description: Shows what will be output in the admin page
        """
        return f"score: {self.score}, user: {self.user}, quiz: {self.quiz}"
