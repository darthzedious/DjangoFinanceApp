from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView, ListView, UpdateView, DeleteView

from financeDjango.mixins import OperationNameContextMixin, CreateActionFormValidMixin, RepaymentJSONContextToTableMixin
from financeDjango.repayment_plans_app.forms import EqualPrincipalPortionForm, EqualPrincipalPortionEditForm, \
    EqualPrincipalPortionDeleteForm
from financeDjango.repayment_plans_app.helpers import calculate_equal_principle_portion
from financeDjango.repayment_plans_app.models import EqualPrincipalPortionPlan


class EqualPPPlanCalculateView(LoginRequiredMixin, OperationNameContextMixin, FormView):
    template_name = 'repayment_plans_templates/repayment_plans_calculations.html'
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
    template_name = 'repayment_plans_templates/equal_installment_pp/equal_principal_portion_plans_list.html'
    context_object_name = 'plans'
    paginate_by = 5


    def get_queryset(self):
        queryset = EqualPrincipalPortionPlan.objects.filter(user=self.request.user).order_by('-id')
        return queryset


class EqualPPPlanEditView(LoginRequiredMixin, UserPassesTestMixin,  UpdateView):
    model = EqualPrincipalPortionPlan
    form_class = EqualPrincipalPortionEditForm
    template_name = 'personal_actions_templates/edit_action.html'
    success_url = reverse_lazy('equal-pp-plans-list')

    def test_func(self):
        plan = get_object_or_404(EqualPrincipalPortionPlan, pk=self.kwargs['pk'])
        return self.request.user == plan.user

    def form_valid(self, form):
        #get the current plan instance
        plan = form.save(commit=False)

        borrowed_amount = form.cleaned_data['borrowed_amount']
        interest_rate = form.cleaned_data['interest_rate']
        periods = form.cleaned_data['periods']

        repayment = calculate_equal_principle_portion(borrowed_amount, interest_rate, periods)

        plan.repayment = repayment
        plan.save()

        return redirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        # Get context data for the edit view (form, repayment data, etc.)
        context = super().get_context_data(**kwargs)
        if self.object:
            context['repayment'] = self.object.repayment
            context['borrowed_amount'] = self.object.borrowed_amount
            context['interest_rate'] = self.object.interest_rate
            context['periods'] = self.object.periods
        return context

class EqualPPPlanDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = EqualPrincipalPortionPlan
    template_name = 'personal_actions_templates/delete_action.html'
    form_class = EqualPrincipalPortionDeleteForm
    success_url = reverse_lazy('equal-pp-plans-list')

    def test_func(self):
        plan = get_object_or_404(EqualPrincipalPortionPlan, pk=self.kwargs['pk'])
        return self.request.user == plan.user

    def get_initial(self):
        return self.get_object().__dict__

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'data': self.get_initial(),
        })

        return kwargs
