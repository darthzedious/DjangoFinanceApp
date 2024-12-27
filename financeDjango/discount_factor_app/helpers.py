def calculate_the_discount_factor(r, n):
    """
       Calculate the discount factor for a given interest rate and time period.

       Args:
           r (float): The annual discount rate (as a decimal, e.g., 0.05 for 5%).
           n (float): The time period in years.

       Returns:
           float: The discount factor, rounded to three decimal places.
       """

    df = 1/(1 + r)**n
    return round(df, 3)

def discounting_present_value(fv, r, n):
    """
       Calculate the present value of a future amount using discounting.

       Args:
           fv (float): The future value or amount to be received.
           r (float): The annual discount rate (as a decimal, e.g., 0.05 for 5%).
           n (float): The time period in years.

       Returns:
           float: The present value, rounded to three decimal places.
       """

    pv = fv / (1 + r)**n
    return round(pv, 3)
