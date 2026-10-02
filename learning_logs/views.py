from django.shortcuts import render

# Create your views here.
def index(request):
    """Homepage"""
    return render(request, 'learning_logs/index.html')