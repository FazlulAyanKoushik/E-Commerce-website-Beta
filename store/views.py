from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from django.views import View
from .models.product import Product
from .models.category import Category
from .models.customer import Customer

# Create your views here.
class Index(View):
    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session.cart = {}
        category_id = request.GET.get('category')
        if category_id:
            products = Product.objects.filter(category = category_id)
        else:
            products = Product.objects.all()
        all_categories = Category.objects.all()
        return render(request, 'index.html', {'products': products, 'categories': all_categories})

    def post(self, request):
        product = request.POST.get('product_id')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:    
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        
        request.session['cart'] = cart
        print('cart ',request.session['cart'])
        print('You are : ',request.session.get('customer_email'))
        return redirect('homepage')





class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')
    
    def post(self, request):
        post_data = request.POST
        first_name = post_data.get('firstname')
        last_name = post_data.get('lastname')
        phone_no = post_data.get('phoneno')
        email = post_data.get('email')
        password = post_data.get('password')
        
        customer = Customer(first_name = first_name,
                            last_name = last_name,
                            phone_no = phone_no,
                            email = email,
                            password= password)       
        error_message = self.validationCustomer(customer)

        # save data
        if (not error_message):
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('login')  
        # show error message
        else:
            return render(request, 'signup.html', {'error': error_message})    

    def validationCustomer(self, customer):
            error_message = None
            if customer.first_name:
                if len(customer.first_name) > 50:
                    error_message = 'First name must be in  50 charater!'
            elif customer.last_name:
                if len(customer.last_name) > 50:
                    error_message = 'Last name must be in  50 charater!'
            elif customer.email:
                if len(customer.email) > 250:
                    error_message = 'Email must be in  250 charater!'
            elif customer.password:
                if len(customer.password) < 6:
                    error_message = 'Password must be minimum 6 character!'

            # verify email address
            customer_email = Customer.objects.filter(email = customer.email)
            if customer_email:
                error_message = 'Email address already registered!'
            
            return error_message


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        pass_word = request.POST.get('password')
        customer_ = Customer.objects.get(email = email)
        error_message = None
        if customer_:
            flag = check_password(pass_word, customer_.password)
            if flag:
                request.session['customer_id'] = customer_.id
                return redirect('homepage')
            else:
                error_message = 'Password invalid !!'
        else:
            error_message = 'Email Invalid !!'
        return render(request, 'login.html', {'error' : error_message})

def logout(request):
    request.session.clear()
    return redirect('login')

class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        return render(request, 'cart.html', {'products':products})
