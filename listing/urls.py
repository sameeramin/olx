from django.urls import path

from listing.views import index, register

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register')
]
