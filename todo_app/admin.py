from django.contrib import admin
from todo_app.models import TodoListModel
# Register your models here.

class TodoListModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'status')

admin.site.register(TodoListModel, TodoListModelAdmin)