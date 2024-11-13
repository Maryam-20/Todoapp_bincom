from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from todoproject.taskapp.models import Task_table


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text="Optional")
    last_name = forms.CharField(max_length=30, required=False, help_text="optional")
    email = forms.EmailField(max_length=254, help_text= "Enter a valid email address ")
    
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2"
        ]

class Task_form(forms.ModelForm):
    task_name = forms.CharField( required=True)
    task_description = forms.CharField(required= True)
    due_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"type": "datetime"}), help_text="Enter the date and time in this format: YYYY-MM-DDTHH:MM")
    
    class Meta:
        model =  Task_table
        fields = [
            "task_name",
            "task_description",
            "due_date",
        ]
        
class edit_task_form(forms.ModelForm):
    task_name = forms.CharField( required=True)
    task_description = forms.CharField(required= True)
    due_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"type": "datetime"}), help_text="Enter the date and time in this format: YYYY-MM-DDTHH:MM")
    
    class Meta:
        model = Task_table
        fields = [
            "task_name",
            "task_description",
            "due_date",
        ]