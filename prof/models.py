from django.db import models

# Create your models here.
class CreateAccount(models.Model):
    username = models.CharField(default="",max_length=100,blank=True,null=True)
    email = models.EmailField(default="",max_length=100,blank=True,null=True)
    M_no = models.CharField(default="",max_length=12,blank=True,null=True)
    reg_date = models.DateField(auto_now=True,blank=True,null=True)
    img = models.ImageField(upload_to="SellerImage",default="",max_length=300,blank=True, null=True)
    password = models.CharField(default="",max_length=100,blank=True,null=True)

    def __str__(self):
        return self.username