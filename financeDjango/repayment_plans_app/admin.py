from django.contrib import admin

from financeDjango.mixins import AdminAddFieldSetMixin
from financeDjango.repayment_plans_app.models import EqualInstallmentPlan, EqualPrincipalPortionPlan, \
    EqualInstallmentChangeableIPPlan


@admin.register(EqualInstallmentPlan)
class AdminEqualInstallmentPlan(AdminAddFieldSetMixin, admin.ModelAdmin):
    list_display = ('user', 'borrowed_amount', 'interest_rate', 'periods', 'created_at',)
    search_fields = ('user__email', )
    ordering = ('user', )
    list_filter = ('user', 'borrowed_amount', )
    list_per_page = 15

    fieldsets = (
        (
            'Edit Repayment Plan',
            {
                'fields': ('user', 'borrowed_amount', 'interest_rate', 'periods', )
            }
        ),
    )

    add_fieldsets = (
        (
            'Add Repayment Plan',
            {
                "classes": ("wide",),
                'fields': ('user', 'borrowed_amount', 'interest_rate', 'periods', ),
            },
        ),
    )

@admin.register(EqualPrincipalPortionPlan)
class AdminEqualPrincipalPortionPlan(AdminAddFieldSetMixin, admin.ModelAdmin):
    list_display = ('user', 'borrowed_amount', 'interest_rate', 'periods', 'created_at',)
    search_fields = ('user__email',)
    ordering = ('user',)
    list_filter = ('user', 'borrowed_amount',)
    list_per_page = 15

    fieldsets = (
        (
            'Edit Repayment Plan',
            {
                'fields': ('user', 'borrowed_amount', 'interest_rate', 'periods',)
            }
        ),
    )

    add_fieldsets = (
        (
            'Add Repayment Plan',
            {
                "classes": ("wide",),
                'fields': ('user', 'borrowed_amount', 'interest_rate', 'periods',),
            },
        ),
    )


@admin.register(EqualInstallmentChangeableIPPlan)
class AdminEqualInstallmentChangeableIPPlan(AdminAddFieldSetMixin, admin.ModelAdmin):
    list_display = ('user', 'borrowed_amount', 'interest_rate_first_period',
                    'interest_rate_second_period', 'first_period',
                    'second_period', 'created_at')
    search_fields = ('user__email',)
    ordering = ('user',)
    list_filter = ('user', 'borrowed_amount',)
    list_per_page = 15

    fieldsets = (
        (
            'Edit Repayment Plan',
            {
                'fields': ('user', 'borrowed_amount',
                           'interest_rate_first_period','interest_rate_second_period',
                           'first_period', 'second_period',)
            }
        ),
    )

    add_fieldsets = (
        (
            'Add Repayment Plan',
            {
                "classes": ("wide",),
                'fields': ('user', 'borrowed_amount',
                           'interest_rate_first_period','interest_rate_second_period',
                           'first_period', 'second_period',),
            },
        ),
    )
