from django import forms

from financeDjango.mixins import DisabledReadonlyMixin
from financeDjango.personal_actions_app.models import Transaction, InvestmentPortfolio, Budget, FinancialGoal


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['type', 'amount', 'description']
        widgets = {
            'type': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Select Transaction Type',
            }),
            'amount': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Amount...',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Describe your transaction...',
            }),
        }

class TransactionDeleteForm(DisabledReadonlyMixin, TransactionForm):
    pass

class TransactionEditForm(TransactionForm):
    pass

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = InvestmentPortfolio
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter name for the investment portfolio...',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Describe your investment...',
            }),
        }

class PortfolioDeleteForm(DisabledReadonlyMixin, PortfolioForm):
    pass

class PortfolioEditForm(PortfolioForm):
    pass

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['category', 'amount', 'start_date', 'end_date']
        widgets = {
            'category': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter category...',
            }),
            'amount': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Amount ...',
            }),
            'start_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'end_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
        }

class BudgetDeleteForm(DisabledReadonlyMixin, BudgetForm):
    pass

class BudgetEditForm(BudgetForm):
    pass

class GoalForm(forms.ModelForm):
    class Meta:
        model = FinancialGoal
        fields = ['title', 'target_amount', 'saved_amount', 'deadline']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the Goal title...',
            }),
            'target_amount': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the target amount...',
            }),
            'saved_amount': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the saved amount...',
            }),
            'deadline': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'placeholder': 'Choose the deadline date...',
            }),
        }

class GoalDeleteForm(DisabledReadonlyMixin, GoalForm):
    pass

class GoalEditForm(GoalForm):
    pass
