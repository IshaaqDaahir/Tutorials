from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_page(request, *args, **kwargs):
    return render(request, 'home.html', {})

def contact_page(request):
    return render(request, 'contact.html', {})

def about_page(request):
    my_context = {
        'my_text': 'this is about us',
        "my_html": '<h1>This is my html</h1>',
        'my_number': 677243789,
        'my_list': [563, 6732, 'mangoe', 'Apple', 643, 5378]
    }
    return render(request, 'about.html', my_context)