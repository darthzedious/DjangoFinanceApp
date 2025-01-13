from django.urls import path

from financeDjango.bonds_app import views

urlpatterns = [
    path('zero-coupon-bond-yield-to-maturity/', views.CalculateZeroCouponBondYieldToMaturity.as_view(),
         name='zero-coupon-bond-yield-to-maturity'),
]