from django.urls import path


from financeDjango.shares_app import stocks_view

urlpatterns = [
    path('preference-shares/', stocks_view.PreferenceSharesPrice.as_view(), name='preference_shares'),
    path('ordinary-shares/', stocks_view.OrdinarySharesPrice.as_view(), name='ordinary_shares'),
    path('return-on-equity/', stocks_view.ReturnOnEquity.as_view(), name='return_on_equity'),
    path('growth-rate/', stocks_view.GrowthRateOfDividends.as_view(), name='growth_rate'),
    path('stock-data/', stocks_view.get_fundamental_stock_data, name='stock_data'),
    path('live-stock-price/', stocks_view.get_live_stock_price, name='stock_price'),
    path('top-10-stocks/', stocks_view.get_top_10_stock_prices, name='top_10_stocks'),
    path('calculate-beta', stocks_view.calculate_beta_coefficient, name='calculate_beta'),
    path('calculate_capm/', stocks_view.CalculateCAPM.as_view(), name='calculate_capm'),

]