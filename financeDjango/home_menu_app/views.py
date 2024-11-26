from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home_menu/home.html'

def stock_operations_menu(request):
    return render(request, 'home_menu/nav/stock_shares_operation_menu.html')

def future_value_menu(request):
    return render(request, 'home_menu/nav/future_value_nav.html')

def discount_factor_menu(request):
    return render(request, 'home_menu/nav/discount_factor_nav.html')

def repayment_plans_menu(request):
    return render(request, 'home_menu/nav/repayment_plans_nav.html')
