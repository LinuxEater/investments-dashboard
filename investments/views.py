from django.shortcuts import render
from django.db.models import Sum
from .models import Investment, Expenses
from django.db.models.functions import TruncMonth
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
    
@login_required
def expenses_view(request):
    expenses = Expenses.objects.all()
    total = sum(float(exp.amount) for exp in expenses)

    # Agrupar por 'name' para gráfico de pizza (gastos por produto)
    by_name = expenses.values('name').annotate(total=Sum('amount'))

    # Agrupar por mês para gráfico de linha
    by_month = expenses.annotate(month=TruncMonth('date'))\
                       .values('month')\
                       .annotate(total=Sum('amount'))\
                       .order_by('month')

    context = {
        'expenses': expenses,
        'total': total,
        'chart_data': {
            'labels': [item['name'] for item in by_name],       # agrupando por produto
            'values': [float(item['total']) for item in by_name],
            'line_labels': [
                item['month'].strftime('%b/%y') if item['month'] else ''
                for item in by_month
            ],
            'line_values': [float(item['total']) for item in by_month],
        }
    }

    return render(request, 'expenses.html', context)