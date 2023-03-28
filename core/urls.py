from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from chat.views import index


urlpatterns = [
    path('', index),
    path('accounts/login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
]
