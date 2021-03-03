from django.shortcuts import render

def index(request):
    return render(request, 'appexpensas/index.html')



def add_expensa(request):
    return render(request, 'appexpensas/add_expensa.html')