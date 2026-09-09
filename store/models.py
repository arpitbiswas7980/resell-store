from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField(help_text="Selling price in INR (e.g. 499)")
    original_price = models.IntegerField(default=999, help_text="Cut price (e.g. 999)")
    sizes = models.CharField(max_length=50, default="6, 7, 8, 9, 10")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def primary_image(self):
        first_img = self.images.first()
        return first_img.image.url if first_img else ''

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return f"{self.product.title} Image"

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    selected_size = models.CharField(max_length=10)
    customer_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    pincode = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.product.title}"