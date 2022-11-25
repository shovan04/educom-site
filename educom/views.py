from django.http import HttpResponse
from django.shortcuts import redirect, render
from datetime import datetime as date
from notice.models import *
from user.models import Student
from .password import *


def home(request):
    request.session['date'] = date.today().strftime("%A")
    try:
        if (request.session['log_st'] != ''):
            return redirect('log_home')
    except:
        return render(request, 'index.html')


def notic(request):
    notic_ = Notic.objects.all()
    try:
        if request.session['log_st'] != "":
            return render(request, 'loged/notice.html', {'notic': notic_})
    except:
        return render(request, 'notic.html', {'notic': notic_})


def signup(request):
    try:
        if (request.session['log_st'] != ''):
            return redirect('log_home')
    except:
        return render(request, 'signup.html')


def login(request):
    try:
        if (request.session['log_st'] != ''):
            return redirect('log_home')
    except:
        return render(request, 'login.html')


def login_sub(request):
    if request.method == "POST":
        uname = request.POST['uname']
        pasw = request.POST['pass']
        if uname != "" and pasw != "":
            user = Student.objects.filter(username=uname)
            if user.count() > 0:
                pasw = secPass(pasw)
                for i in user:
                    if (i.pasw == pasw):
                        request.session['log_st'] = i.username
                        return HttpResponse(1)
                    elif (i.pasw != pasw):
                        return HttpResponse('<div class="alert alert-danger" role="alert">Password not Match.</div>')
            else:
                return HttpResponse('<div class="alert alert-danger" role="alert">No Record Found</div>')
        elif uname == "" and pasw == "":
            return HttpResponse('<div class="alert alert-danger" role="alert">Please Fill all the Fileds.</div>')
    else:
        return redirect('home')


def signup_sub(request):
    if request.method == "POST":
        name = request.POST['name']
        uname = request.POST['uname']
        email = request.POST['email']
        phone = request.POST['phone']
        pasw = request.POST['pass']
        cpasw = request.POST['cpass']

        if name != "" and uname != "" and email != "" and phone != "" and pasw != "" and cpasw != "":
            msg_suc = ''
            msg_phone = ''
            msg_uname = ''
            msg_email = ''
            msg = ''
            if pasw == cpasw:
                if Student.objects.filter(email=email).count() > 0:
                    msg_email = '<div class="alert alert-danger" role="alert">Email alrady exits.</div>'
                    return HttpResponse(msg_email)
                if Student.objects.filter(username=uname).count() > 0:
                    msg_uname = '<div class="alert alert-danger" role="alert">UserName alrady taken.</div>'
                    return HttpResponse(msg_uname)
                if Student.objects.filter(phone=phone).count() > 0:
                    msg_phone = '<div class="alert alert-danger" role="alert">Phone no alrady exits.</div>'
                    return HttpResponse(msg_phone)
                else:
                    secpasw = secPass(pasw)
                    user = Student(name=name, email=email,
                                   username=uname, pasw=secpasw, phone=phone)
                    user.save()
                    msg_suc = '<div class="alert alert-success" role="alert">Successfully Created. Redirect to login page in 5 second.</div>'
                    return HttpResponse(msg_suc)

            if pasw != cpasw:
                msg = '<div class="alert alert-danger" role="alert">Password & Confirm Password didn\'t match</div>'
                return HttpResponse(msg)

        else:
            msg = '<div class="alert alert-danger" role="alert">Please Fill all the Fields.</div>'
            return HttpResponse(msg)
    else:
        return redirect('home')


def test(request):
    data = Student.objects.filter(username='shovan04').count() == 1
    return render(request, 'test.html', {'data': data})


def log_home(request):
    try:
        if request.session['log_st'] != "":
            if Student.objects.filter(username=request.session['log_st']).count() > 0:
                data = Student.objects.filter(
                    username=request.session['log_st'])
                request.session['date'] = date.today().strftime("%A")
                return render(request, 'loged/home.html', {'data': data})
            else:
                del request.session['log_st']
                return redirect('home')
    except:
        return redirect('home')


def lgout(request):
    try:
        if request.session['log_st'] != "":
            if Student.objects.filter(username=request.session['log_st']).count() > 0:
                del request.session['log_st']
                return redirect('home')
    except:
        return redirect('home')


def user(request):
    data = Student.objects.all()
    try:
        if (request.session['log_st'] != ''):
            return render(request, 'loged/user.html', {'data': data})
    except:
        return redirect('home')


def report(request, uname=""):
    try:
        if (request.session['log_st'] != ''):
            if Student.objects.filter(username=uname).count() == 1:
                return render(request, 'loged/report.html', {'status': True, 'uname': uname})
            else:
                return render(request, 'loged/report.html')
    except:
        return redirect('home')


def atdanc(request):
    try:
        if (request.session['log_st'] != ''):
            if date.today().strftime("%A") == 'Sunday':
                return HttpResponse('Hi')
            else:
                return redirect('log_home')
    except:
        return redirect('home')
