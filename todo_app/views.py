from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from todo_app.forms import TodoListForm
from todo_app.models import TodoListModel
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

class MyHomeView(TemplateView):
    template_name = 'home.html'

class TodoFormView(CreateView):
    model = TodoListModel
    template_name = 'add_todo.html'
    form_class = TodoListForm
    success_url = reverse_lazy('homepage')