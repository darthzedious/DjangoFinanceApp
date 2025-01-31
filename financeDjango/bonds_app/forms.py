from django import forms

class BaseBondsPriceForm(forms.Form):
    number_of_periods = forms.DecimalField(
        required=True,
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'The number of periods until maturity (e.g. 3).'
        })
    )

    nominal = forms.DecimalField(
        required=True,
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'The Nominal value of the bond (e.g. 100).'
        })
    )

    yield_to_maturity = forms.DecimalField(
        required=True,
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'The yield to maturity (as a decimal, e.g., 0.05 for 5%).'
        })
    )


class BaseBondsYieldToMaturityForm(forms.Form):
    nominal = forms.DecimalField(
        required=True,
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'The value of the bond (e.g. 100).'
        })
    )

    present_value = forms.DecimalField(
        required=True,
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'The current price of the bond (e.g. 793,83).'
        })
    )

    number_of_periods=forms.DecimalField(
        required=True,
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'The number of periods until maturity (e.g. 3).'
        })
    )


class ZeroCouponBondYieldToMaturityForm(BaseBondsYieldToMaturityForm):
    pass


class CouponBondYieldToMaturityForm(BaseBondsYieldToMaturityForm):
    payment_period = forms.DecimalField(
        required=False,
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'If provided, indicates the payment period (e.g., 6 for semi-annual).'
        })
    )

    coupon_rate = forms.DecimalField(
        required=True,
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Annual coupon rate (e.g., 0.05 for 5%).',
        })
    )

class ZeroCouponBondPriceForm(BaseBondsPriceForm):
    pass

class CouponBondPriceForm(BaseBondsPriceForm):
    coupon_rate = forms.DecimalField(
        required=True,
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'The coupon rate (as a decimal, e.g., 0.05 for 5%).',
        })
    )