from django.shortcuts import render, loader, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import AllFiles, UserProfile, CatAccessories, CatClothing, CatFurniture, CatFood, CatToys, CartItem
from decimal import Decimal

def sign_up(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        province = request.POST['province']
        city = request.POST['city']
        barangay = request.POST['barangay']
        street = request.POST['street']
        number = request.POST['number']

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('sign_up')

        # Create User and UserProfile
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        
        # Create the full address string
        full_address = f"{street}, {barangay}, {city}, {province}"
        
        UserProfile.objects.create(
            user=user,
            province=province,
            city=city,
            barangay=barangay,
            street=street,
            address=full_address,
            number=number
        )

        messages.success(request, 'Account created successfully! You can now log in.')
        return redirect('sign_in')
    return render(request, 'sign_up.html')

def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log the user in and redirect to the home page
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('home-page')  
        else:
            # Authentication failed
            messages.error(request, 'Invalid username or password')
            return redirect('sign_in')  

    return render(request, 'sign_in.html')

def logout_view(request):
    logout(request)
    return redirect('sign_in')

def master(request):
    template = loader.get_template('master.html')
    return HttpResponse(template.render())
    
def home_page(request):
    return render(request, 'home-page.html')

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Here you can add code to handle the form submission
        # For example, sending an email or saving to database
        
        messages.success(request, 'Thank you for your message! We will get back to you soon.')
        return redirect('contacts')
    
    return render(request, 'contacts.html')

@login_required
def cart(request):
    cart_items = CartItem.objects.filter(user=request.user).order_by('-date_added')
    total = sum(item.total_price() for item in cart_items)
    
    context = {
        'cart_items': cart_items,
        'total': total
    }
    return render(request, 'cart.html', context)

@login_required
def add_to_cart(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        file_name = request.POST.get('file_name')
        price = request.POST.get('price')
        quantity = int(request.POST.get('quantity', 1))
        
        # Check if item already exists in cart
        cart_item = CartItem.objects.filter(user=request.user, item_name=item_name).first()
        
        if cart_item:
            # Update quantity if item exists
            cart_item.quantity += quantity
            cart_item.save()
        else:
            # Create new cart item
            CartItem.objects.create(
                user=request.user,
                item_name=item_name,
                file_name=file_name,
                price=price,
                quantity=quantity
            )
        
        messages.success(request, 'Item added to cart successfully!')
        return JsonResponse({'status': 'success'})
    
    return JsonResponse({'status': 'error'})

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    cart_item.delete()
    messages.success(request, 'Item removed from cart successfully!')
    return redirect('cart')

@login_required
def update_cart_quantity(request, item_id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
        cart_item.quantity = quantity
        cart_item.save()
        return JsonResponse({
            'status': 'success',
            'total': str(cart_item.total_price())
        })
    return JsonResponse({'status': 'error'})

def about(request):
    return render(request, 'about.html')

def accessories(request):
    all = CatAccessories.objects.all().values()
    context = {
        'all': all
    }

    return render(request, 'homepage/accessories.html', context)

def clothing(request):
    all = CatClothing.objects.all().values()
    context = {
        'all': all
    }
    return render(request, 'homepage/clothing.html', context)

def furniture(request):
    all = CatFurniture.objects.all().values()
    context = {
        'all': all
    }
    return render(request, 'homepage/furniture.html', context)

def food(request):
    all = CatFood.objects.all().values()
    context = {
        'all': all
    }
    return render(request, 'homepage/food.html', context)

def toys(request):
    all = CatToys.objects.all().values()
    context = {
        'all': all
    }
    return render(request, 'homepage/toys.html', context)

def promo(request):
    return render(request, 'homepage/promo.html')

def free_shipping(request):
    return render(request, 'homepage/freeshipping.html')

def discounts(request):
    return render(request, 'homepage/discounts.html')

def cat_tree(request):
    current_item_name = request.GET.get('name')
    current_image = request.GET.get('image', '')
    
    # Get category prefix and model from image name
    category_prefix = ''
    category_model = None
    if current_image.startswith('furni'):
        category_prefix = 'furni'
        category_model = CatFurniture
    elif current_image.startswith('toy'):
        category_prefix = 'toy'
        category_model = CatToys
    elif current_image.startswith('food'):
        category_prefix = 'food'
        category_model = CatFood
    elif current_image.startswith('cloth'):
        category_prefix = 'cloth'
        category_model = CatClothing
    elif current_image.startswith('acc'):
        category_prefix = 'acc'
        category_model = CatAccessories
    
    # Get all items from the same category except the current item
    if category_model:
        similar_items = category_model.objects.exclude(
            item_name=current_item_name
        ).order_by('?')[:4]  # Random order, limit to 4 items
    else:
        similar_items = []
    
    context = {
        'similar_items': similar_items,
        'name': current_item_name,
        'price': request.GET.get('price'),
        'image': current_image
    }
    return render(request, 'homepage/cat_tree.html', context)

@login_required
def checkout(request):
    # Get selected item IDs from the query parameters
    selected_ids = request.GET.get('selected_ids', '')
    selected_ids = selected_ids.split(',') if selected_ids else []

    # Fetch selected cart items
    selected_items = CartItem.objects.filter(id__in=selected_ids, user=request.user)

    # Calculate total price for the selected items (subtotal)
    subtotal = sum(Decimal(item.total_price()) for item in selected_items)

    # Initialize savings to 0
    savings = Decimal('0.00')

    # Check if promo code is provided and valid
    promo_code = request.GET.get('promo_code', '').strip().upper()
    if promo_code == 'DESIGN10':
        # Apply 10% discount
        savings = subtotal * Decimal('0.10')

    # Define shipping cost (default to ₱50.00, as a Decimal)
    shipping = Decimal('50.00')

    # Calculate total (Subtotal - Savings + Shipping)
    total = subtotal - savings + shipping

    # Calculate the total quantity of items
    total_quantity = sum(item.quantity for item in selected_items)

    # Pass the necessary context to the template
    context = {
        'selected_items': selected_items,
        'subtotal': subtotal,
        'savings': savings,
        'shipping': shipping,
        'total': total,
        'total_quantity': total_quantity,  # Add total_quantity to the context
    }

    return render(request, 'checkout.html', context)
