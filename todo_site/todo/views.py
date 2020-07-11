
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import todoItems


def index(request):
    all_todo_items = todoItems.objects.all()
    return render(request,'todo_index.html',{'all_items':all_todo_items})

def addTodo(request):
    new_item = todoItems(content = request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')

def deleteTodo(request,todo_id):
    item_toDelete = todoItems.objects.get(id = todo_id)
    item_toDelete.delete()
    return HttpResponseRedirect('/todo/')