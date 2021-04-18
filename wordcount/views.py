from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    worddiction = {}
    textcount = fulltext.split()
    for word in textcount:
        if word in worddiction:
            worddiction[word] += 1
        else:
            worddiction[word] = 1

    sortedwords = sorted(worddiction.items(), key=operator.itemgetter(1), reverse = True)
    return render(request,'count.html',{'fulltext': fulltext,'textcount':len(textcount), 'worddiction': sortedwords})

def about(request):
    return render(request,'about.html')
