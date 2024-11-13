from django.shortcuts import render, get_object_or_404
from todoproject.taskapp.forms import Task_form
from django.contrib.auth.models import User
from django.views import generic
from django.contrib import messages
from django.http import HttpResponsePermanentRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import SignUpForm, edit_task_form
from todoproject.taskapp.models import Task_table

# Create your views here.
class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

@login_required  
def create_task(request, userid):
    if request.method == "POST":
        task_form = Task_form(request.POST)
        if task_form.is_valid():
            task = task_form.save(commit=False)
            task.user = request.user
            task_form.save()
            
            messages.success(request, ("Task created succesfull"))
            return HttpResponsePermanentRedirect(reverse("home", args=(userid,)))
        else:
            messages.error(request, ("Form not valid"))
            return HttpResponsePermanentRedirect(reverse("create_task", args=(userid,)))
        
    else:
       task_form = Task_form
       return render(request, "taskapp/create_task.html", {"task_form": task_form}) 
   
@login_required
def viewAll_task(request, userid):
    task = Task_table.objects.all().filter(user_id = userid)
    return render(request, "taskapp/viewAll_task.html", {"tasks":task})

def edit_task(request, userid, taskId):
    if request.method == "POST":
        editTask_form = edit_task_form(request.POST)
        if editTask_form.is_valid():
            taskName = editTask_form.cleaned_data["task_name"]
            taskDescription = editTask_form.cleaned_data["task_description"]
            dueDate = editTask_form.cleaned_data["due_date"]
            
            task = Task_table.objects.all().filter(user_id = userid, task_id = taskId).update(
                task_name = taskName,
                task_description = taskDescription,
                due_date = dueDate
            )
            messages.success(request, (f"Task Updated Succesffull"))
            return HttpResponsePermanentRedirect(reverse("home", args=(userid,)))
        else:
            messages.error(request, (f"Form not valid. fill the form correctly"))
            return HttpResponsePermanentRedirect(reverse("edit_task", args=(userid,)))
        
    else:
        editTask_form = edit_task_form()
        return render(request, "taskapp/editform.html", {"edit_form": editTask_form})
    
@login_required
def mark_as_completed(request, userid, taskId):
    task = get_object_or_404(Task_table, task_id = taskId)
    task.completed_task = True
    task.save()
    return HttpResponsePermanentRedirect(reverse("viewAll_task", args=(userid, )))

@login_required
def viewAll_completed_task(request, userid):
    task_completed = Task_table.objects.filter(user_id = userid, completed_task = True)
    return render(request, "taskapp/all_completed_task.html", {"taskCompleted":task_completed})

@login_required
def delete_task(request, userid, taskId):
    Task_table.objects.filter(user_id = userid, task_id = taskId).delete()
    messages.success(request, (f"Task Deleted Successfully"))
    return HttpResponsePermanentRedirect(reverse("viewAll_task", args=(userid,)))
