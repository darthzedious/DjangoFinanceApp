from django import forms


class FutureValueBaseForm(forms.Form):
    present_value = forms.DecimalField(
        required=True,
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Present value e.g 100...',
        }),
        help_text='Enter the present value.',
    )

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