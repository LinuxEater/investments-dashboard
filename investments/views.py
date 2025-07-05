from django.shortcuts import render
from .models import Investment, Expenses
from collections import defaultdict
from django.contrib.auth.decorators import login_required


@login_required
def dashboard_view(request):
    investments = Investment.objects.all()
    total = sum([inv.amount_invested for inv in investments])

    # Aggregate by type
    data_by_type = defaultdict(float)
    for inv in investments:
        data_by_type[inv.get_type_display()] += float(inv.amount_invested)

    labels = list(data_by_type.keys())
    values = list(data_by_type.values())

    return render(request, 'dashboard.html', {
        'investments': investments,
        'total': total,
        'labels': labels,
        'values': values,
    })
    
def expenses_view(request):
    expenses = Expenses.objects.all()
    total = sum([exp.amount for exp in expenses])
    
    context = {
        'expenses': expenses,
        'total': total, 
    }
    
    return render(request, 'expenses.html', context)