from importlib.resources import contents
from turtle import title
from urllib import request
from xml.etree.ElementTree import Comment
from django.shortcuts import render, redirect
from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request,"home.html")



def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        found_name = User.objects.filter(username= username)
        if len(found_name):
            error = "이미 아이디가 존재합니다"
            return render(request,"signup.html",{"error":error})
        new_user = User.objects.create_user(username= username, password= password)
        auth.login(request, new_user, backend='django.contrib.auth.backends.ModelBackend') 
        return redirect("list")
    return render (request,"signup.html")

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request,username= username, password = password)
        if user is not None:
            auth.login(request, user, backend="django.contrib.auth.backends.ModelBackend")
            return redirect(request.GET.get("next","/"))
        error = "잘못된 아이디 또는 비밀번호를 입력했습니다"
        return render(request,"login.html",{"error":error})
    return render (request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect("home")


def getList(request):
    all_posts = Post.objects.all()
    return render(request,'list.html',{'posts':all_posts})


@login_required(login_url="login")
def createPost(request):
    if request.method == 'POST':
        newpost = Post.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            viewnum = 0,
            author = request.user
        )
        return redirect('detail',newpost.pk)
    return render(request,'createpost.html')

@login_required(login_url="login")
def detailPost(request, post_pk):
    detailpost = Post.objects.get(pk = post_pk)
    detailpost.viewnum +=1
    detailpost.save()
    if request.method == 'POST':
        newcomment = Comment.objects.create(
            post = detailpost,
            content= request.POST['content'],
            author = request.user
        )
    return render(request,'detail.html',{'post':detailpost})


def editPost(request,post_pk):
    post = Post.objects.filter(pk = post_pk)
    if request.method == 'POST':
        post.update(
            title = request.POST['title'],
            content = request.POST['content']
        )
        return redirect('detail',post_pk)
    return render(request,'editpost.html',{'post':post[0]})


def deletePost(request, post_pk):
    post = Post.objects.filter(pk = post_pk)
    post.delete()
    return redirect('list')


def deleteComment(request,post_pk,comment_pk):
    comment = Comment.objects.get(pk = comment_pk)
    comment.delete()
    return redirect('detail',post_pk)