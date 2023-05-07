from django.shortcuts import render, redirect

from apps.users.models import UserRole

# Create your views here.

def home(request):
    return render(request,"home.html")

def user_view(request):
    if request.user.role == UserRole.MEMBER:
        return render(request, 'user_view.html')
    return redirect('/admin')