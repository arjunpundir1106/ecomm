from django.shortcuts import render,HttpResponse
from django.views import View
from . models import Product
from django.db.models import Count
from . forms import CustomerRegistrationForm,CustomerProfileForm
from django.contrib import messages
from .models import Customer,Cart



# Create your views here.

def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

class category(View):
    def get(self,request,val):
        product = Product.objects.filter(category=val) 
        title = Product.objects.filter(category=val).values('title').annotate(total=Count('title')) 
        return render(request,"category.html",locals())
    
class ProductDetail(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request,"productDetail.html",locals())
    
class categoryTitle(View):
    def get(self,request,val):
        product = Product.objects.filter(title=val) 
        title = Product.objects.filter(category=product[0].category).values('title') 
        return render(request,"category.html",locals())
    
class CustomerRegistrationView(View):
    def get(self,request):
        form=CustomerRegistrationForm()
        return render(request,'customerRegistration.html',locals())
    def post(self,request):
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Congratulations! User Registered Successfully")
        else:
            messages.error(request,"Invalid Input Data")
        return render(request,'customerRegistration.html')
    
class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm
        return render(request,'profile.html',locals())

    def post(self,request):
        form=CustomerProfileForm(request.POST)
        if form.is_valid():
            user=request.user
            name = form.cleaned_data['name']
            mobile = form.cleaned_data['mobile']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']

            reg = Customer(user=user,name=name,mobile=mobile,locality=locality,city=city,state=state,zipcode=zipcode)
            reg.save()
            messages.success(request,"Congratulations! Profile Saved Successfully")
        else:
            messages.error(request,"Invalid Input Data")
        return render(request,'profile.html',locals())
    

def address(request):
    add= Customer.objects.filter(user=request.user)
    return render(request,'address.html',locals())


class updateAddress(View):
    def get(self,request):
        add = Customer.objects.get(pk=1)
        form = CustomerProfileForm(instance=add)
        return render(request,'updateAddress.html',locals())

    def post(self,request):
        form=CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.name=form.cleaned_data['name']
            add.locality=form.cleaned_data['locality']
            add.city=form.cleaned_data['city']
            add.mobile=form.cleaned_data['mobile']
            add.zipcode=form.cleaned_data['zipcode']
            add.state=form.cleaned_data['state']
            add.save()
            messages.success(request,"Congratulations! Profile Updated Successfully")
        else:
            messages.error(request,"Invalid Input Data")
        return redirect("address")
        


def add_to_cart(request):
    product_id = request.GET.get('prod_id')
    user = request.user
    product=Product.objects.get(id=product_id)
    Cart(user=user,prouct=product).save()
    return redirect("/showcart")

def show_cart(request):
    user=request.user
    cart = Cartt.objects.filter(user=user)
    return render(request,'addtocart.html',locals())



