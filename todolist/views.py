from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from .models import Task


def index(request):
    task = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('.')
    context = {
        'task': task,
        'form': form
    }
    return render(request, 'todolist/index.html', context)


def update(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'task': task,
        'form': form
    }
    return render(request, 'todolist/update.html', context)


def delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    context = {
        'task': task
    }
    if request.method == 'POST':
        task.delete()
        return redirect('index')
    return render(request, 'todolist/delete.html', context)
