from . import views
from django.urls import path

urlpatterns = [
    path('register-driver', views.driver_form, name="register_driver"),
]
