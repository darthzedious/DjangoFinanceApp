from django import forms


class FutureValueBaseForm(forms.Form):
    present_value = forms.DecimalField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Present value (e.g., 100)',
        }),
    )

    interest_rate = forms.DecimalField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Interest rate (e.g., 0.05)',
        }),
    )

    number_of_periods = forms.IntegerField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Number of periods (e.g., 3)',
        }),
    )