from django.urls import path


from financeDjango.shares_app import stocks_view

urlpatterns = [
    path('preference-shares/', stocks_view.PreferenceSharesPrice.as_view(), name='preference_shares'),
    path('ordinary-shares/', stocks_view.OrdinarySharesPrice.as_view(), name='ordinary_shares'),
    path('return-on-equity/', stocks_view.ReturnOnEquity.as_view(), name='return_on_equity'),
    path('growth-rate/', stocks_view.GrowthRateOfDividends.as_view(), name='growth_rate'),
    path('calculate_capm/', stocks_view.CalculateCAPM.as_view(), name='calculate_capm'),

]