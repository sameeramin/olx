from django.urls import path

from listing.views import (
    ListListingView,
    RegisterUserView,
    CreateAdView,
    UpdateAdView,
    DeleteAdView,
    ListMyListingsView,
    DetailListingView
)

urlpatterns = [
    path('', ListListingView.as_view(), name='index'),
    path('register/', RegisterUserView.as_view(), name="register"),
    path('ads/<int:pk>/', DetailListingView.as_view(), name="ad-details"),
    path('ads/create', CreateAdView.as_view(), name='create-ad'),
    path('ads/update/<int:pk>/', UpdateAdView.as_view(), name="update-ad"),
    path('ads/delete/<int:pk>', DeleteAdView.as_view(), name="delete-ad"),
    path('ads/my-ads/', ListMyListingsView.as_view(), name="my-ads"),
]
