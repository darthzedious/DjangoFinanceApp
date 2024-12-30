from django.urls import path

from financeDjango.annuity_factor_app import views

urlpatterns = [
    path('fv-annuity-end-year-payment/', views.FvAnnuityFactorEndYearPaymentView.as_view(), name="fv-annuity-factor-end-year-payment"),
    path('pv-annuity-end-year-payment/', views.PvAnnuityFactorEndYearPaymentView.as_view(), name="pv-annuity-factor-end-year-payment"),
    path('fv-annuity-start-year-payment/', views.FvAnnuityFactorStartYearPaymentView.as_view(), name="fv-annuity-factor-start-year-payment"),
    path('pv-annuity-start-year-payment/', views.PvAnnuityFactorStartYearPaymentView.as_view(), name="pv-annuity-factor-start-year-payment"),
]