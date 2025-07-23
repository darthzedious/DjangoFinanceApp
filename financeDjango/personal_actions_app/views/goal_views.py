from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from financeDjango.mixins import CreateActionFormValidMixin, OperationNameContextMixin
from financeDjango.personal_actions_app.forms import GoalForm, GoalEditForm, GoalDeleteForm
from financeDjango.personal_actions_app.models import FinancialGoal


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
