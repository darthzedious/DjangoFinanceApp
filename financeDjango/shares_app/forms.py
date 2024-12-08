from django import forms
from django.core.exceptions import ValidationError


class BaseSharesForm(forms.Form):
    dividends = forms.DecimalField(
        required=True,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter dividends (e.g., 250)',
        }),
    )

    rate_of_return = forms.DecimalField(
        required=True,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter rate of return (e.g., 0.08)',
        }),
    )

class BaseROEGrowthRateForm(forms.Form):
    net_profit = forms.DecimalField(
        required=True,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Net profit (e.g., 500000.00)',
        }),
    )

    equity_capital= forms.DecimalField(
        required=True,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Equity capital (e.g., 2500000.00)',
        }),
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
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter the growth rate of dividends (as a decimal, e.g., 0.02 for 2%)',
        }),
    )

    def clean(self):
        cleaned_data = super().clean()
        rate_of_return = cleaned_data.get('rate_of_return')
        growth_rate = cleaned_data.get('growth_rate')

        if rate_of_return is not None and growth_rate is not None:
            if rate_of_return <= growth_rate:
                raise ValidationError("The required rate of return must be greater than the growth rate.")

        return cleaned_data


class ReturnOnEquityForm(BaseROEGrowthRateForm):
    pass


class GrowthRateOfDividendsForm(BaseROEGrowthRateForm):
    retention_ratio = forms.DecimalField(
        required=True,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter the Retention Ratio (Ki e.g., 0.4)',
        }),
    )


class CAPMForm(forms.Form):
    risk_free_rate = forms.DecimalField(
        required=True,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Risk-free rate (e.g., 0.03 for 3%)',
        }),
    )

    market_return = forms.DecimalField(
        required=True,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Market return (e.g., 0.08 for 8%)',
        }),
    )

    beta_coefficient = forms.DecimalField(
        required=True,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Beta coefficient (e.g., 1.2)',
        }),
    )
