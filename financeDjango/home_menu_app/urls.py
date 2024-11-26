from django.urls import path

from financeDjango.home_menu_app import views

urlpatterns = [
    path('',views.HomeView.as_view() , name='home'),
    path('shares-opeartions/', views.stock_operations_menu, name='stock_operations_menu'),
    path('future-value/', views.future_value_menu, name='future-value-menu'),
    path('discount-factor/', views.discount_factor_menu, name='discount-factor-menu'),
    path('repayment_plans/', views.repayment_plans_menu, name='repayment_plans_menu'),

]