from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,HttpResponseRedirect
from .forms import  LoginForm, SignUpForm
from django.contrib import messages
from .models import Contact,Event,Bharatanatyam_Event,Painting_Event,Mohiniyattam_Event,Mime_Event,Groupsong_Event,Groupdance_Event

# Create your views here.

def home(request):
    return render(request,'core/home.html')
def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        contact=Contact(name=name,email=email,subject=subject,message=message)
        contact.save()
    
    return render(request,'core/contact.html')
    
def about(request):
    return render(request,'core/about.html')
def events(request):
    if request.user.is_authenticated:
        return render(request,'core/event.html')
    else:
        return HttpResponseRedirect('/login/')
# eventregister
def eventregister(request):
  if request.method == 'POST':
      name=request.POST['name']
      Event_name=request.POST['name_of_event']
      address=request.POST['address']
      email=request.POST['email']
      phone_number=request.POST['phone_number']
      event=Event(name=name,email=email,Event_name=Event_name,address=address,phonenumber=phone_number)
      event.save()
    
  return render(request,'core/eventregister.html')

# bharatanatyam register
def bharatanatyam(request):
  if request.method == 'POST':
      name=request.POST['name']
      address=request.POST['address']
      email=request.POST['email']
      phone_number=request.POST['phone_number']
      bharatanatyam_event=Bharatanatyam_Event(name=name,email=email,address=address,phonenumber=phone_number)
      bharatanatyam_event.save()
    
  return render(request,'core/bharath.html')

# painting register
def painting(request):
  if request.method == 'POST':
      name=request.POST['name']
      address=request.POST['address']
      email=request.POST['email']
      phone_number=request.POST['phone_number']
      painting_event=Painting_Event(name=name,email=email,address=address,phonenumber=phone_number)
      painting_event.save()
    
  return render(request,'core/paint.html')

# Mohiniyattam register
def mohiniyattam(request):
  if request.method == 'POST':
      name=request.POST['name']
      address=request.POST['address']
      email=request.POST['email']
      phone_number=request.POST['phone_number']
      Mohiniyattam_event=Mohiniyattam_Event(name=name,email=email,address=address,phonenumber=phone_number)
      Mohiniyattam_event.save()
    
  return render(request,'core/mohini.html')

# Mime register
def mime(request):
  if request.method == 'POST':
      grpname=request.POST['grpname']
      address=request.POST['address']
      email=request.POST['email']
      phone_number=request.POST['phone_number']
      Mime_event=Mime_Event(Group_name=grpname,email=email,address=address,phonenumber=phone_number)
      Mime_event.save()
    
  return render(request,'core/mime.html')

# Groupsong register
def groupsong(request):
  if request.method == 'POST':
      grpname=request.POST['grpname']
      address=request.POST['address']
      email=request.POST['email']
      phone_number=request.POST['phone_number']
      Groupsong_event=Groupsong_Event(Group_name=grpname,email=email,address=address,phonenumber=phone_number)
      Groupsong_event.save()
    
  return render(request,'core/grpsong.html')

# Groupdance register
def groupdance(request):
  if request.method == 'POST':
      grpname=request.POST['grpname']
      address=request.POST['address']
      email=request.POST['email']
      phone_number=request.POST['phone_number']
      Groupdance_event=Groupdance_Event(Group_name=grpname,email=email,address=address,phonenumber=phone_number)
      Groupdance_event.save()
    
  return render(request,'core/grpdance.html')


# login
def user_login(request):
  if not request.user.is_authenticated:
    if request.method == 'POST':
        form=LoginForm(request=request,data=request.POST)
        if form.is_valid(): 
            uname=form.cleaned_data['username']
            upass=form.cleaned_data['password']
            user=authenticate(request,username=uname,password=upass) 
            if user is not None:
                login(request,user)
                messages.success(request,'Logged in !!') 
        return HttpResponseRedirect('/events/')
    else:

        form=LoginForm()
    return render(request,'core/login.html',{'form':form})
  else:
    return HttpResponseRedirect('/events/')  
# signup
def user_signup(request):
    if request.method == 'POST':
       
        form = SignUpForm(request.POST)
        
        if form.is_valid():
           messages.success(request,'Congratulations !! Account was created !') 
           form.save()

    else:
          form = SignUpForm()

    return render(request, 'core/signup.html', {'form': form})
# logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
    