from django.contrib import admin
from listing.models import Ad, Category, City, Image

# Registering models
admin.site.register(Ad)
admin.site.register(Category)
admin.site.register(City)
admin.site.register(Image)
