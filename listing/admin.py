from django.contrib import admin
from listing.models import Listing, Category, City, Image

# Registering models
admin.site.register(Listing)
admin.site.register(Category)
admin.site.register(City)
admin.site.register(Image)
