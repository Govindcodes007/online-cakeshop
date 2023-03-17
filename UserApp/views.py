from django.shortcuts import render,redirect
from django.http import HttpResponse
from AdminApp.models import Category,Cake
from UserApp.models import UserInfo,Cart,Payment
# Create your views here.

def homepage(request):
    cats = Category.objects.all()
    cakes =Cake.objects.all()
    return render(request,'master.html',{'cats':cats,'cakes':cakes})

def ShowCakes(request,cid):
    cats = Category.objects.all()
    cat = Category.objects.get(id=cid)
    #Filter method is used to fetch more than 1 objects
    #It returns collection of objects
    cakes = Cake.objects.filter(category=cat)
    return render(request,"master.html",{"cats":cats,"cakes":cakes})

def ViewDetails(request,id):
    cats = Category.objects.all()
    cake = Cake.objects.get(id=id)
    return render(request,"ViewDetails.html",{"cats":cats,"cake":cake})
        
def Login(request):
    cats = Category.objects.all()
    if(request.method == "GET"):
        return render(request,"Login.html",{"cats":cats})
    else:
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        try:
            user = UserInfo.objects.get(username = uname,password=pwd)
        except:
            return redirect(Login)
        else:
            request.session["uname"]=uname
            return redirect(homepage)
        
def SignUp(request):
    cats = Category.objects.all()
    if(request.method == "GET"):
        return render(request,"SignUp.html",{"cats":cats,})
    else:
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        email = request.POST["email"]

        user = UserInfo(uname,pwd,email)
        user.save()
        return redirect(homepage)

def Logout(request):
    request.session.clear()
    return redirect(homepage)

def addToCart(request):
    if(request.method == "POST"):
        if("uname" in request.session):
            user = UserInfo.objects.get(username = request.session["uname"])
            cake = Cake.objects.get(id = request.POST["cake_id"])
            qty = request.POST["qty"]   
            #Before adding to cart we need to check for duplicate entry
            try:
                cart_item = Cart.objects.get(user = user,cake=cake)
            except:
                #Add item to cart
                cart_item = Cart()
                cart_item.user = user
                cart_item.cake = cake
                cart_item.qty = qty
                cart_item.save()
                return redirect(homepage)
            else:
                return HttpResponse("Item already in cart")              
        else:
            return redirect(Login)
    else:
        return redirect(Login)
    
def ShowAllCartItems(request):
    uname = request.session["uname"]
    user = UserInfo.objects.get(username = uname)
    if(request.method == "GET"):       
        items = Cart.objects.filter(user = user)
        cats = Category.objects.all()
        total = 0
        for item  in items:
            total += float(item.cake.price) * float(item.qty)
        request.session["total"] = total
        return render(request,"ShowAllCartItems.html",{"items":items,"cats":cats})
    else:
        action = request.POST["action"]
        cake_id = request.POST["cake_id"]
        cake = Cake.objects.get(id=cake_id)
        item = Cart.objects.get(user=user,cake=cake)
        
        if(action=="update"):
            qty = request.POST["qty"]
            item.qty = qty
            item.save()
        else:            
            item.delete()            
        return redirect(ShowAllCartItems)

def MakePayment(request):
    if(request.method == "GET"):
        return render(request,"MakePayment.html",{})
    else:
        card_no = request.POST["card_no"]
        cvv = request.POST["cvv"]
        expiry = request.POST["expiry"]

        try:
            buyer = Payment.objects.get(card_no=card_no,cvv=cvv,expiry=expiry)
        except:
            return render(request,"MakePayment.html",{"msg":"Invalid card details"})
        else:
            owner = Payment.objects.get(card_no="1111",cvv="111",expiry="12/2030")
            total = request.session["total"]
            buyer.balance -= total
            owner.balance += total
            buyer.save()
            owner.save()
            #Delete the cart items
            uname = request.session["uname"]
            user = UserInfo.objects.get(username = uname)
            items = Cart.objects.filter(user=user)
            for item in items:
                item.delete()
            
            return HttpResponse("Your order has been placed successfuly...")





    
        
