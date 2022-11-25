from django.http import HttpResponse
from django.shortcuts import redirect, render
from datetime import datetime as date
from notice.models import *
from user.models import Student
from .password import *
from django.core.mail import *


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

    msg = EmailMultiAlternatives('Test Subject', '<h2>Test message form django<u> mail</u></h2>',
                                 'educom0075@gmail.com', ['shovanm50@gmail.com'],)
    msg.content_subtype = "html"
    msg.send()

    return render(request, 'test.html')


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


def forgotpass(request, uname="", key=""):
    if uname != "":
        if key != "":
            user = Student.objects.filter(username=uname)
            if user.count() > 0:
                for i in user:
                    if i.SecKey == key :
                        return render(request, 'forgotpass.html', {'typ': 'new', 'uname': uname})
                    else:
                        msg_suc = '<div class="alert alert-danger" role="alert">Token Error.</div><br><br><a href="http://127.0.0.1:8000" class="btn btn-outline-primary" >Back to home</a>'
                        return HttpResponse(msg_suc)
                    # print(type(i.SecKey))
            else:
                msg_suc = '<div class="alert alert-danger" role="alert">User not found! .</div><br><br><a href="http://127.0.0.1:8000" class="btn btn-outline-primary" >Back to home</a>'
                return HttpResponse(msg_suc)
        else:
            return render(request, 'forgotpass.html', {'typ': 'old', 'uname': uname})
    else:
        return render(request, 'forgotpass.html')


def cng_pass(request):
    if request.method == "POST":
        uname = request.POST['uname']
        pasw = request.POST['pass']
        cpasw = request.POST['cpass']

        user = Student.objects.get(username=uname)
        if pasw == cpasw:
            user.pasw = secPass(pasw)
            user.SecKey = "1"

            msg = f'''Update!<br><br>
                    Your profile information has been updated. For your records, here is a copy of the information you submitted to us...<br>
                    Name : {user.name}<br>
                    UserName : {user.username}<br>
                    Email Address : {user.email}<br>
                    Mobile No : {user.phone}<br>
                    Password : {pasw}<br><br><br>

                    Thank You,<br>
                    Team EduCom.<br>'''
            mail  =  EmailMultiAlternatives('Account Details',msg,
                                 'educom0075@gmail.com', ['shovanm50@gmail.com',f'{user.email}'],)
            mail.content_subtype = "html"
            mail.send()
            user.save()
            msg_suc = '<div class="alert alert-success" role="alert">Success. Redirect to login page in 5 second.</div>'
            return HttpResponse(msg_suc)
        else:
            msg_suc = '<div class="alert alert-success" role="alert">Password & Confirm Password not match.</div>'
            return HttpResponse(msg_suc)
    else:
        return redirect('forgot-pass')


def send_mail(request,uname,key):
    user = Student.objects.filter(username=uname,SecKey=key)
    if user.count() == 1:
        for self in user:
            msg = f'''<div style="font-family: Helvetica,Arial,sans-serif;min-width:1000px;overflow:auto;line-height:2">
                <div style="margin:50px auto;width:70%;padding:20px 0">
                <div style="border-bottom:1px solid #eee">
                    <a href="" style="font-size:1.4em;color: #00466a;text-decoration:none;font-weight:600">EduCom</a>
                </div>
                <p style="font-size:1.1em">Hi,</p>
                <p><b>{self.name}</b>&nbsp;&nbsp;Your username is</p>
                <h2 style="background: #00466a;margin: 0 auto;width: max-content;padding: 0 10px;color: #fff;border-radius: 4px;">{self.username}</h2><br>
                <h2>Create Password <a href=`http://127.0.0.1:8000/forgot-pass/{uname}/{key}`>click here</a></h2><br>
                <p style="font-size:0.9em;">Regards,<br />EduCom</p>
                <hr style="border:none;border-top:1px solid #eee" />
                <div style="float:right;padding:8px 0;color:#aaa;font-size:0.8em;line-height:1;font-weight:300">
                    <p>EduCom</p>
                    <p>Teacher - Samir Das.</p>
                    <p>Location - Purnanagar</p>
                </div>
                </div>
            </div>'''
        mail = EmailMultiAlternatives(
                'Account Confirmation', msg, 'educom0075@gmail.com', [f'{self.email}'],)

            
        mail.content_subtype = "html"
        mail.send()

        return HttpResponse('<h2>Success</h2><br><br><a href="http://127.0.0.1:8000/admin/user/student/">Back</a>')
    else :
        return HttpResponse('<h2>Fail</h2><br><br><a href="http://127.0.0.1:8000/admin/user/student/">Back</a>')