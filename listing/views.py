from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import UserCreationForm


@login_required
def index(request):
    ads = ["ad"] * 7
    return render(request, 'listing/index.html', context={"ads": ads})


class RegisterUserView(SuccessMessageMixin, CreateView):
    """ Creates a new user account """
    template_name = 'listing/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    success_message = "%(username) account has been created successfully"
