from django.shortcuts import render,redirect
from django.http import response
from .models import (Quiz,QuestionsAnswers)
import string,random
import json
def generate_random(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))
def Reset(request):
    del request.session['username']
    username = generate_random(10)
    request.session['username'] = username
    questions = Quiz.objects.all()
    for question in questions:
        question.Answered = False
        question.save()
    return redirect('start')
def Start(request):
    if 'message' in request.session:
        del request.session['message']
    if 'username' in request.session:
        pass
    else:
        username = generate_random(10)
        request.session['username'] = username
    #check if the user has answered all questions
    if QuestionsAnswers.objects.filter(userrname=request.session['username']).exists():
        questions = Quiz.objects.all().count()
        answeredQuestions = QuestionsAnswers.objects.filter(userrname=request.session['username']).first()
        if questions==answeredQuestions.totalQuestions:
            #get all the totals 
            passedQuestions = answeredQuestions.rightQuestions
            failedQuestions = answeredQuestions.wrongQuestions
            percentPass = int(round((passedQuestions / answeredQuestions.totalQuestions) * 100,0))
            data={
                'passedQuestions': passedQuestions,
                'failedQuestions': failedQuestions,
                'passRate': percentPass
            }
            print(data)
            return render(request,"Frontend/Questions.html",{'question':[],'data':data})
        else:
            question = Quiz.objects.filter(Answered=False).first()
            return render(request,"Frontend/Questions.html",{'question':question})
    else:
        question = Quiz.objects.filter(Answered=False).first()
        return render(request,"Frontend/Questions.html",{'question':question})
def AddQuiz(request):
    context={}
    return render(request, 'Frontend/AddQuiz.html',context)
def Submit_Answer(request):
    if request.method == 'POST':
        question = request.POST['QuestionTitle']
        current_user = request.session['username']
        SelectionChoice = request.POST['SelectionChoice']
        #get the question 
        q = Quiz.objects.filter(Question=question).first()
        if q:
            if QuestionsAnswers.objects.filter(userrname=current_user).count() > 0:
                #records exists, so update
                attemptedQuestions = QuestionsAnswers.objects.filter(userrname=current_user).first()
                tq = attemptedQuestions.totalQuestions
                tq= tq+1
                attemptedQuestions.totalQuestions = tq
                print(f"The answer is {q.CorrectAnswer==SelectionChoice}")
                if q.CorrectAnswer==SelectionChoice:
                    #the answer is correct 
                    att = (attemptedQuestions.rightQuestions)+1
                    attemptedQuestions.rightQuestions = att
                else:
                    wq = (attemptedQuestions.wrongQuestions)+1
                    attemptedQuestions.wrongQuestions = wq
                attemptedQuestions.save()
                q.Answered=True
                q.save()
                return redirect("start")
            else:
                att=0
                wq =0
                if q.CorrectAnswer==SelectionChoice:
                    #the answer is correct 
                    att = 1
                    print("attempted treu b")
                else:
                    wq=1
                    print("wrong answer")
            QuestionsAnswers.objects.create(
                userrname = request.session['username'],
                rightQuestions = att,
                wrongQuestions=wq,
                totalQuestions=1
            )
            q.Answered=True
            q.save()
    return redirect("start")
def GetQuestion(request):
    if request.method == 'POST':
        question = request.POST['Question']
        Option1 = request.POST['Option1']
        Option2 = request.POST['Option2']
        Option3 = request.POST['Option3']
        Option4 = request.POST['Option4']
        CorrectAnswer = request.POST['CorrectAnswer']
        questions = Quiz.objects.all().count()
        quiz = Quiz.objects.create(
            QuestionId = int(questions)+1,
            Question=question,
            Option1=Option1,
            Option2=Option2,
            Option3=Option3,
            Option4=Option4,
            CorrectAnswer=CorrectAnswer
        )
        message = ''
        if quiz:
            message = "Question Successfully Created"
        else:
            message = "Error Adding Question"
        request.session['message'] = message
        return redirect("add_quiz")
def AllQuestions(request):
    if 'message' in request.session:
        del request.session['message']
    questions = Quiz.objects.all()
    return render(request, 'Frontend/AllQuestions.html',{'questions':questions})