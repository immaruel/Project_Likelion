from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm,CreateUserForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group

from .filters import OrderFilter


from .crawling import get_food

# Create your views here.
def home(request):
    context ={}   
    return render(request, 'app/home.html',context)

@login_required(login_url = 'login')
@admin_only
def adminDashboard(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_orders = orders.count()
    total_customers = customers.count()

    item_ready = orders.filter(status='제품준비중').count()
    riding = orders.filter(status='배송중').count()
    delivered = orders.filter(status='배송완료').count()

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs
 

    context = {'orders':orders,  'customers':customers,
    'total_customers':total_customers,'delivered':delivered, 
    'riding':riding,'item_ready':item_ready, 'total_orders':total_orders,
    'myFilter':myFilter,}
    
    return render(request, 'app/dashboard.html',context)

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['admin'])
def customer(request,pk_test):
    customer = Customer.objects.get(id=pk_test)
    orders = customer.order_set.all()
    order_count = orders.count()

    context ={'customer':customer,'orders':orders,
    'order_count':order_count}
    
    return render(request, 'app/customer.html',context)

def product(request):
    context = {}
    return render(request, 'app/product.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
    orders = request.user.customer.order_set.all()
    
    total_orders = orders.count()
    #total_customers = customers.count()

    item_ready = orders.filter(status='제품준비중').count()
    riding = orders.filter(status='배송중').count()
    delivered = orders.filter(status='배송완료').count()

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    
    context = {'orders':orders, 'myFilter':myFilter,
    'delivered':delivered,'riding':riding,'item_ready':item_ready,
    'total_orders':total_orders, }

    return render(request, 'app/user.html',context)

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, '계정생성완료 ' + user)

            return redirect('login')
    
    context = {'form':form}
    return render(request, 'app/register.html',context)

@unauthenticated_user
def loginPage(request):
	# if request.user.is_authenticated:
	# 	return redirect('home')
	# else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)  

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request,'아이디 혹은 비밀번호가 잘못입력되었습니다!')
		context  = {}
		return render(request, 'app/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['admin'])
def createOrder(request):
	form = OrderForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/adminpage')

	context= {'form':form}
	return render(request, 'app/order_form.html',context)

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['admin'])
def updateOrder(request,pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['admin'])
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')
    context = {'item':order}
    return render(request, 'app/delete.html',context)


def bookFind(request):
    #food = get_food()
    return render(request)

