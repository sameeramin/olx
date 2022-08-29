from django.urls import path

from listing.views import index, RegisterUserView

urlpatterns = [
    path('', index, name='index'),
    path('register/', RegisterUserView.as_view(), name="register"),
]
