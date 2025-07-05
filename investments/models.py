from django.db import models

# Create your models here.

class Investment(models.Model):
    TYPE_CHOICES = [
        ('FIIs', 'Real Estate Fund'),
        ('CDB', 'CDB'),
        ('STOCK', 'Stock'),
        ('CRYPTO', 'Cryptocurrency'),
        ('OTHER', 'Other')
    ]

    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    name = models.CharField(max_length=50)
    amount_invested = models.DecimalField(max_digits=10, decimal_places=2)
    investment_date = models.DateField()
    yield_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.type}"
    
class Expenses(models.Model):
    TYPE_CHOICES = [
        ('MONTHLY', 'monthly'),
        ('ANNUAL', 'annual'),
        ('UNIQUE', 'unique'),
        ('BIWEEKLY', 'biweekly'),
        ('OTHER', 'Other')
    ]
    name = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.amount}"
