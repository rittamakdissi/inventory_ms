from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from . models import Product,Order
from . forms import ProductForm,OrderForm
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

@login_required(login_url='login')
def index(request):
   if request.method=="POST":
     addorder=OrderForm(request.POST)
     if addorder.is_valid():
       instance=addorder.save(commit=False)
       instance.staff=request.user 
       instance.save()
       orderd=addorder.cleaned_data.get('product')
       messages.success(request,f'you have ordered {orderd}')
       return redirect('dashboard-index')
   else:
      addorder=OrderForm(request.POST)
  
   context={
    'orders':Order.objects.all(),
    'addorder':addorder,
    'products':Product.objects.all(),
   }
   return render(request,'index.html',context)



@login_required(login_url='login')
def staff(request):
   workers=User.objects.all()
   workers_count=workers.count()
  
   context={
     
    'workers':workers,
    'workers_count':workers_count
  
   }

   return render(request,'staff.html',context)


def staff_detail(request,pk):
   context={
     
    'workers':User.objects.get(id=pk),
  
   }

   return render(request,'staff_detail.html',context)




@login_required(login_url='login')
def product(request):
   if request.method=="POST":
     addproduct=ProductForm(request.POST)
     if addproduct.is_valid():
       addproduct.save()
       product_name=addproduct.cleaned_data.get('name')
       messages.success(request,f'{product_name} has been added')
       return redirect('dashboard-product')
        
   else:
     addproduct=ProductForm()

   context={
     #'items':Product.objects.all();
      'items':Product.objects.raw('SELECT * FROM dashboard_product'),
       'addproduct':addproduct
   }
   return render(request,'product.html',context)



def delete (request,pk):
  deleteproduct=Product.objects.get(id=pk)
  if request.method=="POST":
    deleteproduct.delete()
    return redirect('dashboard-product')
  
  return render(request,'delete.html')


def edit (request,pk):
   
   item=Product.objects.get(id=pk)

   if request.method=="POST":
      editproduct=ProductForm(request.POST,instance=item)
      if editproduct.is_valid():
       editproduct.save()
       edited=editproduct.cleaned_data.get('name' )
       messages.success(request,f'you have edited {edited} successfully')
       return redirect('dashboard-product')
        
   else:
     editproduct=ProductForm(instance=item)

     context={
       'editproduct':editproduct
     }

     return render(request,'edit.html',context)




@login_required(login_url='login')
def order(request):
  context={
    'orders':Order.objects.all(),
  }
  return render(request,'order.html',context)





