from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
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
    list_display = ('username', 'email')

    list_display = ('pk', 'email', 'is_staff', 'is_superuser', 'view_budgets',)
    search_fields = ('email',)
    ordering = ('pk',)
    list_filter = ('is_staff', 'is_superuser', 'is_active',)

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
        return format_html(
            '<a href="/admin/personal_actions_app/budget/?user__id__exact={}">View Budgets</a>',
            obj.id
        )

    view_budgets.short_description = "Budgets"
