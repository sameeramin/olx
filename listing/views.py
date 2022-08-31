from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from listing.models import Image, Listing
from listing.forms import ListingForm


@login_required
def index(request):
    ads = ["ad"] * 7
    return render(request, 'listing/index.html', context={"ads": ads})


class RegisterUserView(SuccessMessageMixin, CreateView):
    """ Creates a new user account """
    template_name = 'listing/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    success_message = "%(username) account has been created successfully."


class CreateAdView(LoginRequiredMixin, CreateView):
    """ Creates a new ad """
    form_class = ListingForm
    template_name = 'listing/create-ad.html'

    def form_valid(self, form):
        """ Saves a listing first, because image needs a listing before it can be saved """
        form.instance.user = self.request.user
        listing = form.save()
        images = self.request.FILES.getlist('image')

        for image in images:
            Image.objects.create(listing=listing, image=image)

        return redirect(reverse_lazy('create-ad'))


class UpdateAdView(LoginRequiredMixin, UpdateView):
    """ Updates an existing ad """
    model = Listing
    form_class = ListingForm
    template_name = 'listing/create-ad.html'
    success_url = reverse_lazy('create-ad')


class DeleteAdView(LoginRequiredMixin, DeleteView):
    """ Deletes an ad """
    model = Listing
    success_url = reverse_lazy('index')

    def get(self, *args, **kwargs):
        """ Overriding default behaviour to skip confirmation """
        return self.post(*args, **kwargs)
