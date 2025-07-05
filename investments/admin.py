from django.contrib import admin
from .models import Investment, Expenses

# Register your models here.


@admin.register(Investment)
class InvestmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'amount_invested', 'investment_date', 'yield_rate')
    list_filter = ('type',)
    search_fields = ('name',)

@admin.register(Expenses)
class ExpensesAdmin(admin.ModelAdmin):
    list_display = ('name', 'type',)
    list_filter = ('type',)
    search_fields = ('name',)