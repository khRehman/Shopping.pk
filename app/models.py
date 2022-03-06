from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
STATE_CHOICES = (
  ('Islamabad','Islamabad'),
  ('Rawalpindi','Rawalpindi'),
  ('Karachi','Karachi'),
  ('Faisalabad','Faisalabad'),
  ('Bahawalpur','Bahawalpur'),
  ('Chishtian','Chishtian'),
  ('Lodhran','Lodhran'),
  ('Haiderabad','Haiderabad'),
  ('Dadu','Dadu'),
  ('Queta','Queta'),
  ('Hasilpur','Hasilpur'),
  ('Multan','Multan'),
  ('Azad Kashmir','Azad Kashmir'),
  ('Khairpur','Khairpur'),
  ('Sialkot','Sialkot'),
  ('Gujranwala','Gujranwala'),
  ('Lahore','Lahore'),
  ('Minchanabad','Minchanabad'),
  ('Haveli lakha','Haveli lakha'),
  ('Mardan','Mardan'),
  ('Lodhran','Lodhran'),
  ('Vihari','Vihari'),
  ('Burewala','Burewala'),
  ('Arifwala','Arifwala'),
  ('Okara','Okara'),
  ('MuzafaGarh','MuzafaGarh'),
  ('Khanpur Maral','Khanpur Maral'),
  ('Qaimpur','Qaimpur'),
  ('Dera Nawab','Dera Nawab'),
  ('Sadaqabad','Sadaqabad'),
  ('Sehwin','Sehwin'),
  ('Tobatek singh','Tobatek singh'),
  ('Kamalia','Kamalia'),
  ('Rohri','Rohri'),
  ('Peshawar','Peshawar'),
  ('Dahranwala','Dahranwala'),
)
class Customer(models.Model):
 user = models.ForeignKey(User, on_delete=models.CASCADE)
 name = models.CharField(max_length=200)
 locality = models.CharField(max_length=200)
 city = models.CharField(max_length=50)
 zipcode = models.IntegerField()
 state = models.CharField(choices=STATE_CHOICES, max_length=50)

 def __str__(self):
  # return self.user.username
  return str(self.id)


CATEGORY_CHOICES = (
 ('M', 'Mobile'),
 ('L', 'Laptop'),
 ('TW', 'Top Wear'),
 ('BW', 'Bottom Wear'),
)
class Product(models.Model):
 title = models.CharField(max_length=100)
 selling_price = models.FloatField()
 discounted_price = models.FloatField()
 description = models.TextField()
 brand = models.CharField(max_length=100)
 category = models.CharField( choices=CATEGORY_CHOICES, max_length=2)
 product_image = models.ImageField(upload_to='productimg')

 def __str__(self):
  return str(self.id)


class Cart(models.Model):
 user = models.ForeignKey(User, on_delete=models.CASCADE)
 product = models.ForeignKey(Product, on_delete=models.CASCADE)
 quantity = models.PositiveIntegerField(default=1)

 def __str__(self):
  return str(self.id)
  
  # Below Property will be used by checkout.html page to show total cost in order summary
 @property
 def total_cost(self):
   return self.quantity * self.product.discounted_price

STATUS_CHOICES = (
  ('Accepted','Accepted'),
  ('Packed','Packed'),
  ('On The Way','On The Way'),
  ('Delivered','Delivered'),
  ('Cancel','Cancel')
)

class OrderPlaced(models.Model):
 user = models.ForeignKey(User, on_delete=models.CASCADE)
 customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
 product = models.ForeignKey(Product, on_delete=models.CASCADE)
 quantity = models.PositiveIntegerField(default=1)
 ordered_date = models.DateTimeField(auto_now_add=True)
 status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='Pending')

  # Below Property will be used by orders.html page to show total cost
 @property
 def total_cost(self):
   return self.quantity * self.product.discounted_price