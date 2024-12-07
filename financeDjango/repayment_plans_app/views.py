from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView, ListView

from financeDjango.mixins import OperationNameContextMixin, CreateActionFormValidMixin, RepaymentJSONContextToTableMixin
from financeDjango.repayment_plans_app.forms import EqualInstallmentForm, EqualPrincipalPortionForm, \
    EqualInstallmentChangeableIPForm
from financeDjango.repayment_plans_app.helpers import calculate_equal_installment, calculate_equal_principle_portion, \
    calculate_equal_installment_changeable_ip_repayment_plan
from financeDjango.repayment_plans_app.models import EqualInstallmentPlan, EqualPrincipalPortionPlan, \
    EqualInstallmentChangeableIPPlan


class EqualInstallmentPlanCalculateView(LoginRequiredMixin, OperationNameContextMixin, FormView):
    template_name = 'repayment_plans_templates/equal_installment_pp/repayment_plans_calculations.html'
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


class EqualInstallmentPlanListView(LoginRequiredMixin, RepaymentJSONContextToTableMixin,  ListView):
    model = EqualInstallmentPlan
    template_name = 'repayment_plans_templates/equal_installment_pp/repayment_plans_list.html'
    context_object_name = 'plans'
    paginate_by = 5


    def get_queryset(self):
        queryset = EqualInstallmentPlan.objects.filter(user=self.request.user).order_by('-id')
        return queryset

#2
class EqualPPPlanCalculateView(LoginRequiredMixin, OperationNameContextMixin, FormView):
    template_name = 'repayment_plans_templates/equal_installment_pp/repayment_plans_calculations.html'
    form_class = EqualPrincipalPortionForm
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
    model = EqualPrincipalPortionPlan
    fields = ['borrowed_amount', 'interest_rate', 'periods', 'repayment']
    success_url = reverse_lazy('equal-pp-calculation')


class EqualPPPlanListView(LoginRequiredMixin, RepaymentJSONContextToTableMixin, ListView):
    model = EqualPrincipalPortionPlan
    template_name = 'repayment_plans_templates/equal_installment_pp/repayment_plans_list.html'
    context_object_name = 'plans'
    paginate_by = 5


    def get_queryset(self):
        queryset = EqualPrincipalPortionPlan.objects.filter(user=self.request.user).order_by('-id')
        return queryset


#3
class EqualInstallmentChangeableIpCalculateView(LoginRequiredMixin, OperationNameContextMixin, FormView):
    template_name = 'repayment_plans_templates/equal_installment_pp/repayment_plans_calculations.html'
    form_class = EqualInstallmentChangeableIPForm
    operation_name = "Equal Installment With Changeable IP Repayment Plan"

    def form_valid(self, form):
        try:
            borrowed_amount = form.cleaned_data['borrowed_amount']
            interest_rate_first_period = form.cleaned_data['interest_rate_first_period']
            interest_rate_second_period = form.cleaned_data['interest_rate_second_period']
            first_period = form.cleaned_data['first_period']
            second_period = form.cleaned_data['second_period']

            repayment = calculate_equal_installment_changeable_ip_repayment_plan(borrowed_amount,
                                                                                 interest_rate_first_period,
                                                                                 interest_rate_second_period,
                                                                                 first_period,
                                                                                 second_period,
                                                                                 )
            print(repayment)

        except Exception as e:
            form.add_error(None, f"An error occurred during calculation: {e}")
            return self.form_invalid(form)

        return self.render_to_response(self.get_context_data(
            form=form,
            repayment=repayment,
            borrowed_amount=borrowed_amount,
            interest_rate_first_period=interest_rate_first_period,
            interest_rate_second_period=interest_rate_second_period,
            first_period=first_period,
            second_period=second_period,
        ))


class EqualInstallmentChangeableIpSaveView(LoginRequiredMixin,  CreateActionFormValidMixin, CreateView):
    model = EqualInstallmentChangeableIPPlan
    fields = ['borrowed_amount', 'interest_rate_first_period', 'interest_rate_second_period', 'first_period',
              'second_period', 'repayment']
    success_url = reverse_lazy('equal-installment-changeable-ip-calculation')



class EqualInstallmentChangeableIpListView(LoginRequiredMixin, RepaymentJSONContextToTableMixin, ListView):
    model = EqualInstallmentChangeableIPPlan
    template_name = 'repayment_plans_templates/changeable_ip_plans/changeable_ip_plans_list.html'
    context_object_name = 'plans'
    paginate_by = 5


    def get_queryset(self):
        queryset = EqualInstallmentChangeableIPPlan.objects.filter(user=self.request.user).order_by('-id')
        return queryset