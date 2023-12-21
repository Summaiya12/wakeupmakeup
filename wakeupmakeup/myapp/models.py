from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CHOICES_CATEGORY = (
    ('1', 'brush'),
    ('2', 'lipstick'),
    ('3', 'powder'),
    ('4', 'foundation'),
    ('5', 'tint'),
    ('6', 'shadow'),
    ('7', 'liner'),
    ('8', 'blush'),
    ('9', 'mascara'),
    ('10', 'perfume'),
    ('11', 'nail'),
    ('12', 'hair'),

)


class Product(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(max_length=300, default='')
    image = models.ImageField(upload_to='shop/image')
    price = models.IntegerField(default='')
    quantity = models.IntegerField(default='')
    category = models.CharField(choices=CHOICES_CATEGORY, max_length=2)

    def __str__(self):
        return self.name


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, default=False)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=120)

    def __str__(self):
        return self.user.username


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    email = models.EmailField(default=False)

    def __str__(self):
        return self.user.username


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)


class Order(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # cart_items = models.TextField(default='')
    # total_price = models.DecimalField(max_digits=10, decimal_places=2, default='')
    address = models.CharField(max_length=200, default='')
    name = models.CharField(max_length=50, default='')
    creates = models.DateTimeField(auto_now=True)


class Contacts(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.email}"
