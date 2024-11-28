from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from financeDjango.mixins import CreateActionFormValidMixin, OperationNameContextMixin
from financeDjango.personal_actions_app.forms import TransactionForm, PortfolioForm, BudgetForm, GoalForm
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