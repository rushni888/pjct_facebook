from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *

# Create your views here.
def index(request):
    return HttpResponse("hello it worked!!")

def signup(request):
    if request.method=="POST":
        try:
            user=request.POST["uname"]
            pwd=request.POST["pass"]
            loginobj=LoginDummy(user=user,pwd=pwd)
            loginobj.save()
            return render(request,"login.html",{"msg":"user saved"})
        except Exception as error:
            print(e)
            return render(request,"login.html",{"msg":"error"})
    else:
        return render(request,"signup.html")   

def login(request):
    if request.method=='POST':
        user=request.POST["uname"]
        pwd=request.POST["pass"] 
        user_exist=LoginDummy.objects.filter(user=user).exists()
        if user_exist:
            userobj=LoginDummy.objects.get(user=user,pwd=pwd)
            if userobj:
                request.session['userid']=userobj.id
                print(userobj.id)
                return redirect('/fb_app/viewprofile')               
            else:
                return HttpResponse("no such user")
        else:
            return HttpResponse("no such user")
    else:
        return render(request,"login.html")

def viewprofile(request):  
    if request.method=="POST":
        user_id=request.session['userid']
        user=request.POST["uname"]
        pwd=request.POST["pass"] 
        log_details=LoginDummy.objects.get(id=user_id) 
        log_details.user=user
        log_details.pwd=pwd
        log_details.save()
        print(log_details)
        return render(request,"viewprofile.html",{"log_details": log_details})  
    print("-------------")  
    user_id=request.session['userid']
    print("userid is: ",user_id)
    log_details=LoginDummy.objects.get(id=user_id) 
    return render(request,"viewprofile.html",{"log_details": log_details}) 

def forgotpass(request):
    return render(request,"forgotpass.html")
def bootstrapgrid(request):
    return render(request,"bootstrap grid.html")

def fbhome(request):
    if request.method=="POST":        
        firstname=request.POST["firstname"] 
        lastname=request.POST["lastname"]
        username=request.POST["username"]
        password=request.POST["password"]
        day = request.POST.get('day')
        month = request.POST.get('month')
        year = request.POST.get('year')
        if day!=None and month!=None and year!=None:
            formatted_date=year+"-"+month+"-"+day            
            print(formatted_date)
           
        # gender1=request.POST["gender"] this arises multivalue dict error
        gender = request.POST.get('gender')
        try:
            logobj=Login(username=username,password=password)
            logobj.save()
        except NameError:
            return render(request,'dynamicdata1.html',{'error':'Login doesnot exist'},)   
        else:     
            user_obj = UserDetails(firstname=firstname, lastname=lastname, dob=formatted_date, gender=gender, user_id=logobj)
            user_obj.save()
            return HttpResponse("Registered sccessfully")  
    else:   
        return render(request,"fbhome.html")

def fbhomedummy(request):
    return render(request,"fbhomedummy.html") 
def samplejs(request):
    return render(request,"samplejs.html")   
def navbar(request):
    return render(request,"navbar.html")
def home(request):
    return render(request,"home.html")
def jquery(request):
    return render(request,"jquery.html")

def dynamicdata1(request):
    try:       
        # class Destination:
        #     id:int
        #     name:str
        #     img:str
        #     desc:str
        #     price:int
        
        dest1=Destination()
        dest1.id=1
        dest1.name="banglore"
        dest1.price=456
        dest1.desc="beutiful city"
        dest1.img='logo.jpg'
        return render(request,'dynamicdata1.html',{'dest1':dest1})
    except Exception as ex:
        return HttpResponse(ex)
    # except NameError:
    #     return render(request,'dynamicdata1.html',{'error':'destination is not defined'},)
   


    # return render(request,'landingpage.html',{'dest1':700}){{dest1}}
    
def dynamicdata2(request):
    product1=Product()
    product1.name="Daniel klein"
    return render(request,"dynamicdata2.html")

def layout(request):
    return render(request,"layout.html")
