from django.shortcuts import render

# Create your views here.

def about(request):
    d = {'name':'vineeth'}

    return render(request,'about.html',context=d)