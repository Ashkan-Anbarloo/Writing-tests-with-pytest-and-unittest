from django.shortcuts import render , redirect
from django.http import HttpResponse
from lists.models import Item , List
from lists.forms import ItemForm
from lists.models import Item , List
from django.core.exceptions import ValidationError
from lists.forms import ItemForm, EMPTY_ITEM_ERROR
# Create your views here.

# home_page = None
def home_page(request):
    return render(request, 'home.html' , {'form':ItemForm()})
    # return render(request, 'home.html')


def view_list(request , list_id):
    our_list = List.objects.get(id=list_id)
    form = ItemForm()
    if request.method == "POST":
        form = ItemForm(data=request.POST)
        if form.is_valid():
            Item.objects.create(text=request.POST['text'] , list=our_list)
            return redirect(our_list)
    return render(request , 'list.html' , {'list':our_list , 'form':form})

def new_list(request):
    form = ItemForm(data=request.POST)
    if form.is_valid():
        nulist = List.objects.create()
        Item.objects.create(text=request.POST['text'] , list=nulist)
        return redirect(nulist) #f'/lists/{nulist.id}/'
    else:
        return render(request , 'home.html' , {'form':form})
    

def add_item(request , list_id):
    our_list = List.objects.get(id=list_id)
    Item.objects.create(text = request.POST['text'] , list=our_list)
    return redirect(f"/lists/{our_list.id}/")