from django import forms
from listing.models import Listing


class ListingForm(forms.ModelForm):
    image = forms.ImageField(
        label='Image',
        widget=forms.ClearableFileInput(attrs={'multiple': True}),
    )

    class Meta:
        model = Listing
        fields = ('title', 'short_description', 'description', 'price', 'category', 'address', 'city', 'image')
