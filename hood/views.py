from django.shortcuts import render, redirect
from .forms import *


# Create your views here.
def index(request):
    title = "Neighbourhood"
    context = {
        "title": title,
    }
    return render(request, 'index.html', context)


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'register/signUp.html', {"form": form})
