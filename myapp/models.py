from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    cpassword = models.CharField(max_length=100)

    class Meta:
       db_table= "login_form"

class Addproduct(models.Model):
    productname = models.CharField(max_length=200)
    productdescription = models.CharField(max_length=200)
    productcategory = models.CharField(max_length=200)
    offerprice = models.CharField(max_length=200)
    actualprice = models.CharField(max_length=200)
    stock = models.CharField(max_length=100)
    productimage = models.ImageField(upload_to="productimages")   
    

    class Meta:
        db_table = "Addproduct"   

class Bag(models.Model):
    ProductId = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    product_price = models.CharField(max_length=100)
    quantity = models.CharField(max_length=50)
    total_price = models.CharField(max_length=50)
    username = models.CharField(max_length=100)

    class Meta:
        db_table = "bag"

class Order(models.Model):
    firstname = models.CharField(max_length=100)    
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=10)
    address = models.CharField(max_length=300)
    total_product = models.CharField(max_length=400)
    total_price = models.CharField(max_length=60)
    payment = models.CharField(max_length=100)
    card_number = models.CharField(max_length=50)
    cvv = models.CharField(max_length=10)
    expiry_date = models.CharField(max_length=10)
    status = models.CharField(max_length=100)
    
    class Meta:
        db_table = "order"

class Contact(models.Model):
    username = models.CharField(max_length=100)
    email= models.EmailField(max_length=200)   
    message = models.CharField(max_length=600) 

    class Meta:
        db_table = "contact"    