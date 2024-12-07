from django.urls import path, include

from financeDjango.personal_actions_app import views

urlpatterns = [
    path('create-transaction/', views.CreateTransactionView.as_view(), name='create-transaction'),
    path('show-transactions/', views.TransactionListView.as_view(), name='show-transactions'),
    path('transaction/<int:pk>/', include([
        path('edit/', views.TransactionEditView.as_view(), name='edit-transaction'),
        path('delete/', views.TransactionDeleteView.as_view(), name='delete-transaction'),
    ])),

    path('create-portfolio/', views.CreatePortfolioView.as_view(), name='create-portfolio'),
    path('show-portfolio/', views.PortfolioListView.as_view(), name='show-portfolio'),
    path('portfolio/<int:pk>/', include([
        path('edit/', views.PortfolioEditView.as_view(), name='edit-portfolio'),
        path('delete/', views.PortfolioDeleteView.as_view(), name='delete-portfolio'),
    ])),

    path('create-budget/', views.BudgetCreateView.as_view(), name='create-budget'),
    path('show-budget/', views.BudgetListView.as_view(), name='show-budgets'),
    path('budget/<int:pk>/', include([
        path('edit/', views.BudgetEditView.as_view(), name='edit-budgets'),
        path('delete/', views.BudgetDeleteView.as_view(), name='delete-budgets'),
    ])),

    path('create-goal/', views.GoalCreateView.as_view(), name='create-goal'),
    path('show-goals/', views.GoalListView.as_view(), name='show-goals'),
    path('goal/<int:pk>/', include([
        path('edit/', views.GoalEditView.as_view(), name='edit-goal'),
        path('delete/', views.GoalDeleteView.as_view(), name='delete-goal'),
    ])),

]
