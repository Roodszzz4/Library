from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .forms import TaskForm
from .models import Task


def index(request):
    user_tasks = []
    if request.user.is_authenticated:
        user_tasks = Task.objects.filter(user=request.user)

    context = {
        'user_tasks': user_tasks,
        'form': TaskForm,
    }
    if request.method == 'POST':
        Task.objects.create(
            user=request.user,
            title=request.POST.get('title')
        )

    return render(request, 'index.html', context=context)


def set_task_as_completed(request, id):
    task = get_object_or_404(Task, id=id)
    task.is_completed = True
    task.save()
    return redirect(reverse_lazy("index"))


def set_task_as_no_completed(request, id):
    task = get_object_or_404(Task, id=id)
    task.is_completed = False
    task.save()
    return redirect(reverse_lazy("index"))


def del_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect(reverse_lazy("index"))

@login_required
def set_all_completed(request):
    tasks = Task.objects.filter(user=request.user)
    tasks.update(is_completed=True)
    return redirect(reverse_lazy("index"))