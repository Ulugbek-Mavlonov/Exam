from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import *

# Create your views here.

# foydalanuvchi login orqali otuvchi funk
def login_user(request):
    
    if request.method == 'POST':
        username= request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username= username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index/')
        
            
    return render(request, 'login.html')

#  foydalanuvchilarni registratsiyadan otkazish
def register(request):
    form=UserCreationForm()
    context={
        "form":form
    }
    if request.method == "POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    return render(request, 'register.html', context)

# chiqib ketish
def logout(request):
    return render(request, 'login.html', name='logout')

# asosiy sahifada mahsulotlarni chiqarish

def index(request):
    rey= Product.objects.all()
    context={
        'rey':rey
    }
    return render(request, 'index.html', context)

# mahsulotlrni qidirish
def search(requests):
    
    title = requests.GET.get('title')
    if len(list(title))>0:
        product = Product.objects.filter(title__icontains=title)
        return render(requests, 'search.html', {'product': product})
    else:
        return index(requests)
    
# mahsulotlarni korzinkaga qo'shish
def add_basket(request):
    num= request.GET.get('user_id')
    user = User.objects.get(id=num)
    id=request.GET.get('id')
    users_id = Less.objects.all()
    lists=[]
    for i in users_id:
        lists.append(i.number)
        
    if int(id) not in lists:
        number = Less(
        number = id,
        user = user,
        quantity = 1
        )
        number.save()
    else :
        number = Less.objects.filter(number=id, user=user)
        number.delete()
    return redirect('index/')

# basket.html o'tkazish
def basket(request):
    user_id= request.GET.get('user_id')
    user = User.objects.get(id = user_id)
    product = Less.objects.filter(user=user)
    rey = Product.objects.all()
    price =0
    for i in product:
        for l in rey:
            if i.number == l.id :
                price +=l.price
    return render(request, 'basket.html', {'product':product, 'rey':rey, 'price':price})


# savatdagi productni o'chirish

def delete(request, id):
    products_pk = Less.objects.get(id=id)
    products_pk.delete()
    return render(request,'index.html')


# mahsulot malumotlariga o'tish
def detail(request, id):
    rey=Product.objects.get(id=id)
    context={
        'rey':rey
    }
    return render(request, 'detail.html', context)

# sotib olish
def order(request, user_id):
    if request.method =='POST':
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        user_name = User.objects.get(id=user_id)
        sum = Less.objects.filter(user=user_name)
        for i in sum:
            user = i.user
            product = Product.objects.get(id = i.number)
            quantity=i.quantity
            rey = Order(first_name=first_name, email=email, phone=phone, user=user, book=product, quantity=quantity )
            rey.save()
            num=Less.objects.filter(user=user_name)
            num.delete()
        return redirect('/index/')
    return render(request, 'order.html')  

# xaridlar tarixini ko'rish
def history(request, user_id):
    num = Order.objects.filter(user= user_id)
    rey = Product.objects.all()
    return render(request, 'istory.html', {'rey':rey, 'num':num })
    
 

    
