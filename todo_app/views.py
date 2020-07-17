from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .forms import CreateNewList
from django.urls import reverse
from .models import ToDoList, Item
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist


@login_required(login_url='/login/')
def todo_create(request):
    if request.method == 'POST':
        form = CreateNewList(request.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            request.user.todolist.add(t)

            return HttpResponseRedirect(reverse('todo_app:todo_list', args=(t.id,)))
    else:
        form = CreateNewList()

    return render(request, 'todo_app/todo_create.html', {'form': form})


@login_required(login_url='/login/')
def todo_list(request, id):
    # ls = get_object_or_404(ToDoList, id=id)
    try:
        ls = ToDoList.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('todo_app:view'))

    if ls in request.user.todolist.all():
        if request.method == "POST":
            if request.POST.get("save"):
                for item in ls.item_set.all():
                    p = request.POST

                    if "clicked" == p.get("c" + str(item.id)):
                        item.complete = True
                    else:
                        item.complete = False
                    if "text" + str(item.id) in p:
                        item.text = p.get("text" + str(item.id))

                    item.save()
            elif request.POST.get("add"):
                new_item = request.POST.get("new")
                if new_item != "":
                    ls.item_set.create(text=new_item, complete=False)
                else:
                    print("invalid")

            for item in ls.item_set.all():
                if request.POST.get(f'd{item.id}'):
                    p = request.POST

                    if "Delete" == p.get("d" + str(item.id)):
                        item.delete()

        return render(request, 'todo_app/todolist.html', {'ls': ls})
    else:
        return HttpResponseRedirect(reverse('todo_app:view'))


@login_required(login_url='/login/')
def view(request):
    return render(request, 'todo_app/view.html', {})
