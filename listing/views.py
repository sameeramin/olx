from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def index(request):
    return render(request, 'listing/layout.html')


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("/")

        messages.warning(request, "Unsuccessful registration. Invalid information.")

    if request.POST:
        form = UserCreationForm(request.POST)
    else:
        form = UserCreationForm()
    return render(request, 'listing/register.html', context={"register_form": form})


def log_in(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.info(request, f"You're logged in as {username}.")
                return redirect("/")
            else:
                messages.warning(request, "Invalid username or password.")
        else:
            messages.warning(request, "Invalid username or password.")

    form = AuthenticationForm()
    return render(request, 'listing/login.html', context={"login_form": form})


def log_out(request):
    pass
