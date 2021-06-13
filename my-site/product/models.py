from django.db import models
from django.utils.translation import gettext as _

class Product(models.Model):
    title = models.CharField(_("title"), max_length=200)
    price = models.IntegerField(_("price"),)
    discount = models.FloatField(_("discount"))
    special_discount = models.FloatField(_("special_discount"))
    special_discount_time = models.DateTimeField(_("special_discount_time"), auto_now=True, auto_now_add=False)
    number = models.IntegerField(_("number"))
    description = models.TextField(_("description"))
    image = models.FileField(_("image"), blank=True)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')
    
class SlidBar(models.Model):
    title = models.CharField(_("title"), max_length=300)
    header = models.CharField(_("header"), max_length=300, blank=True)
    description = models.TextField(_("description"), blank=True)
    image = models.ImageField(_("image"), upload_to="slidbar/")
    product_id = models.IntegerField(_("product id"), blank=True, default=0)
    is_active = models.BooleanField(_("show on website"))
    

    class Meta:
        verbose_name = _("slider")
        verbose_name_plural = _("sliders")

    def __str__(self):
        return self.title

    
