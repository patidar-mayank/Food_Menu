from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.
#---this is one way to render template
# def index(request):
#     item_list=Item.objects.all()
#     template=loader.get_template('food\index.html')
#     context={

#     }
#     return HttpResponse(template.render(context,request))

#another view ,view is python function

# second way to render template

def index(request):
    item_list=Item.objects.all()
    template=loader.get_template('food\index.html')
    context={
        'item_list':item_list,

   }
    return render(request,'food\index.html',context)
# class based views

class IndexClassView(ListView):
    model = Item; 
    template_name='food/index.html'
    context_object_name='item_list'


def item(request):
    return HttpResponse('<h1>this is second view</h1>')

def detail(request,item_id):
    item=Item.objects.get(pk=item_id)
    context={
        'item':item,
    }
    return render(request,'food\detail.html',context)

class foodDetail(DetailView):
    model=Item
    template_name='food/detail.html'

def create_item(request):
    form=ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request,'food/item-form.html',{'form':form})


def update_item(request,item_id):
    item=Item.objects.get(id=item_id)
    form=ItemForm(request.POST or None,instance=item)
    
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request,'food/item-form.html',{'form':form,'item':item})


def delete_item(request,item_id):
    item=Item.objects.get(id=item_id)
    if request.method=='POST':
        item.delete()
        return redirect('food:index')
    return render(request,'food/item-delete.html',{'item':item})