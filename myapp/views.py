from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from myapp.models import Addproduct
from myapp.models import Bag
from myapp.models import Order
from myapp.models import Contact
from django.core.mail import send_mail
# Create your views here.

def index(request):
    data = Addproduct.objects.all()
    return render(request,"index.html",{"data":data})

def home(request):
    data = Addproduct.objects.all()
    if request.user.is_authenticated:
        username = request.user.username
        dd = Bag.objects.filter(username=username)
        context = {"data":data,"length":len(dd)}
        return render(request,"home.html",context)
    
    else:
        return redirect("/")

def SignUp(request):
    if request.method =="POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        cpassword = request.POST["cpassword"]

        
        d = User.objects.filter(username=username)
        if d:
            msg = "user already exist"
            return render(request,"Signup.html",{"msg":msg})
        else:
            if password == cpassword:
                div = User.objects.create_user(username = username,email = email,password=password)
                div.save()
                msg = "account generated"
                return render(request,"Signup.html",{"msg":msg})
            else:
                msg = "password does not match"
                print(msg)            
                return render(request,"Signup.html",{"msg":msg})
    else:
        return render(request,"Signup.html")
    
def log(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username = username , password= password)
        if user is not None:
            login(request,user)
            return redirect("/home")
        
        else:
            msg = "user not found"
            return render(request,"logIn.html",{"msg":msg})
    
    else:
        return render(request,"logIn.html")
def out(request):
    logout(request)
    return redirect("/home") 

def admindashboard(request):
    data = Addproduct.objects.all()
    b = Order.objects.all()
    n = Bag.objects.all()
    total = 0
    for i in b:
        total += int(i.total_price)

    context = {"data":len(data),"b":len(b),"total":total} 
    return render(request,"admindashboard.html",context)    

   
arr = ["div34"]
def admin(request):
    if request.method =="POST":
        adminid = request.POST["adminid"]
    
        if adminid in arr:
            return redirect("/admindashboard")       

        else:
            return render(request,"admin.html") 
    else:
        return render(request,"admin.html")


def addproduct(request):
    if request.method == "POST":
        productname = request.POST["productname"]
        productdescription = request.POST["productdescription"]
        productcategory = request.POST["productcategory"]
        offerprice = request.POST["offerprice"]
        actualprice = request.POST["actualprice"]
        stock = request.POST["stock"]
        productimage = request.FILES["productimage"]

        dev = Addproduct(productname=productname,productdescription=productdescription,productcategory=productcategory,offerprice=offerprice,actualprice=actualprice,stock=stock,productimage=productimage)
        dev.save()

        return render(request,"addproduct.html" , {"data":dev})
    else:
        return render(request,"addproduct.html")

def viewproduct(request):
    data = Addproduct.objects.all()
    return render(request,"viewproduct.html",{"data":data})  

def manageproduct(request):
     data = Addproduct.objects.all()
     return render(request,"manageproduct.html",{"data":data})

def desk(request,data):
    d = Addproduct.objects.get(id=data)
    d.delete()
    return redirect("/manageproduct")

def editt(request,data):
    div = Addproduct.objects.get(id=data)
    return render(request,"edit.html",{"data":div})

def upd(request,data):
    div = Addproduct.objects.get(id=data)
    if request.method == "POST":
        div.productname = request.POST["productname"]
        div.productdescription = request.POST["productdescription"]
        div.productcategory = request.POST["productcategory"]
        div.offerprice = request.POST["offerprice"]
        div.actualprice = request.POST["actualprice"]
        div.stock = request.POST["stock"]
        div.productimage = request.FILES["productimage"]
        div.save()
        return redirect("/manageproduct")

def cart(request,id):
    if request.user.is_authenticated:
        username = request.user.username

        if request.method == "POST":
            quantity = request.POST["quantity"]
            
            data = Addproduct.objects.get(id = id)
            total = int(data.offerprice) * int(quantity)

            divu = Bag(ProductId = id,product_name = data.productname,product_price = data.offerprice, quantity = quantity,total_price = total, username= username)
            divu.save()
            return redirect("/bag")
    else:
        return redirect("/home")
    
def bag(request):
    n = Bag.objects.all()
    total = 0
    for i in n:
        total += int(i.total_price)


    if request.user.is_authenticated:
        username = request.user.username
        data = Bag.objects.filter(username=username)
        context = {"data":data , "total":total}
        return render(request , "bag.html",context)
    else:
        return redirect("/home")

def dele(request,data):
    p = Bag.objects.get(id=data)
    p.delete()
    return redirect("/bag")

pro = []
def order(request):
    if request.user.is_authenticated:
        username = request.user.username
        data = Bag.objects.filter(username=username)
        total = 0
        for i in data:
            pro.append(i.product_name)
            total  = int(total) + int(i.total_price)

        if request.method=="POST":
            firstname=request.POST['firstname']
            lastname=request.POST['lastname']
            email=request.POST['email']
            contact=request.POST['contact']
            address=request.POST['address']
            payment=request.POST['payment']
            card_number=request.POST['card_number']
            cvv=request.POST['cvv']
            expiry_date=request.POST['expiry_date']
            proorder = list(dict.fromkeys(pro))
            a=Order(firstname=firstname,lastname=lastname,email=email,contact=contact,address=address,total_product =proorder,total_price=total,payment=payment,card_number=card_number,cvv=cvv,expiry_date=expiry_date,status="waiting")
            a.save()
            pro.clear()
            Bag.objects.filter(username=username).delete()
            
            msg="ordered successfully"
            context={"total":total,"msg":msg}
            
            return render(request,"ordernow.html",context)
        else:
            context={"total":total,"pro":data}
            return render(request,"ordernow.html",context)
        
def vcustomer(request):
    dd= User.objects.all()
    return render(request,"viewcustomer.html",{"data":dd})

def vorder(request):
    o = Order.objects.all()
    return render(request,"vieworder.html",{"data":o})

def contact(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        message = request.POST["message"]
        subject = "welcome"
        msg = "hello"
        to = email
        req = send_mail(subject,msg,"divyanshu6939@gmail.com",[to])
        c=Contact(username=username,email=email,message=message)
        c.save()
        msg = "message sent"
        return render(request,"contactus.html",{"msg":msg})
    
    else:
        return render(request,"contactus.html")
    
def status(request,id):
    data = Order.objects.get(id=id)
    if request.method == "POST":
        data.status = request.POST["status"]
        data.save()
        return redirect("/vieworder")
    else:
        return render(request,"vieworder.html")      

def about(request):
    return render(request,"aboutus.html")    
    
def mail(request):
    subject = "welcome"
    msg = "hello"
    to = "divyanshu1342003@gmail.com"
    req = send_mail(subject,msg,"divyanshu6939@gmail.com",[to])
    if req:
        return HttpResponse("sent") 
    else:
        return HttpResponse("not sent") 
    
def track(request):
    if request.user.is_authenticated:
        username = request.user.username
        data = Bag.objects.filter(username=username)
        data = Order.objects.all()
        return render( request,"trackorder.html",{"data":data})    
    else:
        return render(request,"trackorder.html")
  