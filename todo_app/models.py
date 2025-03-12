from django.db import models

# Create your models here.

class TodoListModel(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    status = models.BooleanField(default=False)
