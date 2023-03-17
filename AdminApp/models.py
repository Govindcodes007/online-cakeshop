from django.db import models

# Create your models here.

class Category(models.Model):
    cate_name = models.CharField(max_length=20)

    def __str__(self):
        return self.cate_name
    
    class Meta:
        db_table = 'Category'
        
class Cake(models.Model):
    cake_name =models.CharField(max_length=50)
    price = models.FloatField(default=350)
    description = models.CharField(max_length=100)
    imageurl = models.ImageField(upload_to ='Images',default='abc.jpg')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    
    class Meta:
        
        db_table = 'Cake'
    
    
