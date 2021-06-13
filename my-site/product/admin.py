from django.contrib import admin
from .models import Product, ProductImage, SlidBar

#https://soshace.com/upload-multiple-images-to-a-django-model-without-plugins/
class ProductImageAdmin(admin.StackedInline):
    model = ProductImage
 
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]
 
    class Meta:
       model = Product
 
@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass

class SlidBarAdmin(admin.ModelAdmin):
    pass

admin.site.register(SlidBar, SlidBarAdmin)