from django.db import models
# Create your models here.
class Menu(models.Model):
    class Meta:
        verbose_name_plural = "menu"

    menu_id = models.CharField(primary_key=True,max_length=20)
    menu_title = models.CharField(max_length=200)
    show_in_menu = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add =True)
    updated_at = models.DateTimeField(auto_now =True)

    def __str__(self):
        return self.menu_title

class Sub_menu(models.Model):
    class Meta:
        verbose_name_plural = "sub_menu"

    sub_menu_id = models.CharField(primary_key=True,max_length=20)
    menu = models.ForeignKey(Menu, on_delete = models.CASCADE)
    sub_menu_title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add =True)
    updated_at = models.DateTimeField(auto_now =True)

    def __str__(self):
        return self.sub_menu_title
     

class Video_slider(models.Model):
    class Meta:
        verbose_name_plural = "video_slider"

    vslider_id = models.CharField(primary_key=True,max_length=20)
    vslider_title = models.CharField(max_length=200)
    vslider_description = models.CharField(max_length=200)
    vslider_video = models.FileField()
    created_at = models.DateTimeField(auto_now_add =True)
    updated_at = models.DateTimeField(auto_now =True)

    def __str__(self):
        return self.vslider_title 
       

class Product(models.Model):
    class Meta:
        verbose_name_plural = "product"

    product_id = models.CharField(primary_key=True,max_length=20)
    product_title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add =True)
    updated_at = models.DateTimeField(auto_now =True)

    def __str__(self):
        return self.product_title

class Sub_product(models.Model):
    class Meta:
        verbose_name_plural = "Sub_product"

    sub_product_id = models.CharField(primary_key=True,max_length=20)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    sub_product_title = models.CharField(max_length=200)
    sub_product_image = models.ImageField()
    sub_product_content = models.CharField(max_length=200)
    sub_product_description = models.TextField(max_length=7000)
    created_at = models.DateTimeField(auto_now_add =True)
    updated_at = models.DateTimeField(auto_now =True)

    def __str__(self):
        return self.sub_product_title

class About(models.Model):
    class Meta:
        verbose_name_plural = "about"

    about_id = models.CharField(primary_key=True,max_length=20)
    about_title = models.CharField(max_length=20)
    about_video = models.FileField()
    about_content = models.TextField(max_length=7000)
    mission_image = models.ImageField()
    mission_content = models.TextField(max_length=2000)
    value_image = models.ImageField()
    value_content = models.TextField(max_length=2000)
    vision_image = models.ImageField()
    vision_content = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add =True)
    updated_at = models.DateTimeField(auto_now =True)

    def __str__(self):
        return self.about_title                 

class Service(models.Model):
    class Meta:
        verbose_name_plural = "service"

    service_id = models.CharField(primary_key=True,max_length=20)
    service_title = models.CharField(max_length=20)
    service_content = models.CharField(max_length=7000)
    created_at = models.DateTimeField(auto_now_add =True)
    updated_at = models.DateTimeField(auto_now =True)

    def __str__(self):
        return self.service_title 

class Document(models.Model):
    class Meta:
        verbose_name_plural = "documents"

    name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, blank=True)
    subject = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='')
    message = models.TextField(max_length=2000, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now =True)

    def __str__(self):
        return self.name    

class Form(models.Model):
    class Meta:
        verbose_name_plural = "forms"

    name = models.CharField(max_length=255, blank=True)
    form = models.FileField()
    uploaded_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now =True)

    def __str__(self):
        return self.name          
