from django.shortcuts import render,redirect
from .models import Task
# Create your views here.
def home(request):
    task=Task.objects.filter(is_completed=False)
    completed = Task.objects.filter(is_completed=True)
    context = {
        'task':task,
        'complete':completed,
    }
    return render(request,'index.html',context)
def add_task(request):
    if request.method=='POST':
        task = request.POST.get('task')
        Todo = Task.objects.create(task=task)
        Todo.save()
        return redirect('home')