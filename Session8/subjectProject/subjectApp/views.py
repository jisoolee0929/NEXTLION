from re import template
from sre_constants import SUCCESS
from django.shortcuts import render, redirect
from .models import  Major, Subject
from django.views.generic import CreateView, UpdateView
from .forms import MajorModelForm, SubjectModelForm
from django.urls import reverse_lazy

# Create your views here.

class AddMajorView(CreateView):
    model = Major
    form_class = MajorModelForm
    template_name = 'addMajor.html'
    success_url = reverse_lazy('home')

class AddSubjectView(CreateView):
    model = Subject
    form_class = SubjectModelForm
    template_name = 'addSubject.html'
    success_url = reverse_lazy('home')

class EditSubjectView(UpdateView):
    model = Subject
    form_class = SubjectModelForm
    template_name = 'editSubject.html'
    success_url = reverse_lazy('home')


def delete(request,pk):
    del_subject = Subject.objects.get(pk = pk)
    del_subject.delete()
    return redirect('home')

def home(request):
    majors = Major.objects.all()
    subjects = Subject.objects.all()
    return render(request,'home.html',{'majors':majors,'subjects':subjects})

def major(request,major_name):
    subjects = Subject.objects.all()
    each_major = Major.objects.get(name=major_name)
    each_subject = subjects.filter(major = each_major)
    return render(request,'major.html',{'subjects': each_subject,'name':major_name})



