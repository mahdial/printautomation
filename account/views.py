from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import HttpResponse, redirect, render
from account.models import ProfileDetail
from django.core.files.storage import FileSystemStorage


def signup(request):
    pass
    # if request.method == 'POST':
    #     if User.objects.filter(email=request.POST.get('email')).exists():
    #         return render(request, 'account/account.html', {'err': 'قبلا با این آدرس ایمیل ثبت نام انجام شده است'})
    #     if User.objects.filter(username=request.POST.get('username')).exists():
    #         return render(request, 'account/account.html', {'err': 'نام کاربری تکراری است'})
    #     if request.POST.get('pass1') == request.POST.get('pass2'):
    #         user = User.objects.create_user(request.POST.get(
    #             'username'), request.POST.get('email'), request.POST.get('pass1'))
    #         user.first_name = request.POST.get('name')
    #         user.last_name = request.POST.get('lname')
    #         user.save()
    #         login(request, user)

    #         if request.FILES['img[]']:
    #             myfile = request.FILES['img[]']
    #             fs = FileSystemStorage()
    #             filename = fs.save(myfile.name, myfile)
    #             ProfileDetail.objects.create(img=myfile)

    #         return redirect('dashboard:index')
    #     else:
    #         return render(request, 'account/account.html', {'err': 'رمز عبورها با هم یکسان نیستند'})
    # else:
    #     return render(request, 'account/account.html')


def ulogin(request):
    pass
    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     password = request.POST.get('pass')
    #     user = authenticate(username=username, password=password)
    #     if user:
    #         if user.is_active:
    #             login(request, user)
    #             if 'next' in request.POST:
    #                 return redirect(request.POST.get('next'))
    #             else:
    #                 return redirect('dashboard:index')
    #         else:
    #             return render(request, 'account/login.html', {'err': 'حساب شما غیر فعال شده است . با مدیر سیستم صحبت نمایید'})
    #     else:
    #         return render(request, 'account/login.html', {'err': 'نام کاربری و یا رمز عبور شما اشتباه است'})
    # else:
    #     return render(request, 'account/login.html', {})


def ulogout(request):
    pass
    # logout(request)
    # return redirect(ulogin)
