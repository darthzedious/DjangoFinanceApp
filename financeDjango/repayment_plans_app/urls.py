from django.urls import path

from financeDjango.repayment_plans_app import views

urlpatterns = [
    path('equal-installment-calculation/', views.EqualInstallmentPlanCalculateView.as_view(), name='equal-installment-calculation'),
    path('equal-installment-save/', views.EqualInstallmentPlanSaveView.as_view(), name='equal-installment-save'),
    path('equal-installment-plans-list/', views.EqualInstallmentPlanListView.as_view(), name='equal-installment-plans-list'),
    path('equal-pp-calculation/', views.EqualPPPlanCalculateView.as_view(),
         name='equal-pp-calculation'),
    path('equal-pp-save/', views.EqualPPPlanSaveView.as_view(), name='equal-pp-save'),
    path('equal-pp-plans-list/', views.EqualPPPlanListView.as_view(),
         name='equal-pp-plans-list'),
    path('equal-installment-changeable-ip-calculation/', views.EqualInstallmentChangeableIpCalculateView.as_view(),
         name='equal-installment-changeable-ip-calculation'),
    path('equal-installment-changeable-ip-save/', views.EqualInstallmentChangeableIpSaveView.as_view(),
         name='equal-installment-changeable-ip-save'),
    path('equal-installment-changeable-ip-list/', views.EqualInstallmentChangeableIpListView.as_view(),
         name='equal-installment-changeable-ip-list'),
]