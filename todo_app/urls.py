from django.urls import path
from . import views

urlpatterns = [
    path('', views.MyHomeView.as_view(), name="homepage")
]
