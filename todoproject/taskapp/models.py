from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task_table(models.Model):
    task_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="task", default=1)
    task_name = models.CharField(unique=False, max_length=25, null=True)
    task_description = models.CharField(unique=False, max_length=200, null= True)
    date_created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank = True)
    completed_task = models.BooleanField(default=False)
    
    