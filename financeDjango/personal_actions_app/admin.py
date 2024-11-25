from django.contrib import admin

from financeDjango.mixins import AddAdminFieldSetMixin
from financeDjango.personal_actions_app.forms import BudgetForm
from financeDjango.personal_actions_app.models import Budget


# Register your models here.

@admin.register(Budget)
class BudgetAdmin(AddAdminFieldSetMixin, admin.ModelAdmin):
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

    def get_fieldsets(self, request, obj=None):
        if obj is None: # If object is not already created return add_fieldsets
            return self.add_fieldsets
        return super().get_fieldsets(request, obj)
