from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Order

def home(request):
    products = Product.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    sizes = [s.strip() for s in product.sizes.split(',')]
    
    if request.method == 'POST':
        selected_size = request.POST.get('size')
        customer_name = request.POST.get('name')
        phone_number = request.POST.get('phone')
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')
        city = request.POST.get('city')

        Order.objects.create(
            product=product,
            selected_size=selected_size,
            customer_name=customer_name,
            phone_number=phone_number,
            address=address,
            pincode=pincode,
            city=city
        )
        return render(request, 'success.html', {'product': product, 'name': customer_name})

    return render(request, 'product_detail.html', {'product': product, 'sizes': sizes})