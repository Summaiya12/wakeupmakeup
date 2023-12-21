from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Product, Customer, Profile, User, Cart, Order, Contacts
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm, UserCustomerForm
from django.shortcuts import get_object_or_404


# Create your views here.

@login_required(login_url='register')
def Index(request):
    return render(request, 'index.html')


@login_required(login_url='register')
def About(request):
    return render(request, 'about.html')


@login_required(login_url='register')
def Carts(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = Cart.objects.get_or_create(product=product,
                                                    user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('show_cart')


def Show_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    total_items = sum(item.quantity for item in cart_items)
    return render(request, 'cart.html',
                  {'cart_items': cart_items, 'total_price': total_price, 'total_items': total_items})


def Remove_cart(request, item_id):
    cart_item = Cart.objects.get(id=item_id)
    cart_item.delete()
    return redirect('show_cart')


def Checkout(request):
    product = Product.objects.get(id=product_id)
    cart_item, created = Cart.objects.get_or_create(product=product,
                                                    user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('show_check')


def Show_check(request):
    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        eno = Order(name=name, address=address)
        eno.save()
        messages.success(request, 'Order Successfully..!')
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    total_items = sum(item.quantity for item in cart_items)
    return render(request, 'checkout.html',
                  {'cart_items': cart_items, 'total_price': total_price, 'total_items': total_items})


def Detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }
    return render(request, 'detail.html', context)


@login_required(login_url='register')
def Checkout(request):
    return render(request, 'checkout.html')


@login_required(login_url='register')
def Client(request):
    return render(request, 'clients.html')


@login_required(login_url='register')
def Contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact_message = Contacts.objects.create(name=name, email=email, message=message)
        contact_message.save()
    return render(request, 'contact.html')


def Login(request):
    if request.method == 'POST':
        users = request.POST.get("name")
        password = request.POST.get("pass")
        user = authenticate(request, username=users, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password in correct')
    return render(request, 'login.html')


@login_required(login_url='register')
def Products(request):
    return render(request, 'products.html')


def Logs(request):
    logout(request)
    return redirect('register')


def Register(request):
    if request.method == "POST":
        uname = request.POST.get("name")
        mail = request.POST.get("email")
        password = request.POST.get("pass")
        repass = request.POST.get("re_pass")
        if password != repass:
            messages.error(request, 'Both passwords must be same')
            return render(request, 'register.html')

        if len(password) < 5:
            messages.error(request, "Passwords must be long")
            return render(request, 'register.html')

        if User.objects.filter(email=mail).exists():
            messages.error(request, "Email Already Registered!!")
            return render(request, 'register.html')

        else:
            my_user = User.objects.create_user(uname, mail, password)
            my_user.save()
            messages.success(request, 'User Created Successfully..!')
            return redirect('login')

    return render(request, 'register.html')


@login_required(login_url='register')
def Profile(request):
    if request.method == 'POST':
        form = UserCustomerForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, 'Profile Added Successfully..!')
            # Save the data to the database
            return redirect('profile')  # Redirect to a success page
    else:
        form = UserCustomerForm()

    return render(request, 'profile.html', {'form': form})


@login_required(login_url='register')
def Address(request):
    add = Customer.objects.filter(user=request.user)

    return render(request, 'address.html', locals())


@login_required(login_url='register')
def Action(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, 'action.html', locals())


@login_required(login_url='register')
def Update(request, pk):
    obj = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = UserCustomerForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Update Successfully..!')
    else:
        form = UserCustomerForm(instance=obj)

    return render(request, 'update.html', {'form': form, 'obj': obj})


class CategoryView(View):
    @staticmethod
    def get(request, val):
        product = Product.objects.filter(category=val)
        return render(request, 'category.html', locals())
