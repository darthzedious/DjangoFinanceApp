from django import forms


class DiscountFactorForm(forms.Form):
    interest_rate = forms.DecimalField(
        required=True,
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Interest rate e.g. 0.05...',
        }),
        help_text='Enter the interest rate.',
    )

    number_of_periods = forms.IntegerField(
        required=True,
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Number of periods e.g. 3...',
        }),
        help_text='Enter the number of periods.',
    )

class DiscountPresentValueForm(DiscountFactorForm):
    future_value = forms.DecimalField(
        required=True,
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Future value e.g. 100',
        }),
        help_text='Enter the future value.',
    )