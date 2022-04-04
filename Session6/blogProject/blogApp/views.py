from contextlib import redirect_stderr
from django.shortcuts import render, redirect
from .models import Article
from datetime import datetime


# Create your views here.
def new(request):

    if request.method == 'POST':
        category = request.POST['category']
        if category == "hobby":
            category_id = 1
        elif category == "food":
            category_id = 2
        elif category == "programming":
            category_id = 3
        else:
            category_id = 4

        now = datetime.now()
        newarticle = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            category_id = category_id,
            date = now
        )
        return redirect('list')
    return render(request, 'new.html')


def list(request):
    articles = Article.objects.all()
    count1 = 0
    count2 = 0
    count3 = 0
    for article in articles:
        if article.category_id ==1:
            count1 += 1
        elif article.category_id ==2:
            count2 += 1
        elif article.category_id ==3:
            count3 += 1
        

    return render(request, 'list.html', {'articles': articles, 'count1':count1,'count2':count2,'count3':count3})

def detail(request, article_id):
    articles = Article.objects.get(pk = article_id)
    return render(request,'detail.html',{'articles': articles})

def category(request, category_id):
    articles = Article.objects.filter(category_id = category_id)
    return render(request,'category.html',{'articles': articles})
