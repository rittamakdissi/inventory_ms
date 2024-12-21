from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib import auth,messages
from . forms  import RegisterForm
from django.contrib.auth.models import User
from . models import Profile
from .forms  import UserUpdateForm 
from .forms  import ProfileUpdateForm
from django.contrib import messages
# Create your views here.




def register(request):# sign up هي يعني 
    if request.method=="POST":
        form= RegisterForm(request.POST)
        if form.is_valid():
            form.save()    
            username=form.cleaned_data.get('username')
            messages.success(request,f'accout has been created for {username} please login ')
            return redirect('login')       
    else:
     form= RegisterForm()
     #return redirect('dashboard-index')
    context={
       'form': RegisterForm()
     }
    return render(request,'user/register.html',context)



def login (request):
   if request.method=='POST':
          username=request.POST['username']
          email=request.POST['email']
          password=request.POST['password']
          user=auth.authenticate(username=username,password=password,email=email)

          if user is not None:
               auth.login(request,user)
               return redirect ('dashboard-index') 
          else :
              messages.info(request,'wrong information') 
              return redirect ('login') 

   else: 
      return render(request,'user/login.html')

      # return render(request,'user/login.html')



def logout (request):
   
   return render(request,'user/logout.html')



def profile (request):
   context={
       'profile':Profile.objects.all(),


   }
   
   return render(request,'user/profile.html',context)


def profile_update (request):
   if  request.method=='POST':
       userform=UserUpdateForm(request.POST,instance=request.user)
       profileform=ProfileUpdateForm(request.POST,instance=request.user.profile)#request.files هي لو كنت ضايفة صورة فيه
       
       if userform.is_valid() and profileform.is_valid():
            userform.save()
            profileform.save()
            return redirect('profile')
   
   else:
      userform=UserUpdateForm(instance=request.user)  
      profileform=ProfileUpdateForm(instance=request.user.profile)
 

   context={
       
       'userform':userform,
       'profileform':profileform,

   }
   return render(request,'user/profile_update.html',context)



