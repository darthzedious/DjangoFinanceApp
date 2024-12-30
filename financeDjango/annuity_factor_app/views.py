from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import FormView

from financeDjango.annuity_factor_app.forms import AnnuityFactorForm
from financeDjango.annuity_factor_app.helpers import calculate_future_value_annuity_factor_end_year_payment, \
    calculate_future_value_annuity_factor_start_year_payment, calculate_present_value_annuity_factor_end_year_payment, \
    calculate_present_value_annuity_factor_start_year_payment
from financeDjango.mixins import OperationNameContextMixin


class FvAnnuityFactorEndYearPaymentView(LoginRequiredMixin, OperationNameContextMixin, FormView):
    template_name = 'shares_templates/calculations.html'
    operation_name = 'Future Value Annuity Factor End-Year Payment'
    form_class = AnnuityFactorForm

    def form_valid(self, form):
        interest_rate = form.cleaned_data['interest_rate']
        number_of_periods = form.cleaned_data['number_of_periods']

        result = calculate_future_value_annuity_factor_end_year_payment(interest_rate, number_of_periods)

        context = self.get_context_data(result=result, form=form)

        return self.render_to_response(context)

class FvAnnuityFactorStartYearPaymentView(LoginRequiredMixin, OperationNameContextMixin, FormView):
    template_name = 'shares_templates/calculations.html'
    operation_name = 'Future Value Factor Start-Year Payment'
    form_class = AnnuityFactorForm

    def form_valid(self, form):
        interest_rate = form.cleaned_data['interest_rate']
        number_of_periods = form.cleaned_data['number_of_periods']

        result = calculate_future_value_annuity_factor_start_year_payment(interest_rate, number_of_periods)

        context = self.get_context_data(result=result, form=form)

        return self.render_to_response(context)

class PvAnnuityFactorEndYearPaymentView(LoginRequiredMixin, OperationNameContextMixin, FormView):
    template_name = 'shares_templates/calculations.html'
    operation_name = 'Present Value Annuity Factor End-Year Payment'
    form_class = AnnuityFactorForm

    def form_valid(self, form):
        interest_rate = form.cleaned_data['interest_rate']
        number_of_periods = form.cleaned_data['number_of_periods']

        result = calculate_present_value_annuity_factor_end_year_payment(interest_rate, number_of_periods)

        context = self.get_context_data(result=result, form=form)

        return self.render_to_response(context)

class PvAnnuityFactorStartYearPaymentView(LoginRequiredMixin, OperationNameContextMixin, FormView):
    template_name = 'shares_templates/calculations.html'
    operation_name = 'Present Value Annuity Factor Start-Year Payment'
    form_class = AnnuityFactorForm

    def form_valid(self, form):
        interest_rate = form.cleaned_data['interest_rate']
        number_of_periods = form.cleaned_data['number_of_periods']

        result = calculate_present_value_annuity_factor_start_year_payment(interest_rate, number_of_periods)

        context = self.get_context_data(result=result, form=form)

        return self.render_to_response(context)
