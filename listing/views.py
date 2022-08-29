from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import UserCreationForm


@login_required
def index(request):
    return render(request, 'listing/layout.html')


class RegisterUserView(SuccessMessageMixin, CreateView):
    """ Creates a new user account """
    template_name = 'listing/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    success_message = "User account for %(username)s has been created successfully"
