from django.contrib import admin

# Register your models here.
from .models import Menu, Sub_menu, Video_slider, Product, Sub_product, About, Service

admin.site.register(Menu)
admin.site.register(Sub_menu)
admin.site.register(Video_slider)
admin.site.register(Product)
admin.site.register(Sub_product)
admin.site.register(About)
admin.site.register(Service)

