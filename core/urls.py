from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', include('listing.urls')),
    path('login/', LoginView.as_view(
        template_name='listing/login.html',
        redirect_authenticated_user=True
    ), name="login"),
    path('logout/', LogoutView.as_view(template_name='listing/logout.html'), name="logout"),
    path('admin/', admin.site.urls, name="admin"),
]
