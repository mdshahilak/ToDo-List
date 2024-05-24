from django.shortcuts import render,redirect,get_object_or_404
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
        if not task:
            return redirect('home')
        Todo = Task.objects.create(task=task)
        Todo.save()
        return redirect('home')
def mark_as_done(request,pk):
    task  = Task.objects.get(id = pk)
    task.is_completed=True
    task.save()
    return redirect('home')
def mark_as_undone(request, pk):
    task  = Task.objects.get(id = pk)
    task.is_completed=False
    task.save()
    return redirect('home')
def update_task(request,update_id):
    get_task=get_object_or_404(Task,id=update_id)
    if request.method=='POST':
        new_task=request.POST.get('new_task')
        get_task.task=new_task
        get_task.save()
        return redirect('home')
    else:
        context={
            'get_task':get_task,
        }
        return render(request,'update.html',context)
