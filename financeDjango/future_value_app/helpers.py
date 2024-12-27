def future_value_simple_interest(pv, r, n):
    """
       Calculate the future value of an investment using simple interest.

       Args:
           pv (float): The present value or initial investment amount.
           r (float): The annual interest rate (as a decimal, e.g., 0.05 for 5%).
           n (float): The time period in years.

       Returns:
           float: The future value of the investment, rounded to three decimal places.
       """

    fv = pv * (1 + r * n)
    return round(fv, 3)

def future_value_compound_interest(pv, r, n):
    """
       Calculate the future value of an investment using compound interest.

       Args:
           pv (float): The present value or initial investment amount.
           r (float): The annual interest rate (as a decimal, e.g., 0.05 for 5%).
           n (float): The time period in years.

       Returns:
           float: The future value of the investment, rounded to three decimal places.
       """

    fv = pv * (1 + r) **n
    return round(fv, 3)