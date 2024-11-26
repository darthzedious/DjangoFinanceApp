import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView, ListView

from financeDjango.repayment_plans_app.forms import EqualInstallmentForm
from financeDjango.repayment_plans_app.helpers import calculate_equal_installment
from financeDjango.repayment_plans_app.models import EqualInstallmentPlan





class EqualInstallmentPlanCalculateView(LoginRequiredMixin, FormView):
    template_name = 'repayment_plans_templates/equal_installment/equal_installment_calculation.html'
    form_class = EqualInstallmentForm

    def form_valid(self, form):
        try:
            borrowed_amount = form.cleaned_data['borrowed_amount']
            interest_rate = form.cleaned_data['interest_rate']
            periods = form.cleaned_data['periods']

            repayment = calculate_equal_installment(borrowed_amount, interest_rate, periods)

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


class EqualInstallmentPlanSaveView(LoginRequiredMixin, CreateView):
    model = EqualInstallmentPlan
    fields = ['borrowed_amount', 'interest_rate', 'periods', 'repayment']
    success_url = reverse_lazy('equal-installment-calculation')

    def form_valid(self, form):
        form.instance.user = self.request.user
        # form.instance.repayment = json.dumps(form.instance.repayment)
        return super().form_valid(form)


class RepaymentPlansListView(LoginRequiredMixin, ListView):
    model = EqualInstallmentPlan
    template_name = 'repayment_plans_templates/equal_installment/repayment_plans_list.html'
    context_object_name = 'plans'
    paginate_by = 5

    # def get_queryset(self):
    #     return EqualInstallmentPlan.objects.filter(user=self.request.user)

    # def get_queryset(self):
    #     queryset = EqualInstallmentPlan.objects.filter(user=self.request.user)
    #
    #     # Debugging: Print or log the queryset to check if it's correct
    #     print(f"Queryset contains: {queryset}")  # or use logging
    #
    #     for plan in queryset:
    #         try:
    #             # Deserialize repayment field from JSON string to Python list of dictionaries
    #             plan.repayment_data = json.loads(plan.repayment)
    #         except json.JSONDecodeError:
    #             plan.repayment_data = []  # Fallback if JSON is invalid
    #
    #     return queryset
    def get_queryset(self):
        queryset = EqualInstallmentPlan.objects.filter(user=self.request.user)
        print(f"Queryset contains: {queryset}")  # or use logging
        # Deserialize repayment field from JSON string to Python list of dictionaries

        # for plan in queryset:
        #     print(plan.repayment)
        #     try:
        #         plan.repayment = json.loads(plan.repayment)  # Deserialize to list of dicts
        #     except json.JSONDecodeError:
        #         plan.repayment = []  # Fallback if JSON is invalid

        return queryset