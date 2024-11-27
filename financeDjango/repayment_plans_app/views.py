import ast
import json

from django.contrib.auth.mixins import LoginRequiredMixin
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


class EqualInstallmentPlanSaveView(LoginRequiredMixin, CreateView):
    model = EqualInstallmentPlan
    fields = ['borrowed_amount', 'interest_rate', 'periods', 'repayment']
    success_url = reverse_lazy('equal-installment-calculation')

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)


class RepaymentPlansListView(LoginRequiredMixin, ListView):
    model = EqualInstallmentPlan
    template_name = 'repayment_plans_templates/equal_installment/repayment_plans_list.html'
    context_object_name = 'plans'
    paginate_by = 5

    def get_queryset(self):
        queryset = EqualInstallmentPlan.objects.filter(user=self.request.user).order_by('-id')
        for plan in queryset:
            print(f"Plan ID {plan.id}: repayment={plan.repayment}")

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        for plan in context['plans']:
            try:
                # Try to load the JSON with proper quotes
                plan.repayment_table = json.loads(plan.repayment)
            except json.JSONDecodeError:
                try:
                    # Handle pseudo-JSON with single quotes using ast.literal_eval
                    plan.repayment_table = ast.literal_eval(plan.repayment)
                except (ValueError, SyntaxError) as e:
                    print(f"Error parsing repayment data for plan {plan.id}: {e}")
                    # Default to an empty list if both methods fail
                    plan.repayment_table = []

        return context