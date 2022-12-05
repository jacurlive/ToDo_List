from django.urls import path

from task.views import tasks, del_tasks, update_task

urlpatterns = [
    path('', tasks, name='tasks_view'),
    path('delete/<str:pk>/', del_tasks, name='delete'),
    path('update/<str:pk>/', update_task, name='update')
]
