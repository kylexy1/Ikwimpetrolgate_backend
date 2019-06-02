from django.db import models

class Data(models.Model):
    header_total = models.CharField(max_length=30)
    header_revenue = models.CharField(max_length=30)
    header_growth = models.CharField(max_length=30)
    right_bon = models.CharField(max_length=30)
    right_cards = models.CharField(max_length=30)
    right_discounts = models.CharField(max_length=30)
    right_stock = models.CharField(max_length=30)
    right_cards_sold = models.CharField(max_length=30)
    right_bon_sold = models.CharField(max_length=30)
    right_cards_in_stock = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)


class Info(models.Model):
    name = models.CharField(max_length=30)
    tin_number = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    sector = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ('created',)
   