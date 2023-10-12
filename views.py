

from django.shortcuts import render

def task_view(request):
    data = {
        'task_name': 'Complete Django Assignment',
        'task_description': 'Create a Django project with dynamic data.',
    }
    return render(request, 'myapp/task.html', data)
