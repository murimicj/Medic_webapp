from django.shortcuts import render,redirect
from myapp.models import Appointment
# Create your views here.
def index(request):
    return render(request,'index.html')

def service(request):
    return render(request,'service-details.html')

def starter(request):
    return render(request,'starter-page.html')

def appointment(request):
    if request.method == "POST":
        myappointment=Appointment(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            date=request.POST['date'],
            department=request.POST['department'],
            doctor=request.POST['doctor'],
            message=request.POST['message'],

        )
        myappointment.save()
        return redirect('/appointment')
    else:
        return render(request,'appointment.html')




