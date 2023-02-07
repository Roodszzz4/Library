from django.shortcuts import render

from todo.models import Task


def index(request):
    user_tasks = []
    if request.user.is_authenticated:
        user_tasks = Task.objects.filter(user=request.user)
        context = {
            'user_tasks': user_tasks
        }
    return render(request, 'index.html', context=context)
