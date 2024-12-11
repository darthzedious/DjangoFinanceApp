from django.contrib import admin

from financeDjango.mixins import AdminAddFieldSetMixin
from financeDjango.personal_actions_app.models import Budget, FinancialGoal, InvestmentPortfolio, Transaction


@admin.register(Budget)
class BudgetAdmin(AdminAddFieldSetMixin, admin.ModelAdmin):

    list_display = ('user', 'category', 'amount', 'start_date', 'end_date')
    search_fields = ('user__email', 'category',)
    ordering = ('user',)
    list_filter = ('user', 'category',)
    list_per_page = 15

    fieldsets = (
        (
            'Edit Budget',
            {
                'fields': ('user', 'category', 'amount', 'start_date', 'end_date')
            }
        ),
    )

    add_fieldsets = (
        (
            'Add Budget',
            {
                "classes": ("wide",),
                'fields': ('user', 'category', 'amount', 'start_date', 'end_date'),
            },
        ),
    )

@admin.register(FinancialGoal)
class FinancialGoalAdmin(AdminAddFieldSetMixin, admin.ModelAdmin):

    list_display = ('user', 'title', 'target_amount', 'saved_amount', 'deadline')
    search_fields = ('user__email', 'title')
    ordering = ('user',)
    list_filter = ('user', 'title')
    list_per_page = 15

    fieldsets = (
        (
            'Edit Goal',
            {
                'fields': ('user', 'title', 'target_amount', 'saved_amount', 'deadline')
             }
        ),
    )

    add_fieldsets = (
        (
            'Add Goal',
            {
                "classes": ("wide",),
                'fields': ('user', 'title', 'target_amount', 'saved_amount', 'deadline'),
            }
        ),
    )


@admin.register(InvestmentPortfolio)
class InvestmentPortfolioAdmin(AdminAddFieldSetMixin, admin.ModelAdmin):
    list_display = ('user', 'name', 'description', 'created_at')
    search_fields = ('user__email', 'name', 'description')
    ordering = ('user',)
    list_filter = ('user', 'description')
    list_per_page = 15

    fieldsets = (
        (
            'Edit Goal',
            {
                'fields': ('user', 'name', 'description', )
            }
        ),
    )

    add_fieldsets = (
        (
            'Add Goal',
            {
                "classes": ("wide",),
                'fields': ('user', 'name', 'description', ),
            }
        ),
    )

@admin.register(Transaction)
class TransactionAdmin(AdminAddFieldSetMixin, admin.ModelAdmin):
    list_display = ('user', 'type', 'amount', 'description', 'date', )
    search_fields = ('user__email', 'type', 'description')
    ordering = ('user',)
    list_filter = ('user', 'type')
    list_per_page = 15

    fieldsets = (
        (
            'Edit Goal',
            {
                'fields': ('user', 'type', 'amount', 'description',)
            }
        ),
    )

    add_fieldsets = (
        (
            'Add Goal',
            {
                "classes": ("wide",),
                'fields': ('user', 'type', 'amount', 'description',),
            }
        ),
    )
