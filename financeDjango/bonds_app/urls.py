from django.urls import path

from financeDjango.bonds_app import views

urlpatterns = [
    path('zero-coupon-bond-yield-to-maturity/', views.CalculateZeroCouponBondYieldToMaturity.as_view(),
         name='zero-coupon-bond-yield-to-maturity'),
    path('coupon-bond-yield-to-maturity/',views.CalculateCouponBondYieldToMaturity.as_view(),
         name='coupon-bond-yield-to-maturity'),
    path('coupon-bond-price/', views.CalculateCouponBondPrice.as_view(),
         name='coupon-bond-price'),
    path('zero-coupon-bond-price/', views.CalculateZeroCouponBondPrice.as_view(),
         name='zero-coupon-bond-price'),
]