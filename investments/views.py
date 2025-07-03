from django.shortcuts import render
from .models import Investment

# Create your views here.

def dashboard_view(request):
    investments = Investment.objects.all()
    total = sum([inv.amount_invested for inv in investments])
    return render(request, 'dashboard.html', {
        'investments': investments,
        'total': total
    })