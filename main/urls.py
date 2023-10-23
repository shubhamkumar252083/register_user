
from django.contrib import admin
from django.urls import path
from user.views import UserRegistration, UserLogin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', UserRegistration.as_view(), name='user-registration'),
    path('login', UserLogin.as_view(), name='user-login'),
]
