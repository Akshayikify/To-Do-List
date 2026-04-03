from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Todo
from django.contrib.auth import authenticate,login,logout
def signup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        print(username,email,password)
        new_user=User.objects.create_user(username,email,password)
        new_user.save()
        return redirect('/login')
    return render(request,'signup.html')
def login_user(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/dashboard')
        else:
            return redirect('/login')
    return render(request,'login.html')
def dashboard(request):
    if request.method=='POST':
        title=request.POST.get('title')
        print(title)
        obj=Todo(title=title,user=request.user)
        obj.save()
        res=Todo.objects.filter(user=request.user).order_by('-date')
        return redirect('/dashboard',{'res':res})
    res=Todo.objects.filter(user=request.user).order_by('-date')
    return render(request,'dashboard.html',{'res':res})
def edit_todo(request,task_id):
    if request.method=='POST':
        title=request.POST.get('title')
        print(title)
        obj=Todo.objects.get(task_id=task_id)
        obj.title=title
        obj.save()
        return redirect('/dashboard',{'obj':obj})
    obj=Todo.objects.get(task_id=task_id)
    res=Todo.objects.filter(user=request.user).order_by('-date')
    return render(request,'dashboard.html',{'res':res})