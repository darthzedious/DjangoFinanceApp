from django.urls import path, include

from financeDjango.repayment_plans_app import views

urlpatterns = [
    path('equal-installment-calculation/', views.EqualInstallmentPlanCalculateView.as_view(), name='equal-installment-calculation'),
    path('equal-installment-save/', views.EqualInstallmentPlanSaveView.as_view(), name='equal-installment-save'),
    path('equal-installment-plans-list/', views.EqualInstallmentPlanListView.as_view(), name='equal-installment-plans-list'),
    path('equal-installment/<int:pk>/', include([
        path('edit/', views.EqualInstallmentEditView.as_view(), name='edit-equal-installment'),
        path('delete/', views.EqualInstallmentDeleteView.as_view(), name='delete-equal-installment'),
    ])),
    path('equal-pp-calculation/', views.EqualPPPlanCalculateView.as_view(),
         name='equal-pp-calculation'),
    path('equal-pp-save/', views.EqualPPPlanSaveView.as_view(), name='equal-pp-save'),
    path('equal-pp-plans-list/', views.EqualPPPlanListView.as_view(),
         name='equal-pp-plans-list'),
    path('equal-pp/<int:pk>/', include([
        path('edit/', views.EqualPPPlanEditView.as_view(), name='edit-equal-pp'),
        path('delete/', views.EqualPPPlanDeleteView.as_view(), name='delete-equal-pp'),
    ])),
    path('equal-installment-changeable-ip-calculation/', views.EqualInstallmentChangeableIpCalculateView.as_view(),
         name='equal-installment-changeable-ip-calculation'),
    path('equal-installment-changeable-ip-save/', views.EqualInstallmentChangeableIpSaveView.as_view(),
         name='equal-installment-changeable-ip-save'),
    path('equal-installment-changeable-ip-list/', views.EqualInstallmentChangeableIpListView.as_view(),
         name='equal-installment-changeable-ip-list'),
    path('equal-installment-changeable-ip/<int:pk>/', include([
        path('edit/', views.EqualInstallmentChangeableIpEditView.as_view(), name='edit-equal-installment-changeable-ip'),
        path('delete/', views.EqualInstallmentChangeableIpDeleteView.as_view(), name='delete-equal-installment-changeable-ip'),
    ])),
]