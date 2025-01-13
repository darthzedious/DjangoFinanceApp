def zero_coupon_bond_yield_to_maturity(n, N, po):
    """
    Calculate the yield to maturity (YTM) for a zero-coupon bond.

    Args:
        Nominal (float) N: The value of the bond.
        Present value (float) po: The current price of the bond.
        periods (int) n: The number of periods until maturity.

    Returns:
        float: The yield to maturity (YTM) as a decimal (e.g., 0.05 for 5%).
    """

    r = (N / po) ** (1 / n) - 1
    return round(r, 3)