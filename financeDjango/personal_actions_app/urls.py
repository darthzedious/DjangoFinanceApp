from django.urls import path

from financeDjango.personal_actions_app import views

urlpatterns = [
    path('create-transaction/', views.CreateTransactionView.as_view(), name='create-transaction'),
    path('show-transactions/', views.TransactionListView.as_view(), name='show-transactions'),
    path('create-portfolio/', views.CreatePortfolioView.as_view(), name='create-portfolio'),
    path('show-portfolio/', views.PortfolioListView.as_view(), name='show-portfolio'),
    path('create-budget/', views.BudgetCreateView.as_view(), name='create-budget'),
    path('show-budget/', views.BudgetListView.as_view(), name='show-budgets'),
    path('create-goal/', views.GoalCreateView.as_view(), name='create-goal'),
    path('show-goals/', views.GoalListView.as_view(), name='show-goals'),
]
