import os
import numpy as np
from django.shortcuts import render
import requests

from django.urls import reverse_lazy
from django.views.generic import FormView

from financeDjango.mixins import OperationNameContextMixin
from financeDjango.shares_app.forms import PreferencesSharesForm, OrdinarySharesForm, ReturnOnEquityForm, \
    GrowthRateOfDividendsForm, CAPMForm
from financeDjango.shares_app import helpers


# def calculate_preferences_shares_price(request):
#     result = None
#
#     if request.method == 'POST':
#         form = PreferencesSharesForm(request.POST)
#         if form.is_valid():
#             dividends = form.cleaned_data['dividends']
#             rate_of_return = form.cleaned_data['rate_of_return']
#
#             try:
#                 result = dividends / rate_of_return
#             except (ValueError, ZeroDivisionError):
#                 result = "Invalid input. Please enter a valid number."
#     else:
#         form = PreferencesSharesForm()
#
#     context = {
#         'operation_name': 'Preference Shares Price',
#         'form': form,
#         'result': result,
#     }
#
#
#     return render(request, 'shares_templates/calculations.html', context)

class PreferenceSharesPrice(OperationNameContextMixin, FormView):
    template_name = 'shares_templates/calculations.html'
    form_class = PreferencesSharesForm
    # success_url = reverse_lazy('preference_shares')
    operation_name = 'Preference Shares Price'

    def form_valid(self, form):
        dividends = form.cleaned_data['dividends']
        rate_of_return = form.cleaned_data['rate_of_return']
        result = helpers.calculate_preference_shares_price(dividends, rate_of_return)

        context = self.get_context_data(result=result, form=form)
        return self.render_to_response(context)

class OrdinarySharesPrice(OperationNameContextMixin, FormView):
    template_name = 'shares_templates/calculations.html'
    form_class = OrdinarySharesForm
    operation_name = 'Ordinary Shares Price'

    def form_valid(self, form):
        dividend = form.cleaned_data['dividends']
        rate_of_return = form.cleaned_data['rate_of_return']
        growth_rate = form.cleaned_data['growth_rate']
        result = helpers.calculate_ordinary_shares_price(dividend, rate_of_return, growth_rate)

        context = self.get_context_data(result=result, form=form)
        return self.render_to_response(context)


# def calculate_return_on_equity(request):
#     result = None
#
#     if request.method =="POST":
#         form = ReturnOnEquityForm(request.POST)
#         if form.is_valid():
#             net_profit = form.cleaned_data['net_profit']
#             equity_capital = form.cleaned_data['equity_capital']
#
#             try:
#                 result =round(net_profit / equity_capital, 4)
#             except (ValueError, TypeError):
#                 result = "Invalid input. Please enter a valid number."
#     else:
#         form = ReturnOnEquityForm()
#
#     context = {
#         'operation_name': 'Calculate Return on Equity',
#         'form': form,
#         'result': result,
#     }
#
#     return render(request, 'shares_templates/calculations.html', context)

class ReturnOnEquity(OperationNameContextMixin, FormView):
    template_name = 'shares_templates/calculations.html'
    form_class = ReturnOnEquityForm
    operation_name = 'Return On Equity'

    def form_valid(self, form):
        net_profit = form.cleaned_data['net_profit']
        equity_capital = form.cleaned_data['equity_capital']
        result = helpers.calculate_return_on_equity(net_profit, equity_capital)

        context = self.get_context_data(result=result, form=form)
        return self.render_to_response(context)


class GrowthRateOfDividends(OperationNameContextMixin, FormView):
    """Retention Ratio (ki): The proportion of earnings a company retains for reinvestment,
     calculated as the percentage of net profit that is not distributed as dividends.
    The complement, 1 − ki, represents the Payout Ratio,
     or the portion of net income paid to shareholders as dividends."""

    template_name = 'shares_templates/calculations.html'
    form_class = GrowthRateOfDividendsForm
    operation_name = 'Growth Rate of Dividends'

    def form_valid(self, form):
        net_profit = form.cleaned_data['net_profit']
        equity_capital = form.cleaned_data['equity_capital']
        ki = form.cleaned_data['retention_ratio']
        result = helpers.calculate_growth_rate_of_dividends(net_profit, equity_capital, ki)

        context = self.get_context_data(result=result, form=form)
        return self.render_to_response(context)

