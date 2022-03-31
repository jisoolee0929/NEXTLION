from django.shortcuts import render

# Create your views here.

def count(request):
    return render(request,'count.html')

def result(request):
    text = request.POST['text']
    no_blank_len = 0
    word_count = 0
    line1 = text.split('\n')
    for i in line1:
        word = i.replace('\n','').split(' ')
        for j in word:
            if j !='' and j != ' ':
                word_count += 1
                no_blank_len += len(j.replace(' ','').strip(' '))


    total_len = len(text.replace('\n',''))
    return render(request, 'result.html',{'text':text,'total_len':total_len, 'no_blank_len':no_blank_len,'word_count':word_count})