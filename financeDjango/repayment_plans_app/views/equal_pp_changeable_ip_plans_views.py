from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView, UpdateView, DeleteView, ListView

from financeDjango.mixins import OperationNameContextMixin, CreateActionFormValidMixin, RepaymentJSONContextToTableMixin
from financeDjango.repayment_plans_app.forms import EqualPrincipalPortionChangeableIPForm, \
    EqualPrincipalPortionChangeableIPEditForm, EqualPrincipalPortionChangeableIPDeleteForm
from financeDjango.repayment_plans_app.helpers import calculate_equal_principle_portion_changeable_ip_repayment_plan
from financeDjango.repayment_plans_app.models import EqualPrincipalPortionChangeableIPPlan


class EqualPrincipalPortionChangeableIPCalculateView(LoginRequiredMixin, OperationNameContextMixin, FormView):
    template_name = 'repayment_plans_templates/repayment_plans_calculations.html'
    form_class = EqualPrincipalPortionChangeableIPForm
    operation_name = "Equal Principal Portion With Changeable IP Repayment Plan"

    def form_valid(self, form):
        try:
            borrowed_amount = form.cleaned_data['borrowed_amount']
            interest_rate_first_period = form.cleaned_data['interest_rate_first_period']
            interest_rate_second_period = form.cleaned_data['interest_rate_second_period']
            number_of_periods = form.cleaned_data['number_of_periods']
            second_period = form.cleaned_data['second_period']

            repayment = calculate_equal_principle_portion_changeable_ip_repayment_plan(borrowed_amount,
                                                                                 interest_rate_first_period,
                                                                                 interest_rate_second_period,
                                                                                 number_of_periods,
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
            number_of_periods=number_of_periods,
            second_period=second_period,
        ))

class EqualPrincipalPortionChangeableIPSaveView(LoginRequiredMixin, CreateActionFormValidMixin, CreateView):
    model = EqualPrincipalPortionChangeableIPPlan
    fields = ['borrowed_amount', 'interest_rate_first_period', 'interest_rate_second_period', 'number_of_periods',
              'second_period', 'repayment']
    success_url = reverse_lazy('equal-pp-changeable-ip-calculation')

class EqualPrincipalPortionChangeableIPListView(LoginRequiredMixin, RepaymentJSONContextToTableMixin, ListView):
    template_name = 'repayment_plans_templates/changeable_ip_plans/equal_pp_changeable_ip_plans_list.html'
    model = EqualPrincipalPortionChangeableIPPlan
    paginate_by = 5
    context_object_name = 'plans'

    def get_queryset(self):
        queryset = EqualPrincipalPortionChangeableIPPlan.objects.filter(user=self.request.user).order_by('-id')
        return queryset

class EqualPrincipalPortionChangeableIPEditView(LoginRequiredMixin, UserPassesTestMixin,  UpdateView):
    model = EqualPrincipalPortionChangeableIPPlan
    form_class = EqualPrincipalPortionChangeableIPEditForm
    template_name = 'personal_actions_templates/edit_action.html'
    success_url = reverse_lazy('equal-pp-changeable-ip-list')

    def test_func(self):
        plan = get_object_or_404(EqualPrincipalPortionChangeableIPPlan, pk=self.kwargs['pk'])
        return self.request.user == plan.user

    def form_valid(self, form):

        plan = form.save(commit=False)

        borrowed_amount = form.cleaned_data['borrowed_amount']
        interest_rate_first_period = form.cleaned_data['interest_rate_first_period']
        interest_rate_second_period = form.cleaned_data['interest_rate_second_period']
        number_of_periods = form.cleaned_data['number_of_periods']
        second_period = form.cleaned_data['second_period']

        repayment = calculate_equal_principle_portion_changeable_ip_repayment_plan(borrowed_amount,
                                                                                   interest_rate_first_period,
                                                                                   interest_rate_second_period,
                                                                                   number_of_periods, second_period,
                                                                                   )

        plan.repayment = repayment
        plan.save()

        return redirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.object:
            context['repayment'] = self.object.repayment
            context['borrowed_amount'] = self.object.borrowed_amount
            context['interest_rate_first_period'] = self.object.interest_rate_first_period
            context['interest_rate_second_period'] = self.object.interest_rate_second_period
            context['number_of_periods'] = self.object.number_of_periods
            context['second_period'] = self.object.second_period
        return context

class EqualPrincipalPortionChangeableIPDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = EqualPrincipalPortionChangeableIPPlan
    template_name = 'personal_actions_templates/delete_action.html'
    form_class = EqualPrincipalPortionChangeableIPDeleteForm
    success_url = reverse_lazy('equal-pp-changeable-ip-list')

    def test_func(self):
        plan = get_object_or_404(EqualPrincipalPortionChangeableIPPlan, pk=self.kwargs['pk'])
        return self.request.user == plan.user

    def get_initial(self):
        return self.get_object().__dict__

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'data': self.get_initial(),
        })

        return kwargs
