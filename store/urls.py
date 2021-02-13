from django.contrib import admin
from django.urls import path
from .views import Index, Signup, Login, logout, Cart

urlpatterns = [
    path('', Index.as_view(), name = 'homepage'),
    path('signup', Signup.as_view()),
    path('login', Login.as_view(), name = 'login'),
    path('logout', logout, name = 'logout'),
    path('cart', Cart.as_view(), name = 'cart'),
]