import email
from django.shortcuts import redirect, render
from django.template import context
from .forms import RegistrationForm
from .models import RegistrationModel
from django.http import HttpResponse
from cryptography.fernet import Fernet

# Create your views here.
def encryptpassword(password):
        key =Fernet.generate_key()
        fernet =Fernet(key)
        encpassword=fernet.encrypt(password.encode())
        return encpassword

def decryptpassword(password):
        key =Fernet.generate_key()
        fernet =Fernet(key)
        encpassword=fernet.decrypt(password.decode())
        return encpassword


def home(request):
    return render(request, 'authentic/home.html')


    
def login(request):
    if request.method  =='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        user=RegistrationModel.objects.get(email=email)
        
        if user:
            userfullname =user.fullname()
            usershortname=user.shortname()
            usernormalizeemail=user.normalizeEmail()
            userpassword =user.password
            username=user.__str__()
            
            return HttpResponse(f'The user full name is <br>"{userfullname}";<br><br>username is <br>"{username}"<br><br>and his password is <br>"{userpassword}"')

    return render(request, 'authentic/login.html')

def register(request):
    form = RegistrationForm()
    if  request.method == 'POST':
        username=request.POST.get('username')
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        email  = request.POST.get('email')
        password = encryptpassword(request.POST.get('password'))
        user = RegistrationModel(username=username,f_name=f_name,l_name=l_name,email=email ,password=password)
        user.save()
        return redirect('login')
    context = {'form':form}
    return render(request, 'authentic/register.html',context)    