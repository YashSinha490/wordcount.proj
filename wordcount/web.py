from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request,'home.html')

def count(request):
    textbox=request.GET['textbox']
    words=textbox.split()
    countword=len(words)
    dic={}
    for i in words:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    lis=dic.items()
    sorteddic=sorted(lis,key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{'textbox':textbox,'countword':countword,'sorteddic':sorteddic})

def about(request):
    return render(request,'about.html')
