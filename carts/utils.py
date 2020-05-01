from .models import Cart

def get_or_create_cart(request):
    user = request.user if request.user.is_authenticated else None #Asigna el carrito a un usuario si esta autenticado, caso contrario no.
    cart_id = request.session.get('cart_id')
    cart = Cart.objects.filter(cart_id = cart_id).first() #si esta vacio, o sea no existe carrito first es = None

    if cart is None:
        cart = Cart.objects.create(user=user)

    if user and cart.user is None: # si el usuario existe y el carrito no esta asignado a ese usuario, lo asigno
        cart.user = user
        cart.save()
    
    request.session['cart_id'] = cart.cart_id

    return cart