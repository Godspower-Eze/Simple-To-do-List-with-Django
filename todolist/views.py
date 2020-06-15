from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


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
        'form':form
    }
    return render(request, 'todolist/index.html', context)
