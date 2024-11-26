from django import forms

from financeDjango.repayment_plans_app.models import EqualInstallmentPlan


class RepaymentPlanForm(forms.ModelForm):
    class Meta:
        model = EqualInstallmentPlan
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
        },