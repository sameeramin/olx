from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from listing.models import Image, Listing
from listing.forms import ListingForm


class ListListingView(ListView):
    """ Lists all the ads """
    paginate_by = 6
    model = Listing
    template_name = 'listing/index.html'


class ListMyListingsView(LoginRequiredMixin, ListView):
    """ Lists all the ads created by a user """
    model = Listing
    template_name = 'listing/my-ads.html'

    def get_queryset(self):
        return Listing.objects.filter(user=self.request.user)


class DetailListingView(DetailView):
    """ Show the detailed view of an ad """
    model = Listing
    template_name = 'listing/ad-details.html'


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
    template_name = 'listing/update-ad.html'

    def form_valid(self, form):
        """ Updates a listing images by deleting previous images """
        listing = form.save()
        Image.objects.filter(listing=listing).delete()
        images = self.request.FILES.getlist('image')

        for image in images:
            Image.objects.create(listing=listing, image=image)

            return redirect(reverse_lazy('my-ads'))


class DeleteAdView(LoginRequiredMixin, DeleteView):
    """ Deletes an ad """
    model = Listing
    success_url = reverse_lazy('my-ads')

    def get(self, *args, **kwargs):
        """ Overriding default behaviour to skip confirmation """
        return self.post(*args, **kwargs)
