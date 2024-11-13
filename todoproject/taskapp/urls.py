from django.urls import path
from todoproject.taskapp import views as vw

urlpatterns = [
    path("create_task/<int:userid>/", vw.create_task, name = "create_task"),
    path("all_task/<int:userid>/", vw.viewAll_task, name = "viewAll_task"),
    path("edit_task/<int:userid>/<int:taskId>/", vw.edit_task, name = "edit_task"),
    path("task_completed/<int:userid>/<int:taskId>/", vw.mark_as_completed, name = "mark_as_completed" ),
    path("task/<int:userid>/completed/", vw.viewAll_completed_task, name ="all_completed_task"),
    path("task/<int:userid>/<int:taskId>/delete/", vw.delete_task, name= "delete_task")
]