def get_fundamental_stock_data(request):
    symbol = request.GET.get('symbol')
    stock_data = None
    error_message = None

    # Check if the symbol parameter is provided
    if symbol:
        api_key = os.getenv('ALPHA_VANTAGE_API_KEY')

        if not api_key:
            error_message = 'API key is missing. Please set the API key.'
        else:
            url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&apikey={api_key}'

            try:
                response = requests.get(url)
                data = response.json() # => If the API response is valid, data will be a dictionary that can be further processed.

                # Check if the response contains data
                if data and 'Symbol' in data:
                    stock_data = data
                else:
                    error_message = 'Error retrieving data. Please check the symbol or API key.'

            except requests.RequestException as e:
                error_message = f'Error retrieving data: {str(e)}'

    context = {
        'symbol': symbol,
        'stock_data': stock_data,
        'error_message': error_message,
    }

    return render(request, 'shares_templates/fundamental_stock_data.html', context)


def get_live_stock_price(request):
    """
    Django view to get the live stock price for an individual symbol.
    """
    symbol = request.GET.get('symbol', None)
    stock_price = None
    error_message = None

    if symbol:
        stock_price = helpers.fetch_stock_price(symbol)
        if stock_price is None:
            error_message = f"Error retrieving price for symbol {symbol}."

    context = {
        'symbol': symbol,
        'stock_price': stock_price,
        'error_message': error_message
    }

    return render(request, 'shares_templates/live_stock_price.html', context=context)


def get_top_10_stock_prices(request):
    """
    Django view to get live prices for the top 10 stocks.
    """
    top_10_symbols = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'BRK.B', 'NVDA', 'META', 'JPM', 'JNJ']
    stock_prices = {}
    error_message = None

    for symbol in top_10_symbols:
        price = helpers.fetch_stock_price(symbol)
        if price is not None:
            stock_prices[symbol] = price
        else:
            error_message = f"Error retrieving data for {symbol}."

    context = {
        'stock_prices': stock_prices,
        'error_message': error_message
    }

    return render(request, 'shares_templates/top_10_shares.html', context)

def calculate_beta_coefficient(request):
    symbol = request.GET.get('symbol')
    beta = None
    error_message = None

    if symbol:
        stock_data, market_data = helpers.fetch_historical_data(symbol)

        try:
            # Extract closing prices and calculate returns
            stock_prices = []
            market_prices = []

            # Assume we have monthly adjusted closing prices
            if "Monthly Adjusted Time Series" in stock_data and "Monthly Adjusted Time Series" in market_data:
                stock_series = stock_data["Monthly Adjusted Time Series"]
                market_series = market_data["Monthly Adjusted Time Series"]

                for date in stock_series:
                    if date in market_series:
                        stock_prices.append(float(stock_series[date]["5. adjusted close"]))
                        market_prices.append(float(market_series[date]["5. adjusted close"]))

                # Convert to returns
                stock_returns = np.diff(stock_prices) / stock_prices[:-1]
                market_returns = np.diff(market_prices) / market_prices[:-1]

                # Calculate beta
                beta = np.cov(stock_returns, market_returns)[0][1] / np.var(market_returns)

            else:
                error_message = "Error retrieving data. Please check the symbol or API key."

        except Exception as e:
            error_message = f"An error occurred: {str(e)}"

    context = {
        'symbol': symbol,
        'beta': beta,
        'error_message': error_message
    }

    return render(request, 'shares_templates/calculate_beta.html', context)

class CalculateCAPM(OperationNameContextMixin, FormView):
    form_class = CAPMForm
    template_name = 'shares_templates/calculations.html'
    operation_name = 'Capital Asset Pricing Model (CAPM)'

    def form_valid(self, form):
        risk_free_rate = form.cleaned_data['risk_free_rate']
        market_return = form.cleaned_data['market_return']
        beta_coefficient = form.cleaned_data['beta_coefficient']
        result = helpers.calculate_cpam(risk_free_rate, market_return, beta_coefficient)

        context = self.get_context_data(result=result, form=form)
        return self.render_to_response(context)
