from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    CYTIGORY=(
      (('stationry'),('stationry')),
      (('electronics'),('electronics')),
      (('food'),('food')),)

    name=models.CharField(max_length=100,null=True)
    catigory=models.CharField(max_length=20,choices=CYTIGORY,null=True)
    quantity=models.PositiveIntegerField(null=True)

    def __str__(self):
      return f'{self.name}-{self.quantity}'
    
    class Meta:
        verbose_name_plural = 'Product'
    

    
class Order (models.Model):
   product=models.ForeignKey(Product,on_delete=models.CASCADE) 
   staff=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
   order_quantity=models.PositiveBigIntegerField(null=True) #كم غرض بهاد الاوردر
   date=models.DateTimeField(auto_now_add=True)# يعني لما انعمل هالاوردر دغري حفظلي الوقت والتاريخ يلي انعمل فيه
    
   def __str__(self):
      return f'{self.product} orderd by ({self.staff.username})'
    







