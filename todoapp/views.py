from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoItem
from datetime import datetime

@login_required
def todo_list(request):
    tasks = TodoItem.objects.filter(user=request.user)
    return render(request, 'todoapp/todo_list.html', {'tasks': tasks})

def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        deadline_str = request.POST.get('deadline')
        deadline = None
        if title:
            TodoItem.objects.create(user=request.user,title=title)
        if deadline_str:
            deadline = datetime.fromisoformat(deadline_str)  # convert string to datetime
        TodoItem.objects.create(user=request.user, title=title, deadline=deadline)
    return redirect('todo_list')

def toggle_complete(request, item_id):
    item = get_object_or_404(TodoItem, id=item_id, user=request.user)
    item.completed = not item.completed
    item.save()
    return redirect('todo_list')

def delete_todo(request, item_id):
    item = get_object_or_404(TodoItem, id=item_id, user=request.user)
    item.delete()
    return redirect('todo_list')