# import ast
# import json
# from json import JSONDecodeError

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView, ListView

from financeDjango.mixins import OperationNameContextMixin, CreateActionFormValidMixin, RepaymentJSONContextToTableMixin
from financeDjango.repayment_plans_app.forms import EqualInstallmentForm, EqualPrinciplePortionForm
from financeDjango.repayment_plans_app.helpers import calculate_equal_installment, calculate_equal_principle_portion
from financeDjango.repayment_plans_app.models import EqualInstallmentPlan, EqualPrinciplePortionPlan


class EqualInstallmentPlanCalculateView(LoginRequiredMixin, OperationNameContextMixin, FormView):
    template_name = 'repayment_plans_templates/equal_installment_pp/equal_installment_and_pp_calculation.html'
    form_class = EqualInstallmentForm
    operation_name = 'Equal Installment Repayment Plan'

    def form_valid(self, form):
        try:
            borrowed_amount = form.cleaned_data['borrowed_amount']
            interest_rate = form.cleaned_data['interest_rate']
            periods = form.cleaned_data['periods']

            repayment = calculate_equal_installment(borrowed_amount, interest_rate, periods)
            print(repayment)

        except Exception as e:
            form.add_error(None, f"An error occurred during calculation: {e}")
            return self.form_invalid(form)

        return self.render_to_response(self.get_context_data(
            form=form,
            repayment=repayment,
            borrowed_amount=borrowed_amount,
            interest_rate=interest_rate,
            periods=periods,
        ))


class EqualInstallmentPlanSaveView(LoginRequiredMixin, CreateActionFormValidMixin, CreateView):
    model = EqualInstallmentPlan
    fields = ['borrowed_amount', 'interest_rate', 'periods', 'repayment']
    success_url = reverse_lazy('equal-installment-calculation')


class EqualInstallmentPlanListView(LoginRequiredMixin,RepaymentJSONContextToTableMixin,  ListView):
    model = EqualInstallmentPlan
    template_name = 'repayment_plans_templates/equal_installment_pp/repayment_plans_list.html'
    context_object_name = 'plans'
    paginate_by = 5

    def get_queryset(self):
        queryset = EqualInstallmentPlan.objects.filter(user=self.request.user).order_by('-id')
        return queryset

#2
class EqualPPPlanCalculateView(LoginRequiredMixin, OperationNameContextMixin, FormView):
    template_name = 'repayment_plans_templates/equal_installment_pp/equal_installment_and_pp_calculation.html'
    form_class = EqualPrinciplePortionForm
    operation_name = 'Equal Principle Portion Repayment Plan'

    def form_valid(self, form):
        try:
            borrowed_amount = form.cleaned_data['borrowed_amount']
            interest_rate = form.cleaned_data['interest_rate']
            periods = form.cleaned_data['periods']

            repayment = calculate_equal_principle_portion(borrowed_amount, interest_rate, periods)
            print(repayment)

        except Exception as e:
            form.add_error(None, f"An error occurred during calculation: {e}")
            return self.form_invalid(form)

        return self.render_to_response(self.get_context_data(
            form=form,
            repayment=repayment,
            borrowed_amount=borrowed_amount,
            interest_rate=interest_rate,
            periods=periods,
        ))

class EqualPPPlanSaveView(LoginRequiredMixin, CreateActionFormValidMixin, CreateView):
    model = EqualPrinciplePortionPlan
    fields = ['borrowed_amount', 'interest_rate', 'periods', 'repayment']
    success_url = reverse_lazy('equal-pp-calculation')


class EqualPPPlanListView(LoginRequiredMixin, RepaymentJSONContextToTableMixin, ListView):
    model = EqualPrinciplePortionPlan
    template_name = 'repayment_plans_templates/equal_installment_pp/repayment_plans_list.html'
    context_object_name = 'plans'
    paginate_by = 5

    def get_queryset(self):
        queryset = EqualPrinciplePortionPlan.objects.filter(user=self.request.user).order_by('-id')
        return queryset
