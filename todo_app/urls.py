from django.urls import path
from . import views

urlpatterns = [
    path('', views.MyHomeView.as_view(), name="homepage"),
    path('add_new_task/', views.TodoFormView.as_view(), name="add_task"),
]
