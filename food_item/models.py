from django.db import models

# Create your models here.
class Item(models.Model):

    def __str__(self):
        return self.item_name  # itshow item value name when we see item in python shell wiithout it show only object 1,2
    
    item_name=models.CharField(max_length=200)
    item_desc=models.CharField(max_length=200)
    item_price=models.IntegerField()

