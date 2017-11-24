from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def mylogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/login/')
    else:
        return render(request, 'superbuy/login.html')


def mylogout(request):
    logout(request)
    return render(request, 'superbuy/login.html')


def homepage(request):
    return render(request, 'superbuy/base.html', locals())


def qt_coupon(request):
    return
