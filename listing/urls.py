from django.urls import path

from listing.views import index

urlpatterns = [
    path('', index, name='index'),
]
