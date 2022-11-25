from django.contrib import admin
from django.urls import path

from educom import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('notic/',views.notic,name='notic'),
    path('signup/',views.signup,name='signup'),
    path('signup_sub/',views.signup_sub,name='signup_sub'),
    path('login/',views.login,name='login'),
    path('login_sub/',views.login_sub,name='login_sub'),
    path('test/',views.test,name='test'),
    path('home/',views.log_home,name='log_home'),
    path('lgout/',views.lgout,name='lgout'),
    path('user/',views.user,name='user'),
    path('report/',views.report,name='report'),
    path('report/<uname>',views.report,name='report'),
    path('atdanc/',views.atdanc,name='atdanc'),
    path('forgot-pass/',views.forgotpass,name='forgot-pass'),
    path('forgot-pass/<uname>/',views.forgotpass,name='forgot-pass'),
    path('forgot-pass/<uname>/<key>',views.forgotpass,name='forgot-pass'),
    path('cng_pass',views.cng_pass,name='cng_pass'),
    path('send-mail/<uname>/<key>/',views.send_mail,name='send-mail'),
]
