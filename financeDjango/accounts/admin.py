from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.urls import reverse
from django.utils.html import format_html

from financeDjango.accounts.forms import RegisterForm, AppUserChangeForm
from financeDjango.accounts.models import Profile


# Register your models here.

UserModel = get_user_model()

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    fields = ('date_of_birth', 'profile_picture', )


@admin.register(UserModel)
class AppUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    add_form = RegisterForm
    form = AppUserChangeForm

    list_display = ('pk', 'email', 'is_staff', 'is_superuser',
                    'view_budgets', 'view_finance_goals',
                    'view_investment', 'view_transactions', 'view_equal_installment_plans',
                    'view_equal_principal_portion_plans', 'view_equal_installment_changeable_ip_plans')

    search_fields = ('email',)
    ordering = ('pk',)
    list_filter = ('is_staff', 'is_superuser', 'is_active',)
    list_per_page = 15

    fieldsets = (
        ('Credentials', {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (
            'REGISTER USER',
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )

    def view_budgets(self, obj):
        url = reverse('admin:personal_actions_app_budget_changelist')
        return format_html(
            '<a href="{}?user__id__exact={}">View Budgets</a>',
            url,
            obj.id,
        )

    view_budgets.short_description = "Budgets"

    def view_finance_goals(self, obj):
        url = reverse('admin:personal_actions_app_financialgoal_changelist')
        return format_html(
            '<a href="{}?user__id__exact={}">View Goals</a>',
            url,
            obj.id,
        )

    view_finance_goals.short_description = "Goals"

    def view_investment(self, obj):
        url = reverse('admin:personal_actions_app_investmentportfolio_changelist')
        return format_html(
            '<a href="{}?user__id__exact={}">View Portfolios</a>',
            url,
            obj.id,
        )

    view_investment.short_description = "Investments"

    def view_transactions(self, obj):
        url = reverse('admin:personal_actions_app_transaction_changelist')
        return format_html(
            '<a href="{}?user__id__exact={}">View Transactions</a>',
            url,
            obj.id,
        )

    view_transactions.short_description = "Transactions"

    def view_equal_installment_plans(self, obj):
        url = reverse('admin:repayment_plans_app_equalinstallmentplan_changelist')
        return format_html(
            '<a href="{}?user__id__exact={}">View Plans</a>',
            url,
            obj.id,
        )

    view_equal_installment_plans.short_description = "Equal Install Plans"

    def view_equal_principal_portion_plans(self, obj):
        url = reverse('admin:repayment_plans_app_equalprincipalportionplan_changelist')
        return format_html(
            '<a href="{}?user__id__exact={}">View Plans</a>',
            url,
            obj.id,
        )

    view_equal_principal_portion_plans.short_description = "Equal Principal Portion Plans"

    def view_equal_installment_changeable_ip_plans(self, obj):
        url = reverse('admin:repayment_plans_app_equalinstallmentchangeableipplan_changelist')
        return format_html(
            '<a href="{}?user__id__exact={}">View Plans</a>',
            url,
            obj.id,
        )

    view_equal_installment_changeable_ip_plans.short_description = "Equal Installment With Changeable Interest Rate Plans"