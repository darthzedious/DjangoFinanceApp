from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from financeDjango.mixins import CreateActionFormValidMixin, OperationNameContextMixin
from financeDjango.personal_actions_app.forms import PortfolioForm, PortfolioEditForm, PortfolioDeleteForm
from financeDjango.personal_actions_app.models import InvestmentPortfolio


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
