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
    success_url = reverse_lazy('show_tasks')


class TodoListView(ListView):
    model = TodoListModel
    template_name = 'show_tasks.html'
    context_object_name = 'data'

class DeleteTodoListView(DeleteView):
    model = TodoListModel
    template_name = 'delete_confirmation.html'
    success_url = reverse_lazy('show_tasks')

class TaskUpdateView(UpdateView):
    model = TodoListModel
    template_name = 'add_todo.html'
    form_class = TodoListForm
    success_url = reverse_lazy('show_tasks')

class MarkTaskCompleteView(UpdateView):
    model = TodoListModel
    
    def get(self, request, *args, **kwargs):
        task = self.get_object()
        task.status = True
        task.save()
        return redirect("completed_tasks")

class CompletedTasksView(ListView):
    model = TodoListModel
    template_name = 'completed_tasks.html'
    context_object_name = 'data'
    
    def get_queryset(self):
        return TodoListModel.objects.filter(status=True)
    