from django import forms

from financeDjango.mixins import DisabledReadonlyMixin
from financeDjango.repayment_plans_app.models import EqualInstallmentPlan, EqualPrincipalPortionPlan, \
    EqualInstallmentChangeableIPPlan, EqualPrincipalPortionChangeableIPPlan



class BaseEqualCPPForm(forms.ModelForm):
    class Meta:
        fields = ['borrowed_amount', 'interest_rate', 'periods']
        widgets = {
            'borrowed_amount': forms.NumberInput(attrs={
                'step': '0.01',
                'class': 'form-control',
                'placeholder': 'The amount borrowed. e.g. 31700',
            }),
            'interest_rate': forms.NumberInput(attrs={
                'step': '0.01',
                'class': 'form-control',
                'placeholder': 'Interest rate per period (e.g., 0.1 for 10%)',
            }),
            'periods': forms.NumberInput(attrs={
                'min': 1,
                'class': 'form-control',
                'placeholder': 'Number of periods e.g. 4...',
            }),
        }

class EqualInstallmentForm(BaseEqualCPPForm):
    class Meta(BaseEqualCPPForm.Meta):
        model = EqualInstallmentPlan

class EqualInstallmentEditForm(EqualInstallmentForm):
    pass

class EqualInstallmentDeleteForm(DisabledReadonlyMixin, EqualInstallmentForm):
    pass


class EqualPrincipalPortionForm(BaseEqualCPPForm):
    class Meta(BaseEqualCPPForm.Meta):
        model = EqualPrincipalPortionPlan

class EqualPrincipalPortionEditForm(EqualPrincipalPortionForm):
    pass

class EqualPrincipalPortionDeleteForm(DisabledReadonlyMixin, EqualPrincipalPortionForm):
    pass



class BaseChangeableIPForm(forms.ModelForm):
    class Meta:
        fields = ['borrowed_amount', 'interest_rate_first_period', 'interest_rate_second_period', 'first_period', 'second_period']
        widgets = {
            'borrowed_amount': forms.NumberInput(attrs={
                'step': '0.01',
                'class': 'form-control',
                'placeholder': 'The amount borrowed. e.g. 31700',
            }),
            'interest_rate_first_period': forms.NumberInput(attrs={
                'step': '0.01',
                'class': 'form-control',
                'placeholder': 'Interest rate for period (e.g., 0.1 for 10%)',
            }),
            'interest_rate_second_period': forms.NumberInput(attrs={
                'step': '0.01',
                'class': 'form-control',
                'placeholder': 'Interest rate for period (e.g., 0.1 for 10%)',
            }),
            'first_period': forms.NumberInput(attrs={
                'step': '0.01',
                'class': 'form-control',
                'placeholder': 'First repayment periods (e.g., 4)',
            }),
            'second_period': forms.NumberInput(attrs={
                'step': '0.01',
                'class': 'form-control',
                'placeholder': 'Second repayment periods (e.g., 2)',
            })
        }

class EqualInstallmentChangeableIPForm(BaseChangeableIPForm):
    class Meta(BaseChangeableIPForm.Meta):
        model = EqualInstallmentChangeableIPPlan

class EqualInstallmentChangeableIPEditForm(EqualInstallmentChangeableIPForm):
    pass

class EqualInstallmentChangeableIPDeleteForm(DisabledReadonlyMixin, EqualInstallmentChangeableIPForm):
    pass

class EqualPrincipalPortionChangeableIPForm(BaseChangeableIPForm):
    class Meta(BaseChangeableIPForm.Meta):
        model = EqualPrincipalPortionChangeableIPPlan

class EqualPrincipalPortionChangeableIPEditForm(EqualPrincipalPortionChangeableIPForm):
    pass

class EqualPrincipalPortionChangeableIPDeleteForm(DisabledReadonlyMixin, EqualPrincipalPortionChangeableIPForm):
    pass
