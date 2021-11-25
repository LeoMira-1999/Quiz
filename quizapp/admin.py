from django.contrib import admin
from django.contrib import admin
from .models import Question, Answer, Quiz, Images, Score


class AnswerInline(admin.TabularInline):
    model = Answer


class ImagesInline(admin.TabularInline):
    model = Images


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ImagesInline, AnswerInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Images)
admin.site.register(Quiz)
admin.site.register(Score)


