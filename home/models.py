from django.db import models
# Create your models here.

class Product(models.Model):
    image =models.ImageField(upload_to='images')
    name = models.TextField()
    title =models.TextField()
    category = models.CharField(max_length=200)
    date =models.DateField()
  
    def __str__(self):
      return self.category
class comment(models.Model):
     coment = models.TextField()
     name = models.CharField(max_length=20)
     mark = models.IntegerField()





class Mahsulot(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    discription = models.TextField()
    img = models.ImageField(upload_to="images")


    def __str__(self) -> str:
        return self.title
    