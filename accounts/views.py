from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
from django.http import HttpResponse
from django.contrib import messages, auth 
from django.contrib.auth.models import User
from smtplib import SMTPException
from email.message import EmailMessage
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from .models import Department, Employee



# Create your views here.

def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    else:
        return render(request,'login.html')    

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            else:   
                user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name,last_name=last_name)
                user.save();
                print('user created')
                return redirect('login')

        else:
            messages.info(request,'password not matching..')    
            return redirect('register')
        return redirect('/')
        
    else:
        return render(request,'register.html')



def logout(request):
    auth.logout(request)
    return redirect('/')       


#email

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            
            # Save the form data to the database
            contact = Contact(
                name=form.cleaned_data['name'],
                phone=form.cleaned_data['phone'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            contact.save()


            send_mail(
                 'Testing Mail',
                 'Here is the message.',
                 'testingonly552@gmail.com',
                 ['testingprojectd@gmail.com'],
                 fail_silently=False,
            )  

              
            messages.success(request, 'Thank you for your message! We will get back to you shortly.')
            return redirect('contact')  # Redirect to the same page to avoid resubmission
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()

    
    return render(request, 'contact.html', {'form': form})


# View to list all departments
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'department_list.html', {'departments': departments})

# View to list all employees
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

# View to display a specific department's details and its employees
def department_detail(request, pk):
    department = get_object_or_404(Department, pk=pk)
    employees = department.employees.all()
    return render(request, 'department_detail.html', {'department': department, 'employees': employees})

# View to display a specific employee's details
def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'employee_detail.html', {'employee': employee})

