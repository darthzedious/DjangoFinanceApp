from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView, ListView, UpdateView, DeleteView

from financeDjango.mixins import OperationNameContextMixin, CreateActionFormValidMixin, RepaymentJSONContextToTableMixin
from financeDjango.repayment_plans_app.forms import EqualInstallmentForm, EqualPrincipalPortionForm, \
    EqualInstallmentChangeableIPForm, EqualInstallmentEditForm, EqualInstallmentDeleteForm, \
    EqualPrincipalPortionEditForm, EqualPrincipalPortionDeleteForm, EqualInstallmentChangeableIPDeleteForm, \
    EqualInstallmentChangeableIPEditForm, EqualPrincipalPortionChangeableIPForm, \
    EqualPrincipalPortionChangeableIPDeleteForm, EqualPrincipalPortionChangeableIPEditForm
from financeDjango.repayment_plans_app.helpers import calculate_equal_installment, calculate_equal_principle_portion, \
    calculate_equal_installment_changeable_ip_repayment_plan, \
    calculate_equal_principle_portion_changeable_ip_repayment_plan
from financeDjango.repayment_plans_app.models import EqualInstallmentPlan, EqualPrincipalPortionPlan, \
    EqualInstallmentChangeableIPPlan, EqualPrincipalPortionChangeableIPPlan


class EqualInstallmentPlanCalculateView(LoginRequiredMixin, OperationNameContextMixin, FormView):
    template_name = 'repayment_plans_templates/repayment_plans_calculations.html'
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
    template_name = 'repayment_plans_templates/equal_installment_pp/equal_installment_plans_list.html'
    context_object_name = 'plans'
    paginate_by = 5


    def get_queryset(self):
        queryset = EqualInstallmentPlan.objects.filter(user=self.request.user).order_by('-id')
        return queryset

class EqualInstallmentEditView(LoginRequiredMixin, UserPassesTestMixin,  UpdateView):
    model = EqualInstallmentPlan
    form_class = EqualInstallmentEditForm
    template_name = 'personal_actions_templates/edit_action.html'
    success_url = reverse_lazy('equal-installment-plans-list')

    def test_func(self):
        plan = get_object_or_404(EqualInstallmentPlan, pk=self.kwargs['pk'])
        return self.request.user == plan.user

    def form_valid(self, form):
        #get the current plan instance
        plan = form.save(commit=False)

        borrowed_amount = form.cleaned_data['borrowed_amount']
        interest_rate = form.cleaned_data['interest_rate']
        periods = form.cleaned_data['periods']

        repayment = calculate_equal_installment(borrowed_amount, interest_rate, periods)

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

class EqualInstallmentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = EqualInstallmentPlan
    template_name = 'personal_actions_templates/delete_action.html'
    form_class = EqualInstallmentDeleteForm
    success_url = reverse_lazy('equal-installment-plans-list')

    def test_func(self):
        plan = get_object_or_404(EqualInstallmentPlan, pk=self.kwargs['pk'])
        return self.request.user == plan.user

    def get_initial(self):
        return self.get_object().__dict__

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'data': self.get_initial(),
        })

        return kwargs

#2
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

#3
class EqualInstallmentChangeableIpCalculateView(LoginRequiredMixin, OperationNameContextMixin, FormView):
    template_name = 'repayment_plans_templates/repayment_plans_calculations.html'
    form_class = EqualInstallmentChangeableIPForm
    operation_name = "Equal Installment With Changeable IP Repayment Plan"

    def form_valid(self, form):
        try:
            borrowed_amount = form.cleaned_data['borrowed_amount']
            interest_rate_first_period = form.cleaned_data['interest_rate_first_period']
            interest_rate_second_period = form.cleaned_data['interest_rate_second_period']
            number_of_periods = form.cleaned_data['number_of_periods']
            second_period = form.cleaned_data['second_period']

            repayment = calculate_equal_installment_changeable_ip_repayment_plan(borrowed_amount,
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


class EqualInstallmentChangeableIpSaveView(LoginRequiredMixin,  CreateActionFormValidMixin, CreateView):
    model = EqualInstallmentChangeableIPPlan
    fields = ['borrowed_amount', 'interest_rate_first_period', 'interest_rate_second_period', 'number_of_periods',
              'second_period', 'repayment']
    success_url = reverse_lazy('equal-installment-changeable-ip-calculation')

    # def form_valid(self, form):
    #     # Check if the form is valid and the model is being saved
    #     instance = form.save()  # Save the instance
    #     print(f"Saved instance: {instance}")  # Ensure the instance is saved
    #
    #     # Return the response after saving
    #     return super().form_valid(form)

class EqualInstallmentChangeableIpListView(LoginRequiredMixin, RepaymentJSONContextToTableMixin, ListView):
    model = EqualInstallmentChangeableIPPlan
    template_name = 'repayment_plans_templates/changeable_ip_plans/equal_installment_changeable_ip_plans_list.html'
    context_object_name = 'plans'
    paginate_by = 5


    def get_queryset(self):
        queryset = EqualInstallmentChangeableIPPlan.objects.filter(user=self.request.user).order_by('-id')
        return queryset

class EqualInstallmentChangeableIpEditView(LoginRequiredMixin, UserPassesTestMixin,  UpdateView):
    model = EqualInstallmentChangeableIPPlan
    form_class = EqualInstallmentChangeableIPEditForm
    template_name = 'personal_actions_templates/edit_action.html'
    success_url = reverse_lazy('equal-installment-changeable-ip-list')

    def test_func(self):
        plan = get_object_or_404(EqualInstallmentChangeableIPPlan, pk=self.kwargs['pk'])
        return self.request.user == plan.user

    def form_valid(self, form):
        #get the current plan instance
        plan = form.save(commit=False)

        borrowed_amount = form.cleaned_data['borrowed_amount']
        interest_rate_first_period = form.cleaned_data['interest_rate_first_period']
        interest_rate_second_period = form.cleaned_data['interest_rate_second_period']
        number_of_periods = form.cleaned_data['number_of_periods']
        second_period = form.cleaned_data['second_period']

        repayment = calculate_equal_installment_changeable_ip_repayment_plan(borrowed_amount,
                                                                             interest_rate_first_period,
                                                                             interest_rate_second_period,
                                                                             number_of_periods,
                                                                             second_period,
                                                                             )

        plan.repayment = repayment
        plan.save()

        return redirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        # Get context data for the edit view (form, repayment data, etc.)
        context = super().get_context_data(**kwargs)
        if self.object:
            context['repayment'] = self.object.repayment
            context['borrowed_amount'] = self.object.borrowed_amount
            context['interest_rate_first_period'] = self.object.interest_rate_first_period
            context['interest_rate_second_period'] = self.object.interest_rate_second_period
            context['number_of_periods'] = self.object.number_of_periods
            context['second_period'] = self.object.second_period
        return context

class EqualInstallmentChangeableIpDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = EqualInstallmentChangeableIPPlan
    template_name = 'personal_actions_templates/delete_action.html'
    form_class = EqualInstallmentChangeableIPDeleteForm
    success_url = reverse_lazy('equal-installment-changeable-ip-list')

    def test_func(self):
        plan = get_object_or_404(EqualInstallmentChangeableIPPlan, pk=self.kwargs['pk'])
        return self.request.user == plan.user

    def get_initial(self):
        return self.get_object().__dict__

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'data': self.get_initial(),
        })

        return kwargs

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