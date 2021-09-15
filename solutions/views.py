from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django .shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from brainix1 import *
import razorpay

# Create your views here.
def home(request):
    context = {}
    return render (request, 'index.html',context)

@csrf_exempt
def success(request):
    if request.method == "POST":
        a = request.POST
        print(a)
    
    return render (request, 'success.html')
@csrf_exempt
def trial_workshop_registration_success(request):
    if request.method == "POST":
        a = request.POST
        print(a)
    
    return render (request, 'trial_success.html')
        
@csrf_exempt
def failed(request):
    if request.method == "POST":
        a = request.POST
        print(a)
    
    return render (request, 'fail.html')
    
  
def about(request):
    context = {}
    return render (request, 'about.html',context)
    
  
def pay(request):
    
    if request.method == 'POST':
        amount = 199900
        client = razorpay.Client(auth=('rzp_test_OOyILZb0j2zQfh','emxRvTKcJ3T9mBlZzWFA665R'))
        response_payment = client.order.create(dict(amount = amount, currency='INR',payment_capture='1'))
        print(response_payment)
        for value in response_payment:
            if (response_payment['status'] == 'created'):
                return redirect ('success')
            else:
                return redirect ('failed')
    return render (request, 'test_pay.html',)
def testpage(request):
    context = {}
    return render (request, 'base.html',context)

def gallery(request):
    context = {}
    return render (request, 'gallery.html',context)
def gallery1(request):
    context = {}
    return render (request, 'gallery1.html',context)

def workshop(request):
    context = {}
    return render (request, 'workshop.html',context)


from django.core.mail import EmailMessage 
from django.conf import settings
from django.template.loader import render_to_string 

def checkout(request,pk_test):
    

    checkout_details = Payworkshop.objects.get(id=pk_test)
    email_id = checkout_details.email
    name = checkout_details.fname
    orderid = checkout_details.order_id
    id = checkout_details.id
    phno = checkout_details.phno
    
    if request.method == 'POST':
        amount = 199900
        client = razorpay.Client(auth=('rzp_live_Xc3fyKMq1KOaQi','4b0qzbWEJ2mSPXR0tprhQVhW'))
        response_payment = client.order.create(dict(amount = amount, currency='INR',payment_capture='1'))
        print(response_payment)
        checkout_details.razorpay_id = response_payment['id']
        
        checkout_details.save()

        for value in response_payment:
            if (response_payment['status'] == 'created'):
                send_mail(
                    'Brainix Online Science Workshop',
                    "Payment for registration is successfully recieved.We will send you the meet details soon.",
                    settings.EMAIL_HOST_USER,
                    [email_id],
                    fail_silently=False,
                )
                
               
                return redirect ('success')
            else:
                return redirect ('failed')

   
    return render (request, 'billingpage.html',{"checkout_details":checkout_details})
  

        
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        obj = Feedbackform.objects.create (name = name, email = email, subject = subject, message = message)
        obj.save()
    return render(request, 'contact.html')

def trial_form(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        dob = request.POST['dob']
        gender = request.POST['gender']
        pname = request.POST['pname']
        email = request.POST['email']
        phno = request.POST['phno']
        address = request.POST['address']
        spref = request.POST['spref']
        lpref = request.POST['lpref']
        obj = Trialworkshop.objects.create (fname = fname, lname= lname, dob = dob, gender = gender, pname = pname, email = email, phno = phno, address = address, spref = spref, lpref = lpref)
        obj.save()
        return redirect('trial_workshop_registration_success')
        
    return render (request, 'trial-form.html')

i = 0

def pay_form(request):
    obj = Payworkshop.objects.last()
    if obj != None:
        id = obj.id + 1
    else:
        id = 1
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        dob = request.POST['dob']
        gender = request.POST['gender']
        pname = request.POST['pname']
        email = request.POST['email']
        phno = request.POST['phno']
        address = request.POST['address']
        spref = request.POST['spref']
        lpref = request.POST['lpref']
        obj = Payworkshop.objects.create (fname = fname, lname= lname, dob = dob,gender = gender, pname = pname, email = email, phno = phno, address = address, spref = spref, lpref = lpref, id = id )
        obj.save()
        
        return redirect(f'/checkout/{id}')

    context = {'id':id}
        
    return render (request, 'payworkshop.html',context)
