from django.contrib import admin

# Register your models here.
from .models import Menu, Sub_menu, Sub_of_sub_menu, Video_slider, Image_slider, Product, Sub_product, About

admin.site.register(Menu)
admin.site.register(Sub_menu)
admin.site.register(Sub_of_sub_menu)
admin.site.register(Video_slider)
admin.site.register(Image_slider)
admin.site.register(Product)
admin.site.register(Sub_product)
admin.site.register(About)

