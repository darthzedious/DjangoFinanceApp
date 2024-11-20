from django import forms
from django.core.exceptions import ValidationError


class BaseSharesForm(forms.Form):
    dividends = forms.DecimalField(
        required=True,
        label='',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Dividends',
        }),
        help_text='Enter the dividend of the preference share.',
    )

    rate_of_return = forms.DecimalField(
        required=True,
        label='',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter rate of return (e.g., 0.08)',
        }),
        help_text='Enter the required rate of return (as a decimal, e.g., 0.08 for 8%).',
    )

class BaseROEGrowthRateForm(forms.Form):
    net_profit = forms.DecimalField(
        required=True,
        label='',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Net profit',
        }),
        help_text='Enter the net profit of the company',
    )

    equity_capital= forms.DecimalField(
        required=True,
        label='',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Equity capital ',
        }),
        help_text='Enter the equity capital of the company',
    )

    def clean_equity_capital(self):
        equity_capital = self.cleaned_data.get('equity_capital')
        if equity_capital == 0.0:
            raise ValidationError('Equity capital cannot be zero.')
        return equity_capital


class PreferencesSharesForm(BaseSharesForm):
   def clean_rate_of_return(self):
       rate_of_return = self.cleaned_data.get('rate_of_return')
       if rate_of_return == 0.0:
           raise ValidationError("Rate of return cannot be zero.")
       return rate_of_return


class OrdinarySharesForm(BaseSharesForm):
    growth_rate = forms.DecimalField(
        required=True,
        label='',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Growth rate',
        }),
        help_text='Enter the growth rate of dividends (as a decimal, e.g., 0.02 for 2%)',
    )

    def clean(self):
        cleaned_data = super().clean()
        rate_of_return = cleaned_data.get('rate_of_return')
        growth_rate = cleaned_data.get('growth_rate')

        if rate_of_return is not None and growth_rate is not None:
            if rate_of_return <= growth_rate:
                raise ValidationError("The required rate of return must be greater than the growth rate.")

        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['dividends'].widget.attrs['placeholder'] = 'Expected dividend'
        self.fields['dividends'].help_text = 'Enter the expected dividend for the next period'
        self.fields['rate_of_return'].help_text = ('Enter the required rate of return (as a decimal, e.g., 0.08 for 8%;<br>'
                                                   'The required rate of return must be greater than the growth rate.)')


class ReturnOnEquityForm(BaseROEGrowthRateForm):
    pass


class GrowthRateOfDividendsForm(BaseROEGrowthRateForm):
    retention_ratio = forms.DecimalField(
        required=True,
        label='',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Retention ratio',
        }),
        help_text='Enter the Retention Ratio (Ki) of the company',
    )

class CAPMForm(forms.Form):
    risk_free_rate = forms.DecimalField(
        required=True,
        label = '',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Risk-free rate (e.g., 0.03 for 3%)',
        }),
        help_text='Enter the Risk-free rate of the company',
    )

    market_return = forms.DecimalField(
        required=True,
        label='',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Market return (e.g., 0.08 for 8%)',
        }),
        help_text='Enter the market return of the company',
    )

    beta_coefficient = forms.DecimalField(
        required=True,
        label ='',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Beta coefficient (e.g., 1.2)',
        }),
        help_text='Enter the beta coefficient of the company',
    )
