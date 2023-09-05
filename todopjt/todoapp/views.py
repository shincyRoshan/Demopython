from django.shortcuts import render
from .models import Tasks
# Create your views here.
def home(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        priorites = request.POST.get('priority')
        todo = Tasks(name=name, priorites=priorites)
        todo.save()
    return render(request,'home.html')