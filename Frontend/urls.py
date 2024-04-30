from django.urls import path 
from . import views

urlpatterns=[
    path('',views.Start,name='index'),
    path('Start/',views.Start,name='start'),
    path('Add_Questions/',views.AddQuiz,name='add_quiz'),
    path("Get-Question/",views.GetQuestion,name='get_question'),
    path("All/",views.AllQuestions,name='all_questions'),
    path("Reset-progress/",views.Reset,name='reset_progress'),
    path("Submit-Answer/",views.Submit_Answer,name='submit_answer'),
]