from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def index(request):
    title = "Neighbourhood"
    context = {
        "title": title,
    }
    return render(request, 'index.html', context)


def register(request):
    form = UserCreationForm()
    context = {
        "form": form,
    }
    return render(request, 'register/signUp.html', context)
