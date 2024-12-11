from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from financeDjango.mixins import CreateActionFormValidMixin, OperationNameContextMixin
from financeDjango.personal_actions_app.forms import TransactionForm, PortfolioForm, BudgetForm, GoalForm, \
    BudgetDeleteForm, GoalDeleteForm, PortfolioDeleteForm, TransactionDeleteForm, TransactionEditForm, \
    PortfolioEditForm, BudgetEditForm, GoalEditForm
from financeDjango.personal_actions_app.models import Transaction, InvestmentPortfolio, Budget, FinancialGoal


class CreateTransactionView(LoginRequiredMixin, CreateActionFormValidMixin, OperationNameContextMixin,  CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'personal_actions_templates/create_action.html'
    success_url = reverse_lazy('show-transactions')
    operation_name = 'Transaction'


class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'personal_actions_templates/transaction_templates/transaction_list.html'
    context_object_name = 'transactions'
    paginate_by = 5

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user).order_by('-date')

class TransactionEditView(LoginRequiredMixin, UserPassesTestMixin,  UpdateView):
    model = Transaction
    form_class = TransactionEditForm
    template_name = 'personal_actions_templates/edit_action.html'
    success_url = reverse_lazy('show-transactions')

    def test_func(self):
        transaction = get_object_or_404(Transaction, pk=self.kwargs['pk'])

        return self.request.user == transaction.user

class TransactionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Transaction
    template_name = 'personal_actions_templates/delete_action.html'
    form_class = TransactionDeleteForm
    success_url = reverse_lazy('show-transactions')

    def test_func(self):
        transaction = get_object_or_404(Transaction, pk=self.kwargs['pk'])

        return self.request.user == transaction.user

    def get_initial(self):
        return self.get_object().__dict__

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'data': self.get_initial(),
        })

        return kwargs

class CreatePortfolioView(LoginRequiredMixin, CreateActionFormValidMixin, OperationNameContextMixin,  CreateView):
    model = InvestmentPortfolio
    form_class = PortfolioForm
    template_name = 'personal_actions_templates/create_action.html'
    success_url = reverse_lazy('show-portfolio')
    operation_name = 'Investment Portfolio'


class PortfolioListView(LoginRequiredMixin, ListView):
    model = InvestmentPortfolio
    template_name = 'personal_actions_templates/portfolio_templates/portfolio-list.html'
    context_object_name = 'portfolio'
    paginate_by = 5

    def get_queryset(self):
        return InvestmentPortfolio.objects.filter(user=self.request.user).order_by('-created_at')

class PortfolioEditView(LoginRequiredMixin, UserPassesTestMixin,  UpdateView):
    model = InvestmentPortfolio
    form_class = PortfolioEditForm
    template_name = 'personal_actions_templates/edit_action.html'
    success_url = reverse_lazy('show-portfolio')

    def test_func(self):
        portfolio = get_object_or_404(InvestmentPortfolio, pk=self.kwargs['pk'])

        return self.request.user == portfolio.user

class PortfolioDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = InvestmentPortfolio
    template_name = 'personal_actions_templates/delete_action.html'
    form_class = PortfolioDeleteForm
    success_url = reverse_lazy('show-portfolio')

    def test_func(self):
        portfolio = get_object_or_404(InvestmentPortfolio, pk=self.kwargs['pk'])

        return self.request.user == portfolio.user

    def get_initial(self):
        return self.get_object().__dict__

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'data': self.get_initial(),
        })

        return kwargs

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

class GoalCreateView(LoginRequiredMixin, CreateActionFormValidMixin, OperationNameContextMixin, CreateView):
    model = FinancialGoal
    form_class = GoalForm
    template_name = 'personal_actions_templates/create_action.html'
    success_url = reverse_lazy('show-goals')
    operation_name = 'Goal'

class GoalListView(LoginRequiredMixin, ListView):
    model = FinancialGoal
    template_name = 'personal_actions_templates/goal_templates/goal_list.html'
    context_object_name = 'goals'
    paginate_by = 5

    def get_queryset(self):
        return FinancialGoal.objects.filter(user=self.request.user).order_by('-target_amount', '-deadline')

class GoalEditView(LoginRequiredMixin, UserPassesTestMixin,  UpdateView):
    model = FinancialGoal
    form_class = GoalEditForm
    template_name = 'personal_actions_templates/edit_action.html'
    success_url = reverse_lazy('show-goals')

    def test_func(self):
        # Check if the user owns the budget
        goal = get_object_or_404(FinancialGoal, pk=self.kwargs['pk'])

        return self.request.user == goal.user

class GoalDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = FinancialGoal
    template_name = 'personal_actions_templates/delete_action.html'
    form_class = GoalDeleteForm
    success_url = reverse_lazy('show-goals')

    def test_func(self):
        goal = get_object_or_404(FinancialGoal, pk=self.kwargs['pk'])

        return self.request.user == goal.user

    def get_initial(self):
        return self.get_object().__dict__

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'data': self.get_initial(),
        })

        return kwargs
