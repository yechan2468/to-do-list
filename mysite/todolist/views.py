from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    task_list = Task.objects.order_by('finished', 'due_date', '-priority_level')
    context = {'task_list': task_list}
    return render(request, 'task_list.html', context)


def detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    context = {'task': task}
    return render(request, 'task_detail.html', context)


def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    context = {'form': form}
    return render(request, 'task_form.html', context)


def task_edit(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            question = form.save(commit=False)
            question.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    context = {'form': form}
    return render(request, 'task_form.html', context)


def task_delete(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect('task_list')
