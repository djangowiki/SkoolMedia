from django.shortcuts import render

def home(request):
    return render(request, 'home/index.html', {})

def about(request):
    return render(request, 'home/about.html', {})
    

def solutions(request):
    return render (request, 'home/solutions.html', {})

def centers (request):
    return render(request, 'home/centers.html', {})

def contact(request):
    return render(request, 'home/contact.html', {})