def future_value_simple_interest(pv, r, n):
    fv = pv * (1 + r * n)
    return round(fv, 3)

def future_value_compound_interest(pv, r, n):
    fv = pv * (1 + r) **n
    return round(fv, 3)