from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import FormView

from financeDjango.discount_factor_app.forms import DiscountFactorForm, DiscountPresentValueForm
from financeDjango.discount_factor_app.helpers import calculate_the_discount_factor, discounting_present_value
from financeDjango.mixins import OperationNameContextMixin


class CalculateDiscountFactor(LoginRequiredMixin, OperationNameContextMixin, FormView):
    template_name = 'shares_templates/calculations.html'
    form_class = DiscountFactorForm
    operation_name = 'Calculate Discount Factor'

    def form_valid(self, form):
        interest_rate = form.cleaned_data['interest_rate']
        number_of_periods = form.cleaned_data['number_of_periods']
        result = calculate_the_discount_factor(interest_rate, number_of_periods)

        context = self.get_context_data(result=result, form=form)
        return self.render_to_response(context)

class DiscountingPresentValue(LoginRequiredMixin, OperationNameContextMixin, FormView):
    template_name = 'shares_templates/calculations.html'
    form_class = DiscountPresentValueForm
    operation_name = 'Calculate Discount Present Value'

    def form_valid(self, form):
        interest_rate = form.cleaned_data['interest_rate']
        number_of_periods = form.cleaned_data['number_of_periods']
        future_value = form.cleaned_data['future_value']
        result = discounting_present_value(future_value, interest_rate, number_of_periods)

        context = self.get_context_data(result=result, form=form)
        return self.render_to_response(context)