from django.urls import path

from listing.views import index, RegisterUserView, CreateAdView, UpdateAdView, DeleteAdView

urlpatterns = [
    path('', index, name='index'),
    path('register/', RegisterUserView.as_view(), name="register"),
    path('ads/create', CreateAdView.as_view(), name='create-ad'),
    path('ads/update/<int:pk>/', UpdateAdView.as_view(), name="update-ad"),
    path('ads/delete/<int:pk>', DeleteAdView.as_view(), name="delete-ad"),
]
