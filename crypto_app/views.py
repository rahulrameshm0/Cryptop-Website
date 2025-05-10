from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about_layout.html')

def how(request):
    return render(request, 'how_layout.html')
    