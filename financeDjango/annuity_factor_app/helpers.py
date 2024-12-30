def calculate_future_value_annuity_factor_end_year_payment(r, n):
    """
        Calculate the future value annuity factor for a given interest rate and number of periods when payment is at the end of the
        calendar year.

        Args:
            r (float): The interest rate per period (e.g., 0.1 for 10).
            n (int): The number of periods.

        Returns:
            float: The annuity factor rounded to three decimal places.
    """
    fv_af = ((1 + r)**n - 1) / r
    return round(fv_af, 3)


def calculate_future_value_annuity_factor_start_year_payment(r, n):
    """
        Calculate the future value annuity factor for a given interest rate and number of periods when the payment is at the beginning
        of the calendar year.

        Args:
            r (float): The interest rate per period ( 0.1 for 10%).
            n (int): The number of periods.

        Returns:
            float: The annuity factor rounded to three decimal places.
        """
    fv_af = (((1 + r)**(n + 1) - 1) / r) - 1
    return round(fv_af, 3)

def calculate_present_value_annuity_factor_start_year_payment(r, n):
    """
    Calculate the present value annuity factor for a given interest rate and number of periods when the payment is at the beginning
    of the calendar year.

    Args:
        r (float): The interest rate per period ( 0.1 for 10%).
        n (int): The number of periods.

    Returns:
        float: The annuity factor rounded to three decimal places.
    """
    pv_af = (((1 + r)**(n - 1) - 1) / r * (1 + r)**(n - 1)) + 1
    return round(pv_af, 3)

def calculate_present_value_annuity_factor_end_year_payment(r, n):
    """
    Calculate the present value annuity factor for a given interest rate and number of periods when payment is at the end of the
    calendar year.

    Args:
        r (float): The interest rate per period (e.g., 0.1 for 10).
        n (int): The number of periods.

    Returns:
        float: The annuity factor rounded to three decimal places.

    Example:
        #>>> calculate_annuity_factor(0.1, 4)
        3.17
    """
    af = round(1/r * (1 - 1/(1 + r)**n), 3)
    return af
