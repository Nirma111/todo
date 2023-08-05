from django.shortcuts import render,redirect
from .models import task
from .forms import TodoForm
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.

class Tasklist(ListView):
    model=task
    template_name='home.html'
    context_object_name = 'task2'
class TaskDetail(DetailView):
    model = task
    template_name = 'detail.html'
    context_object_name = 't'
class TaskUpdate(UpdateView):
    model=task
    template_name = 'edit.html'
    context_object_name = 'Task'
    fields = ('name','priority','date')
def get_success_url(self):
    return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})
class TaskDelete(DeleteView):
    model = task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvlist')

def home(request):
    task2 = task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date = request.POST.get('date', '')
        task1=task(name=name,priority=priority,date=date)
        task1.save()

    return render (request,'home.html',{'Task':task2})
def delete(request,taskid):
    Task=task.objects.get(id=taskid)
    if request.method=="POST":
        Task.delete()
        return redirect ('/')
    return render(request,'delete.html')

def update(request,taskid):
    Task=task.objects.get(id=taskid)
    f=TodoForm(request.POST or None,instance=Task)
    if f.is_valid ():
        f.save()
        return redirect('/')
    return render(request,'update.html',{'f':f,'Task':Task})
