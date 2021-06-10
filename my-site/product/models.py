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
    