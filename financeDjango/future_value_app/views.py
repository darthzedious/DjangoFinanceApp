from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView

from financeDjango.future_value_app.forms import FutureValueBaseForm
from financeDjango.future_value_app.helpers import future_value_simple_interest, future_value_compound_interest
from financeDjango.mixins import OperationNameContextMixin


class FutureValueSimpleInterest(LoginRequiredMixin, OperationNameContextMixin, FormView):
    template_name = 'shares_templates/calculations.html'
    form_class = FutureValueBaseForm
    operation_name = 'Future Value with simple interest'

    def form_valid(self, form):
        present_value = form.cleaned_data['present_value']
        interest_rate = form.cleaned_data['interest_rate']
        number_of_periods = form.cleaned_data['number_of_periods']
        result = future_value_simple_interest(present_value, interest_rate, number_of_periods)

        context = self.get_context_data(result=result, form=form)
        return self.render_to_response(context)

class FutureValueCompoundInterest(LoginRequiredMixin, OperationNameContextMixin, FormView):
    template_name = 'shares_templates/calculations.html'
    form_class = FutureValueBaseForm
    operation_name = 'Future Value with compound interest'

    def form_valid(self, form):
        present_value = form.cleaned_data['present_value']
        interest_rate = form.cleaned_data['interest_rate']
        number_of_periods = form.cleaned_data['number_of_periods']
        result = future_value_compound_interest(present_value, interest_rate, number_of_periods)

        context = self.get_context_data(result=result, form=form)
        return self.render_to_response(context)
