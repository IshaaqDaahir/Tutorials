from django.shortcuts import render

def home(request):
    return render(request, 'profiles/home.html', {})

def about(request):
    return render(request, 'profiles/about.html', {})
