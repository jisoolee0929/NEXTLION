from turtle import left, title
from django.shortcuts import render, redirect
from datetime import datetime
from .models import todoPost

# Create your views here.
def home(request):
    todo_posts = todoPost.objects.all()
    return render(request,'home.html', {'todo_posts': todo_posts })

def new(request):
    if request.method == 'POST':
        now = datetime.now()
        date_obj = datetime.strptime(request.POST['duedate'], '%Y-%m-%d')
        date_diff= date_obj - now
        new_post = todoPost.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            duedate = request.POST['duedate'],
            detail = request.POST['detail'],
            left_day = date_diff.days
        )
        return redirect('detail', new_post.pk)
    return render(request,'new.html')

def detail(request,pk):
    detail_post =todoPost.objects.get(pk = pk)
    return render(request,'detail.html',{'detail_post':detail_post})

def edit(request,pk):
    edit_post = todoPost.objects.get(pk = pk)
    if request.method =='POST':
        todoPost.objects.filter(pk=pk).update(
            title = request.POST['title'],
            content = request.POST['content'],
            duedate = request.POST['duedate'],
            detail = request.POST['detail'],
            left_day = request.POST['left_day']
        )
        return redirect('detail',pk)
    return render(request,'edit.html',{'edit_post':edit_post})

def delete(request,pk):
    del_post = todoPost.objects.get(pk =pk)
    del_post.delete()
    return redirect('home')