from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, admin
from django.contrib.auth.forms import UserCreationForm


def index(request):
    return render(request, 'listing/layout.html')


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("/admin")

        messages.warning(request, "Unsuccessful registration. Invalid information.")

    form = UserCreationForm(request.POST)
    return render(request, 'listing/register.html', context={"register_form": form})
