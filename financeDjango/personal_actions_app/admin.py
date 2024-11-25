from django.contrib import admin

from financeDjango.mixins import AdminAddFieldSetMixin
from financeDjango.personal_actions_app.models import Budget


@admin.register(Budget)
class BudgetAdmin(AdminAddFieldSetMixin, admin.ModelAdmin):

    list_display = ('user', 'category', 'amount', 'start_date', 'end_date')
    search_fields = ('user__email', 'category',)
    ordering = ('user',)
    list_filter = ('user', 'category',)

    fieldsets = (
        ('Edit Budget', {'fields': ('user', 'category', 'amount', 'start_date', 'end_date')}),
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
