from django.shortcuts import render, redirect

from task.forms import TasksForm
from task.models import Task


def tasks(request):
    task_model = Task.objects.all()

    form = TasksForm()

    if request.method == 'POST':
        form = TasksForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('tasks_view')

    context = {
        'tasks': task_model,
        'form': form
    }
    return render(request, 'task/list.html', context)


def del_tasks(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('tasks_view')

    context = {
        'task': task
    }

    return render(request, 'task/delete.html', context)


def update_task(request, pk):
    task = Task.objects.get(id=pk)

    forms = TasksForm(instance=task)

    if request.method == 'POST':
        form = TasksForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks_view')

    context = {
        'form': forms
    }

    return render(request, 'task/update.html', context)
