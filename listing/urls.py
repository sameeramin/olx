from django.urls import path

from listing.views import index, register, log_in, log_out

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('login/', log_in, name='log_in'),
    path('logout/', log_out, name='log_out'),
]
