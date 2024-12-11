from django.views.generic import FormView

from financeDjango.mixins import OperationNameContextMixin
from financeDjango.shares_app.forms import PreferencesSharesForm, OrdinarySharesForm, ReturnOnEquityForm, \
    GrowthRateOfDividendsForm, CAPMForm
from financeDjango.shares_app import helpers

class PreferenceSharesPrice(OperationNameContextMixin, FormView):
    template_name = 'shares_templates/calculations.html'
    form_class = PreferencesSharesForm
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
