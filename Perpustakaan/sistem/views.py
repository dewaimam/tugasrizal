from django.shortcuts import render

def index(request):
    context = {
        'heading':'sistem',
        'content':'konten',
    }

    return render(request, 'index.html', context),