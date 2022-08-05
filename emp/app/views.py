
import email
from django.shortcuts import render
from .forms import UserForm,LoginForm
from django.db.models import Q
from .models import registration



def home(request):
    return render(request,'home.html')

def create(request):
    if request.method=='POST':
        fm=UserForm(request.POST)
        if fm.is_valid():
            uname = request.POST['name']
            uemail = request.POST['email']
            ucontact = request.POST['contact']
            q1=Q(name=uname)
            q2=Q(email=uemail)
            q3=Q(contact=ucontact)
            (q1 & q2 & q3)
            if registration.objects.filter(q1):
                error1="Username Already Exist!!"
                fm=UserForm()
                return render(request,'register.html',{'form':fm,'msg1':error1})
            elif registration.objects.filter(q2):
                error1="Contact Already Exist!!"
                fm=UserForm()
                return render(request,'register.html',{'form':fm,'msg2':error1})
            elif registration.objects.filter(q3):
                error1="Email Already Exist!!"
                fm=UserForm()
                return render(request,'register.html',{'form':fm,'msg3':error1})
            else:

                fm.save()
                text = "User Created Successfully"
                return render(request,'register.html',{'form':fm,'msg':text})
    else:
        fm=UserForm()
    return render(request,'register.html',{'form':fm})



def details(request):
    data= registration.objects.all()
    return render(request,'details.html',{'dat':data})


def login(request):
    lf = LoginForm()
    if request.method=='POST':
        uname = request.POST['username']
        upass = request.POST['password']
        q1=Q(name=uname)
        q2=Q(password=upass)
        u1=registration.objects.filter(q1 & q2)
        if u1:
            text = "User Logged-In Successfully"
            return render(request,'home.html',{'msg1':text})
        else:
            text ="No User Found!"
            return render(request,'home.html',{'msg2':text})
    else:
        return render(request,'login.html',{'loginform':lf})
       