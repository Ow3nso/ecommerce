from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import *

# Create your views here.

@login_required(login_url='login')
def home(request):

    list = List.objects.all()
    item = Item.objects.all()
    form = Inquireform

    if request.method=="POST":
        form = Inquireform(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Message sent successfully')
            return redirect('/')

    context = {'list':list, 'item':item, 'form':form}

    return render(request, 'home.html', context)

@login_required(login_url='login')
def additem(request):

    form = ItemForm

    list = List.objects.all()

    if request.method=="POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Item added successfully")
            return redirect('/')
        else:
            messages.success(request, 'Item could not be added. Invalid form')
            return redirect('additem')

    context = {'form':form, 'list':list}
    return render(request, 'additem.html', context)

@login_required(login_url='login')
def shoes(request):

    list = List.objects.all()
    item = Item.objects.all()
    form = Inquireform

    if request.method=="POST":
        form = Inquireform(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Message sent successfully')
            return redirect('/')

    context = {'list':list, 'item':item, 'form':form}

    return render(request, 'shoes.html', context)

@login_required(login_url='login')
def blazers(request):

    list = List.objects.all()
    item = Item.objects.all()
    form = Inquireform

    if request.method=="POST":
        form = Inquireform(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Message sent successfully')
            return redirect('/')

    context = {'list':list, 'item':item, 'form':form}

    return render(request, 'blazers.html', context)

@login_required(login_url='login')
def dresses(request):

    list = List.objects.all()
    item = Item.objects.all()
    form = Inquireform

    if request.method=="POST":
        form = Inquireform(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Message sent successfully')
            return redirect('/')

    context = {'list':list, 'item':item, 'form':form}

    return render(request, 'dresses.html', context)

@login_required(login_url='login')
def gym(request):

    list = List.objects.all()
    item = Item.objects.all()
    form = Inquireform

    if request.method=="POST":
        form = Inquireform(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Message sent successfully')
            return redirect('/')

    context = {'list':list, 'item':item, 'form':form}

    return render(request, 'gym.html', context)

@login_required(login_url='login')
def jackets(request):

    list = List.objects.all()
    item = Item.objects.all()
    form = Inquireform

    if request.method=="POST":
        form = Inquireform(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Message sent successfully')
            return redirect('/')

    context = {'list':list, 'item':item, 'form':form}

    return render(request, 'jackets.html', context)

@login_required(login_url='login')
def jeans(request):

    list = List.objects.all()
    item = Item.objects.all()
    form = Inquireform

    if request.method=="POST":
        form = Inquireform(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Message sent successfully')
            return redirect('/')

    context = {'list':list, 'item':item, 'form':form}

    return render(request, 'jeans.html', context)

@login_required(login_url='login')
def makeup(request):

    list = List.objects.all()
    item = Item.objects.all()
    form = Inquireform

    if request.method=="POST":
        form = Inquireform(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Message sent successfully')
            return redirect('/')

    context = {'list':list, 'item':item, 'form':form}

    return render(request, 'makeup.html', context)

@login_required(login_url='login')
def other(request):

    list = List.objects.all()
    item = Item.objects.all()
    form = Inquireform

    if request.method=="POST":
        form = Inquireform(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Message sent successfully')
            return redirect('/')

    context = {'list':list, 'item':item, 'form':form}

    return render(request, 'other.html', context)

@login_required(login_url='login')
def shirts(request):

    list = List.objects.all()
    item = Item.objects.all()
    form = Inquireform

    if request.method=="POST":
        form = Inquireform(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Message sent successfully')
            return redirect('/')

    context = {'list':list, 'item':item, 'form':form}

    return render(request, 'shirts.html', context)

@login_required(login_url='login')
def update(request, itemid):

    item = Item.objects.get(pk=itemid)

    form = ItemForm(request.POST or None, instance=item)

    if request.method=="POST":
        
        if form.is_valid:
            form.save()
            messages.success(request, 'Item updated successfully')
            return redirect('/')

    context = {'form':form, 'item':item}
    return render(request, 'update_item.html', context)

@login_required(login_url='login')
def delete(request, itemid):

    item = Item.objects.get(pk=itemid)

    item.delete()

    return redirect('/')

def login_user(request):

    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, ("Invalid username or password"))
            return redirect('login')

    else:

        return render(request, 'login.html')

@login_required(login_url='login')
def logout_user(request):

    logout(request)
    return redirect('login')

def register(request):
    form = Registerform

    if request.method=="POST":
        form = Registerform(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password1')
            user = authenticate(username=username, email=email, password=password)
            messages.success(request, ("Registration successful. Please Login"))
            return redirect('login')
        else:
            messages.success(request, 'Registration not Successfull')
            return redirect('register')

    else:
        form = Registerform()


    context = {'form':form}

    return render(request, 'register.html', context)

def search(request):

    if request.method =="POST":
        searched = request.POST['searched']
        item = Item.objects.filter(name__contains=searched)

        context = {'searched':searched, 'item':item}

        return render(request, 'home.html', context)

def chat(request):

    user = request.user

    form = MessageForm
    text = Message.objects.filter(user=user)
    users = get_user_model().objects.all()

    if request.method=="POST":
        form= MessageForm(request.POST)
        if form.is_valid:
            text = request.POST.get('text')
            message = Message(text=text)
            message.user = user
            message.save()
            return redirect('chat')

    context = {'users':users, 'form':form, 'text':text}

    return render(request, 'chat.html',context)

def view_item(request, itemid):

    items = Item.objects.all()

    form = Inquireform

    item = Item.objects.get(pk=itemid)

    if request.method=="POST":
        form = Inquireform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message sent successfully')
            return redirect('/')
        else:
            messages.success(request, 'There is an error with your form')
            return redirect('/')


    context = {'item':item, 'items':items, 'form':form}

    return render(request, 'view.html', context)

def order(request, itemid):

    item = Item.objects.get(pk=itemid)
    user = request.user
    form = OrderForm

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid:
            project = form.save(commit=False)
            project.user = user
            project.save()
            messages.success(request, 'Item ordered successfully. proceed to payment')
            return redirect('cart')

    context ={'item':item, 'form':form}

    return render(request, 'order.html', context)


def cart(request):

    user = request.user
    cart = Cart.objects.filter(user=user)

    if request.method=="POST":
        img = request.POST.get('image')
        id = request.POST.get('item_id')
        pro = request.POST.get('product')
        price = request.POST.get('price')
        qty = request.POST.get('qty')
        total = int(qty) * int(price)


        if int(qty) > 0:
            user = request.user
            x = Cart(user=user, item_id=id, image=img, total=total, product=pro, quantity=qty)
            messages.success(request, 'Items added to cart successfully')
            x.save()

        

    context = {'cart':cart}
    
    return render(request, 'cart.html', context)


"""
def cart(request):

    cart = Cart.objects.all
    if request.method=="POST":
        id = request.POST.get('item_id')
        pro = request.POST.get('product')
        qty = request.POST.get('qty')
    
        
        if int(qty) > 0:
            user = request.user
            x = Cart(user=user, item_id=id, product=pro, quantity=qty)
            x.save()

            context = {'cart':cart}
            return render(request, 'cart.html', context)


"""

def dele(request, cartid):

    cart = Cart.objects.get(pk=cartid)

    cart.delete()

    return redirect('cart')