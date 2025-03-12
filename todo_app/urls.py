from django.urls import path
from . import views

urlpatterns = [
    path('', views.MyHomeView.as_view(), name="homepage"),
    path('add_new_task/', views.TodoFormView.as_view(), name="add_task"),
    path('show_tasks/', views.TodoListView.as_view(), name="show_tasks"),
    path('delete_task/<int:pk>/', views.DeleteTodoListView.as_view(), name="delete_task"),
    path('update_task/<int:pk>/', views.TaskUpdateView.as_view(), name="update_task"),
]
