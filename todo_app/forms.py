from django import forms
from todo_app.models import TodoListModel

class TodoListForm(forms.ModelForm):
    class Meta:
        model = TodoListModel
        # fields = '__all__'
        fields = ['title', 'description']
        widgets = {
            'description': forms.Textarea()
        }