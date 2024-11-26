from django.urls import path

from financeDjango.repayment_plans_app import views

urlpatterns = [
    path('equal-installment-calculation/', views.EqualInstallmentPlanCalculateView.as_view(), name='equal-installment-calculation'),
    path('equal-installment-save/', views.EqualInstallmentPlanSaveView.as_view(), name='equal-installment-save'),
    path('Repayment-plans-list/', views.RepaymentPlansListView.as_view(), name='repayment-plans-list'),
]