from django.urls import path
from . import views

urlpatterns = [
    path('', views.convert_to_nepali_date, name='convert_to_nepali_date'),
]
