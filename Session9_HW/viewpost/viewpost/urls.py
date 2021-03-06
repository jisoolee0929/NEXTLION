"""viewpost URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home,name="home"),
    path('list', views.getList, name='list'),
    path('detail/<int:post_pk>,', views.detailPost, name='detail' ),
    path('createpost',views.createPost, name = 'createpost'),
    path('editpost<int:post_pk>',views.editPost,name = 'editpost'),
    path('deletepost<int:post_pk>', views.deletePost,name = 'deletepost'),
    path('deletecomment<int:post_pk><int:comment_pk>',views.deleteComment,name='deletecomment'),
    path('signup',views.signup,name="signup"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('accounts/', include('allauth.urls')),

]
