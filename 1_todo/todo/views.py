from django.shortcuts import render
from django.http import HttpResponse
from .models import items

from django.template import loader

from django.http import HttpResponseRedirect
from .forms import todoForm, change

def index(request):
    todo_list = items.objects.order_by('-complete')
    template = loader.get_template('todo/todo.html')
    context = {
        'todo_list' : todo_list, 
        'form' : todoForm,
        'change' : change
    }
#     output = '<pre>status      task</pre>'
#     output += ' '.join(['<pre>%s   %s</pre>'%(q.is_complete(), q.item) for q in todo_list])
    return HttpResponse(template.render(context, request))

def todo_item(request, itemId):
    return HttpResponse("item %s"%itemId)

def add_item(request):
    if request.method == 'POST':
        f = todoForm(request.POST)
        if f.is_valid():
            item = f.cleaned_data['item']
            new_item = items(item=item, complete='todo')
            new_item.save()
        
            return HttpResponseRedirect('/todo/')
    else:
        form.todoForm()

    return render(request, 'todo.html', {'forms': forms})
        
def complete(request, listId):
    item = items.objects.get(pk=listId)
    item.complete = 'completed'
    item.save()
    return HttpResponseRedirect('/todo/')

def delete(request, listId):
    item = items.objects.get(pk=listId)
    item.delete()
    return HttpResponseRedirect('/todo/')

    
# Create your views here.
