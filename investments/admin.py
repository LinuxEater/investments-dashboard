from django.contrib import admin
from .models import Investment

# Register your models here.


@admin.register(Investment)
class InvestmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'amount_invested', 'investment_date', 'yield_rate')
    list_filter = ('type',)
    search_fields = ('name',)