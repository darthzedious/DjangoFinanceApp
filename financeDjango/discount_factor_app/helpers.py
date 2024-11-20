def calculate_the_discount_factor(r, n):
    df = 1/(1 + r)**n
    return round(df, 3)

def discounting_present_value(fv, r, n):
    pv = fv / (1 + r)**n
    return round(pv, 3)
