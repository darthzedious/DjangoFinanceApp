from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from financeDjango.mixins import CreateActionFormValidMixin, OperationNameContextMixin
from financeDjango.personal_actions_app.forms import BudgetForm, BudgetEditForm, BudgetDeleteForm
from financeDjango.personal_actions_app.models import Budget


class BudgetCreateView(LoginRequiredMixin, CreateActionFormValidMixin, OperationNameContextMixin, CreateView):
    model = Budget
    form_class = BudgetForm
    template_name = 'personal_actions_templates/create_action.html'
    success_url = reverse_lazy('show-budgets')
    operation_name = 'Budget'

class BudgetListView(LoginRequiredMixin, ListView):
    model = Budget
    template_name = 'personal_actions_templates/budget_templates/list_budget.html'
    context_object_name = 'budgets'
    paginate_by = 5

    def get_queryset(self):
        return Budget.objects.filter(user=self.request.user).order_by('start_date')

class BudgetEditView(LoginRequiredMixin, UserPassesTestMixin,  UpdateView):
    model = Budget
    form_class = BudgetEditForm
    template_name = 'personal_actions_templates/edit_action.html'
    success_url = reverse_lazy('show-budgets')

    def test_func(self):
        # Check if the user owns the budget
        budget = get_object_or_404(Budget, pk=self.kwargs['pk'])

        return self.request.user == budget.user

class BudgetDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Budget
    template_name = 'personal_actions_templates/delete_action.html'
    form_class = BudgetDeleteForm
    success_url = reverse_lazy('show-budgets')

    def test_func(self):
        budget = get_object_or_404(Budget, pk=self.kwargs['pk'])

        return self.request.user == budget.user

    def get_initial(self):
        return self.get_object().__dict__

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'data': self.get_initial(),
        })

        return kwargs
