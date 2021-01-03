from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

from .forms import Orderform, signupform , loginform
from .models import customer,product,deepak,signdata

# Create your views here.
def signuppage(request):
    form = signupform()
    if request.method == 'POST':
        form = signupform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("signuppage")
    context = {'form': form}
    return render(request, "signup.html", context)

def loginpage(request):
    context = {}
    if request.method == 'POST':
        try:
            userdetails = signdata.objects.get(sign_username = request.POST['sign_username'] , sign_password = request.POST['sign_password'])
            print(userdetails)
            request.session['sign_username'] = userdetails.sign_username
            return render(request,"home1.html")
        except signdata.DoesNotExist as e:
            messages.success(request,"invalid")
    return render(request,"login.html",context)
        

        

def savelogin(request):
    us=request.POST.get('loginusername')
    pw=request.POST.get('loginpassword')
    objj = deepak(use_name=us,use_password=pw)
    objj.save()
    return redirect("homepage")

def savesignup(request):
    signus=request.POST.get('signupusername')
    signem=request.POST.get('signupemail')
    signpw=request.POST.get('signuppassword')
    signpwconf=request.POST.get('signuppasswordconf')
    signobj=signdata(sign_username=signus,sign_email=signem,sign_password=signpw,sign_passwordconf=signpwconf)
    signobj.save()
    return redirect("homepage")
    
def basefile(request):
    context = {}
    return render(request, 'base.html' , context)

def homepage(request):
    context={}
    return render(request,'home1.html', context)

def aboutuspage(request):
    context={}
    return render(request,'about.html',context)

def contactuspage(request):
    context={}
    return render(request,'contact.html',context)
@csrf_exempt
def findbikepage(request):
    prod = product.objects.all()
    print(prod)
    n = len(prod)
    context={'range':range(1,n), 'prod':prod}
    return render(request,'findbike.html',context)

def products(request,id):
    return render(request,"productview.html")
    

def bookingpage(request):
    context={}
    return render(request,'booking.html', context)
@csrf_exempt
def savedata(request):
    cn=request.POST.get('name')
    pd=request.POST.get('pdate')
    pt=request.POST.get('ptime')
    dd=request.POST.get('ddate')
    dt=request.POST.get('dtime')
    vn=request.POST.get('vname')
    obj=customer(cust_name=cn,pickdate=pd,picktime=pt,dropdate=dd,droptime=dt,vehname=vn)
    obj.save()
    return render(request,"next.html")

def testpage(request):
    return render(request,"test.html")

@csrf_exempt
def testsave(request):
    pr_n=request.POST.get("pn")
    pr_p=request.POST.get("pr")
    objc=product(pro_name=pr_n,price=pr_p)
    objc.save()
    context={'ob':objc}   
    return render(request,"final.html",context)





