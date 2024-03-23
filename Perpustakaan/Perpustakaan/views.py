from django.shortcuts import render

def index(request):
    context = {
        'title':'Home',
        'content':'ini adalah home',
    }
    return render(request,'index.html',context)