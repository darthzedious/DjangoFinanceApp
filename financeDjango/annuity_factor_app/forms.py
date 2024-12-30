from django import forms


class AnnuityFactorForm(forms.Form):

    interest_rate = forms.DecimalField(
        min_value=0.0001,
        required=True,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Interest rate (e.g., 0.1 for 10%).',
            }
        ),
    )

    number_of_periods = forms.IntegerField(
        min_value=1,
        required=True,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter number of periods (e.g., 10).',
            }
        ),
    )

