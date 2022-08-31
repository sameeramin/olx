from django import forms
from listing.models import Listing, Image
from betterforms.multiform import MultiModelForm


class ListingForm(forms.ModelForm):

    class Meta:
        model = Listing
        fields = ('title', 'short_description', 'description', 'price', 'category', 'address', 'city')


class ImageForm(forms.ModelForm):
    image = forms.ImageField(
        label='Image',
        widget=forms.ClearableFileInput(attrs={'multiple': True})
    )

    class Meta:
        model = Image
        fields = ('image', )


class ListingMultiImageForm(MultiModelForm):
    form_classes = {
        'listing': ListingForm,
        'image': ImageForm,
    }
