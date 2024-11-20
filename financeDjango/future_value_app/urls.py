from django.urls import path

from financeDjango.future_value_app import views

urlpatterns = [
    path('fv-simple-interest/', views.FutureValueSimpleInterest.as_view(), name='fv-simple-interest'),
    path('fv-compound-interest/', views.FutureValueCompoundInterest.as_view(), name='fv-compound-interest'),
]