from django.shortcuts import render,redirect
from .models import person
import datetime 

# Create your views here.

    
def list2(request):
    ser = person.objects.all()
    if request.method=="POST":
        id = request.POST.get('id')
        task = request.POST.get("task")
        # date = request.POST.get("date")
        task_type = request.POST.get("type")
        todo=person(task = task, date= datetime.datetime.now() , task_type=task_type,sr_no=id)
        todo.save()
    return render(request,'list2.html',{"service":ser})

def delete(request,id):
    dele = person.objects.get(id=id)
    dele.delete()
    return redirect('/list2')

def update(request,id):
    todo = person.objects.get(id = id)
    print(todo)
    if request.method =='POST':
        todo.id = request.POST.get('id')
        todo.task = request.POST.get('task')
    
        todo.task_type=request.POST.get('task_type')
        todo.save()
        return redirect('/list2')

    context = {'todo':todo }
    
    return render(request,'update.html',context)

