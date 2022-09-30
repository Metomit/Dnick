from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth import logout as django_logout

# Create your views here.
def login_req(request):
    if not request.user.is_authenticated:
        return render(request,'login.html')
    else:
        return redirect('/select_course')

def actual_login(request):
    if not request.user.is_authenticated:
        if request.POST["username"]=="admin" and request.POST["password"]=="admin":
            user = authenticate(request, username='admin', password='admin')
            login(request, user)
            return render(request,'select.html')
        else:
            return render(request,'noexist.html')
    else:
        return render(request,'select.html')

def logout(request):
    django_logout(request)
    return render(request,'logout.html')

def video(request):
    if not request.user.is_authenticated:
        return render(request,'login.html')
    else:
        return render(request,'video.html')

def stream(request):
    if not request.user.is_authenticated:
        return render(request,'login.html')
    else:
        return render(request,'stream.html')

def about(request):
    if not request.user.is_authenticated:
        return render(request,'login.html')
    else:
        return render(request,'about.html')

def books(request):
    if not request.user.is_authenticated:
        return render(request,'login.html')
    else:
        return render(request,'books.html')