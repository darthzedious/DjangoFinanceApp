from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from financeDjango.mixins import CreateActionFormValidMixin, OperationNameContextMixin
from financeDjango.personal_actions_app.forms import TransactionForm, TransactionEditForm, TransactionDeleteForm
from financeDjango.personal_actions_app.models import Transaction


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
