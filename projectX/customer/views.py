from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterUserForm
from .models import Employee

# Create your views here.
def loginCustomer(request):
    if request.method == "POST":
        username = request.POST['Username']
        password = request.POST['password']
        user = authenticate(request, username=username, password = password)
        if user is not None:
            login(request, user)
            return redirect("customer:home")
        else:
            messages.success(request, ("there is an error. try again"))
            return redirect("customer:login")

    else:
        return render(request, "customer/login.html", {})

def logoutCustomer(request):
    logout(request)
    messages.success(request, ("You are loged out"))
    return redirect("customer:login")


def index(request):
    if request.user.is_authenticated:   
        return render(request, "customer/index.html")
    else:
        messages.success(request, ("You have to log in first."))
        return redirect("customer:login")
        

def add(request):
    return render(request, "customer/register.html")

def form(request):
    if request.user.is_authenticated:
        return render(request, 'customer/form.html')
    else:
        messages.success(request, ('You have to log in first'))
        return redirect("customer:home")
        

def service(request):
    if request.user.is_authenticated:   
        return render(request, 'customer/services.html')
    else:
        messages.success(request, ('You have to log in first'))
        return redirect("customer:login")
        

def home(request):
    return render(request, 'customer/home.html')

def register(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid:
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
           
            user = authenticate(username=username, password=password)
            
            login(request, user)
            messages.success(request, ("You've Signed up now!"))
            return redirect("customer:home")
    else:
        form = RegisterUserForm()

    return render(request, 'customer/register.html', {
        "form": form  
    })

def join(request):
    if request.method == "POST" and request.FILES["userimage"]:
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        age = request.POST["age"]
        email = request.POST["email"]
        gender = request.POST["gender"]
        nic = request.POST["nic"]
        mobile = request.POST["mobile"]
        userimage = request.FILES["userimage"]


        if request.POST.getlist("garden"):
            garden = True
        else:
            garden = 'False'

        if request.POST.getlist("house"):
            house = True
        else:
            house = 'False'

        if request.POST.getlist("roof"):
            roof = True
        else:
            roof = 'False'

        if request.POST.getlist("pipe"):
            pipe = True
        else:
            pipe = 'False'

        if firstname and lastname and age and email and gender and nic and mobile and userimage:
            employee = Employee(
            firstname=firstname, 
            lastname=lastname, 
            age=age, 
            email=email, 
            mobile=mobile, 
            gender=gender, 
            nic=nic,
            image=userimage, 
            garden=garden, 
            house=house, 
            roof=roof, 
            pipe=pipe,
            )

            employee.save()
            return redirect("customer:list")
        
    else:
        messages.success(request, ("Attemp to join was unsuccessful"))
        return redirect("customer:form")

def profile(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'customer/index.html', {
        "employee": employee
    })

def list(request):
    if request.user.is_authenticated:
        employees = Employee.objects.all()
        return render(request, 'customer/emplist.html', {
            'employees': employees
        })
    else:
        messages.success(request, ("You have to log in first"))
        return redirect("customer:login")
        
def garden(request):
    employees = Employee.objects.all()
    return render(request, "customer/gardenn.html", {
        "employees": employees
    })

def pipe(request):
    employees = Employee.objects.all()
    return render(request, "customer/pipe.html", {
        "employees": employees
    })

def roof(request):
    employees = Employee.objects.all()
    return render(request, "customer/roof.html", {
        "employees": employees
    })

def house(request):
    employees = Employee.objects.all()
    return render(request, "customer/house.html", {
        "employees": employees
    })    