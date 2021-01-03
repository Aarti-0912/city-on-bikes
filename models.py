from django.db import models

# Create your models here.
class customer(models.Model):
    cust_name=models.CharField(max_length=30,default="")
    pickdate=models.DateField(max_length=10,default="")
    picktime=models.TimeField()
    dropdate=models.DateField(max_length=10,default="")
    droptime=models.TimeField()
    vehname=models.CharField(max_length=30,default="")
    class Meta:
        db_table="customer"
class Order(models.Model):
    first_name = models.CharField(max_length=30,default="")
    last_name = models.CharField(max_length=30,default="")
    email = models.EmailField(max_length=200,default="")
    # city = models.CharField(max_length=30)
    # age = models.IntegerField()

class product(models.Model):
    pro_name = models.CharField(max_length=30,default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=3000,default="")
    available = models.CharField(max_length=20,default="")
    image = models.ImageField(upload_to="static/images",default="")
    class Meta:
        db_table="product"
    def __str__(self):
        return self.pro_name

class deepak(models.Model):
    use_name=models.CharField(max_length=30,default="")
    use_password=models.CharField(max_length=50)
    class Meta:
        db_table="deepak"

class signdata(models.Model):
    sign_username=models.CharField(max_length=30, default="")
    sign_email=models.EmailField(max_length=30)
    sign_password=models.CharField(max_length=30)
    sign_passwordconf=models.CharField(max_length=30)
    class Meta:
        db_table="signdata"
