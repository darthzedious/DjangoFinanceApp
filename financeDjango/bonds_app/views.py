from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView

from financeDjango.bonds_app.forms import ZeroCouponBondYieldToMaturityForm, CouponBondYieldToMaturityForm
from financeDjango.bonds_app.helpers import zero_coupon_bond_yield_to_maturity, calculate_coupon_bond_yield_to_maturity
from financeDjango.mixins import OperationNameContextMixin


# Create your views here.

class CalculateZeroCouponBondYieldToMaturity(LoginRequiredMixin, OperationNameContextMixin,FormView):
    template_name = 'shares_templates/calculations.html'
    form_class = ZeroCouponBondYieldToMaturityForm
    operation_name = 'Zero Coupon Bond Yield To Maturity'

    def form_valid(self, form):
        nominal = form.cleaned_data['nominal']
        present_value = form.cleaned_data['present_value']
        number_of_periods = form.cleaned_data['number_of_periods']

        result = zero_coupon_bond_yield_to_maturity(number_of_periods, nominal, present_value)

        context = self.get_context_data(result=result, form=form)

        return self.render_to_response(context)

class CalculateCouponBondYieldToMaturity(LoginRequiredMixin, OperationNameContextMixin, FormView):
    template_name = 'shares_templates/calculations.html'
    form_class = CouponBondYieldToMaturityForm
    operation_name = 'Coupon Bond Yield To Maturity'

    def form_valid(self, form):
        coupon_rate = form.cleaned_data['coupon_rate']
        nominal = form.cleaned_data['nominal']
        present_value = form.cleaned_data['present_value']
        number_of_periods = form.cleaned_data['number_of_periods']
        payment_period = form.cleaned_data['payment_period']

        result = calculate_coupon_bond_yield_to_maturity(coupon_rate, nominal, present_value, number_of_periods, payment_period)

        context = self.get_context_data(result=result, form=form)

        return self.render_to_response(context)