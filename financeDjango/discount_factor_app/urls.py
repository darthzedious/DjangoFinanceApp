from django.urls import path
from financeDjango.discount_factor_app import views

urlpatterns = [
    path('calculate-df/', views.CalculateDiscountFactor.as_view(), name='calculate-discount-factor'),
    path('discounting-pv/', views.DiscountingPresentValue.as_view(), name='discounting-present-value'),
]