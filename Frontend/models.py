from django.db import models

# Create your models here.
class Quiz(models.Model):
    QuestionId=models.IntegerField(default=0,primary_key=True)
    Question = models.CharField(max_length=500)
    Option1 = models.TextField(max_length=500)
    Option2 = models.TextField(max_length=50)
    Option3 = models.TextField(max_length=500)
    Option4 = models.TextField(max_length=500,default=None)
    Answered = models.BooleanField(default=False)
    CorrectAnswer = models.TextField(max_length=500,default="None")
    createdAt=models.DateTimeField(auto_now=True)
    updatedAt=models.DateTimeField(auto_now_add=False,auto_now=True)

    def __str__(self):
        return self.Question
class QuestionsAnswers(models.Model):
    userrname = models.CharField(max_length=50)
    rightQuestions = models.IntegerField(default=0)
    wrongQuestions = models.IntegerField(default=0)
    totalQuestions = models.IntegerField(default=0)
    createdAt=models.DateTimeField(auto_now_add=True)
    updatedAt=models.DateTimeField(auto_now_add=False,auto_now=True)

    def __str__(self):
        return self.userrname