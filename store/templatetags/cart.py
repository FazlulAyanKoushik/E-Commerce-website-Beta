from django import template

register = template.Library()

@register.filter(name = 'is_in_cart')
def is_in_cart(product , cart):
    keys  = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    return False

@register.filter(name = 'cart_count')
def cart_count(product , cart):
    keys  = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return 0

@register.filter(name  = 'product_total_price')  
def product_total_price(product, cart):
    return product.price * cart_count(product, cart)

@register.filter(name = 'cart_total_price')
def cart_total_price(products, cart):
    sum = 0 
    for p in products:
        sum += product_total_price(p, cart)
        
    return sum