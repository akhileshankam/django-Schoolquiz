

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render,HttpResponse
from django.contrib import messages, auth
from .models import quiz1, score1,quiz2,score2
import time

def home(request):
    return render(request,'home.html')
def signupform(request):
    return render(request,'signupform.html')
def register(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if cpassword==password:
            if username and password:
                x=User.objects.create_user(username=username,password=password)
                x.save()
                return render(request,'confirmation.html')
            else:
                return HttpResponse("enter all fields")
        else:
            return HttpResponse("passwords didnt match")
def loginform(request):
    return render(request,'loginform.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'welcome.html')
z=[0]
def quiz0(request):
    m= time.perf_counter()
    z[0]=m
    return render(request,'quiz1.html')

c=[0]
def quiz12(request):
    if request.method=="POST":
        ans1=request.POST['1ans']
        answer = ans1
        username=request.user.username
        x=quiz1(answer=answer,username=username)
        x.save()
        if ans1=="panaji":
            c[0]=c[0]+1
            messages.success(request,"correct answer")
            return render(request,'quiz12.html')
        else:
            messages.success(request," wrong answer ,answer is panaji")
            return render(request, 'quiz12.html')

def quiz13(request):
    if request.method=="POST":
        ans1=request.POST['1ans']
        answer = ans1
        username = request.user.username
        x = quiz1(answer=answer, username=username)
        x.save()
        if ans1=="bhopal":
            c[0] = c[0] + 1
            messages.success(request,"correct answer")
            return render(request,'quiz13.html')
        else:
            messages.success(request," wrong answer ,answer is bhopal")
            return render(request, 'quiz13.html')
def quiz14(request):
    if request.method=="POST":
        ans1=request.POST['1ans']
        answer = ans1
        username = request.user.username
        x = quiz1(answer=answer, username=username)
        x.save()
        if ans1=="dispur":
            c[0] = c[0] + 1
            messages.success(request,"correct answer")
            return render(request,'quiz14.html')
        else:
            messages.success(request," wrong answer ,answer is dispur")
            return render(request, 'quiz14.html')
def quiz15(request):
    if request.method=="POST":
        ans1=request.POST['1ans']
        answer = ans1
        username = request.user.username
        x = quiz1(answer=answer, username=username)
        x.save()
        if ans1=="itanagar":
            c[0] = c[0] + 1
            messages.success(request,"correct answer")
            return render(request,'quiz15.html')
        else:
            messages.success(request," wrong answer ,answer is itanagar")
            return render(request, 'quiz15.html')
def quiz16(request):
    if request.method=="POST":
        ans1=request.POST['1ans']
        answer = ans1
        username = request.user.username
        x = quiz1(answer=answer, username=username)
        x.save()
        if ans1=="gangtok":
            c[0] = c[0] + 1
            messages.success(request,"correct answer")
            return render(request,'quiz16.html')
        else:
            messages.success(request," wrong answer ,answer is gangtok")
            return render(request, 'quiz16.html')
def quiz17(request):
    if request.method=="POST":
        ans1=request.POST['1ans']
        answer = ans1
        username = request.user.username
        x = quiz1(answer=answer, username=username)
        x.save()
        if ans1=="jaipur":
            c[0] = c[0] + 1
            messages.success(request,"correct answer")
            return render(request,'quiz17.html')
        else:
            messages.success(request," wrong answer ,answer is jaipur")
            return render(request, 'quiz17.html')
def quiz18(request):
    if request.method=="POST":
        ans1=request.POST['1ans']
        answer = ans1
        username = request.user.username
        x = quiz1(answer=answer, username=username)
        x.save()
        if ans1=="chandigarh":
            c[0] = c[0] + 1
            messages.success(request,"correct answer")
            return render(request,'quiz18.html')
        else:
            messages.success(request," wrong answer ,answer is chandigarh")
            return render(request, 'quiz18.html')
def quiz19(request):
    if request.method=="POST":
        ans1=request.POST['1ans']
        answer = ans1
        username = request.user.username
        x = quiz1(answer=answer, username=username)
        x.save()
        if ans1=="calcutta":
            c[0] = c[0] + 1
            messages.success(request,"correct answer")
            return render(request,'quiz19.html')
        else:
            messages.success(request," wrong answer ,answer is calcutta")
            return render(request, 'quiz19.html')
def quiz20(request):
    if request.method=="POST":
        ans1=request.POST['1ans']
        answer=ans1
        username = request.user.username
        x = quiz1(answer=answer, username=username)
        x.save()
        if ans1=="mumbai":
            c[0] = c[0] + 1
            messages.success(request,"correct answer")
            return render(request,'quiz20.html')
        else:
            messages.success(request," wrong answer ,answer is mumbai")
            return render(request, 'quiz20.html')
def quiz21(request):
    if request.method=="POST":
        ans1=request.POST['1ans']
        answer = ans1
        username = request.user.username
        x = quiz1(answer=answer, username=username)
        x.save()
        if ans1=="kohima":
            y= time.perf_counter()
            c[0] = c[0] + 1
            st="your score is {}/10 ".format(c[0])
            b=y-z[0]
            st1 = "Total time taken {} seconds".format(b)
            if (c[0] < 5):
                st2 = " , you FAILED"
            else:
                st2 = ", you PASSED"
            q=st+st1+st2
            j=score1(username=request.user.username,score1=c[0])
            j.save()

            return HttpResponse(q)
        else:

                y = time.perf_counter()
                st = "your score is {}/10".format(c[0])
                b = y - z[0]
                st1 = "Total time taken {} seconds".format(b)
                if (c[0] < 5):
                    st2 = ", you FAILED"
                else:
                    st2 = ", you PASSED"
                q = st + st1 + st2
                j = score1(username=request.user.username, score1=c[0])
                j.save()
                return HttpResponse(q)


z2=[0]
def quiz02(request):
    m= time.perf_counter()
    z2[0]=m
    return render(request,'quiz21.html')

c2=[0]
def quiz22(request):
    if request.method=="POST":
        ans1=request.POST['1ans']
        answer = ans1
        username=request.user.username
        x=quiz2(answer=answer,username=username)
        x.save()
        if ans1=="shimla":
            c2[0]=c2[0]+1
            messages.success(request,"correct answer")
            return render(request,'quiz22.html')
        else:
            messages.success(request," wrong answer ,answer is shimla")
            return render(request, 'quiz22.html')

def quiz23(request):
    if request.method=="POST":
        ans1=request.POST['1ans']
        answer = ans1
        username = request.user.username
        x = quiz2(answer=answer, username=username)
        x.save()
        if ans1=="patna":
            c2[0] = c2[0] + 1
            messages.success(request,"correct answer")
            return render(request,'quiz23.html')
        else:
            messages.success(request," wrong answer ,answer is patna")
            return render(request, 'quiz23.html')

def quiz24(request):
    if request.method == "POST":
        ans1 = request.POST['1ans']
        answer = ans1
        username = request.user.username
        x = quiz2(answer=answer, username=username)
        x.save()
        if ans1 == "gandhinagar":
            c2[0] = c2[0] + 1
            messages.success(request, "correct answer")
            return render(request, 'quiz24.html')
        else:
            messages.success(request, " wrong answer ,answer is gandhinagar")
            return render(request, 'quiz24.html')
def quiz25(request):
    if request.method=="POST":
        ans1=request.POST['1ans']
        answer = ans1
        username = request.user.username
        x = quiz2(answer=answer, username=username)
        x.save()
        if ans1=="ranchi":
            c2[0] = c2[0] + 1
            messages.success(request,"correct answer")
            return render(request,'quiz25.html')
        else:
            messages.success(request," wrong answer ,answer is ranchi")
            return render(request, 'quiz25.html')
def quiz26(request):
    if request.method=="POST":
        ans1=request.POST['1ans']
        answer = ans1
        username = request.user.username
        x = quiz2(answer=answer, username=username)
        x.save()
        if ans1=="bangalore":
            c2[0] = c2[0] + 1
            messages.success(request,"correct answer")
            return render(request,'quiz26.html')
        else:
            messages.success(request," wrong answer ,answer is bangalore")
            return render(request, 'quiz26.html')
def quiz27(request):
    if request.method=="POST":
        ans1=request.POST['1ans']
        answer = ans1
        username = request.user.username
        x = quiz2(answer=answer, username=username)
        x.save()
        if ans1=="imphal":
            c2[0] = c2[0] + 1
            messages.success(request,"correct answer")
            return render(request,'quiz27.html')
        else:
            messages.success(request," wrong answer ,answer is imphal")
            return render(request, 'quiz27.html')
def quiz28(request):
    if request.method=="POST":
        ans1=request.POST['1ans']
        answer = ans1
        username = request.user.username
        x = quiz2(answer=answer, username=username)
        x.save()
        if ans1=="shillong":
            c2[0] = c2[0] + 1
            messages.success(request,"correct answer")
            return render(request,'quiz28.html')
        else:
            messages.success(request," wrong answer ,answer is shillong")
            return render(request, 'quiz28.html')
def quiz29(request):
    if request.method=="POST":
        ans1=request.POST['1ans']
        answer = ans1
        username = request.user.username
        x = quiz2(answer=answer, username=username)
        x.save()
        if ans1=="aizwal":
            c2[0] = c2[0] + 1
            messages.success(request,"correct answer")
            return render(request,'quiz29.html')
        else:
            messages.success(request," wrong answer ,answer is aizwal")
            return render(request, 'quiz29.html')
def quiz30(request):
    if request.method=="POST":
        ans1=request.POST['1ans']
        answer = ans1
        username = request.user.username
        x = quiz2(answer=answer, username=username)
        x.save()
        if ans1=="bhubaneshwar":
            c2[0] = c2[0] + 1
            messages.success(request,"correct answer")
            return render(request,'quiz30.html')
        else:
            messages.success(request," wrong answer ,answer is bhubaneshwar")
            return render(request, 'quiz30.html')

def quiz31(request):
    if request.method=="POST":
        ans1=request.POST['1ans']
        answer = ans1
        username = request.user.username
        x = quiz2(answer=answer, username=username)
        x.save()
        if ans1=="chennai":
            y= time.perf_counter()
            c2[0] = c2[0] + 1
            st="your score is {}/10 ".format(c2[0])
            b=y-z2[0]
            st1 = "Total time taken {} seconds".format(b)
            if (c2[0] < 5):
                st2 = " ,you FAILED"
            else:
                st2 = " ,you PASSED"
            q=st+st1+st2
            j=score2(username=request.user.username,score2=c2[0])
            j.save()
            return HttpResponse(q)
        else:

                y = time.perf_counter()
                st = "your score is {}/10".format(c2[0])
                b = y - z2[0]
                st1 = "Total time taken {} seconds".format(b)
                if (c2[0] < 5):
                    st2 = " ,you FAILED"
                else:
                    st2 = " ,you PASSED"
                q = st + st1 + st2
                j = score2(username=request.user.username, score2=c2[0])
                j.save()
                return HttpResponse(q)

