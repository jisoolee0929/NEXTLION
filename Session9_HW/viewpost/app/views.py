from importlib.resources import contents
from turtle import title
from xml.etree.ElementTree import Comment
from django.shortcuts import render, redirect
from .models import Post, Comment

# Create your views here.

def getList(request):
    all_posts = Post.objects.all()
    return render(request,'list.html',{'posts':all_posts})

def createPost(request):
    if request.method == 'POST':
        newpost = Post.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            viewnum = 0  
        )
        return redirect('detail',newpost.pk)
    return render(request,'createpost.html')

def detailPost(request, post_pk):
    detailpost = Post.objects.get(pk = post_pk)
    detailpost.viewnum +=1
    detailpost.save()
    if request.method == 'POST':
        newcomment = Comment.objects.create(
            post = detailpost,
            content= request.POST['content']
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