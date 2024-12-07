def calculate_present_value_annuity_factor_end_year_payment(r, n):
    """
    Args:
        r (float): The interest rate per period (e.g., 0.1 for 10).
        n (int): The number of periods.
    Example:
        3.17
    """
    af = round(1/r * (1 - 1/(1 + r)**n), 3)
    return af

def calculate_equal_installment(borrowed_amount, r, n):
    annuity_factor = calculate_present_value_annuity_factor_end_year_payment(r, n)
    installment = borrowed_amount / annuity_factor
    repayment_plan = []

    rp = borrowed_amount
    for i in range(1, n + 1):
        ip = rp * r
        pp = installment - ip
        rp -= pp
        repayment_plan.append({
            "n": i,
            "C": round(installment, 2),
            "IP": round(ip, 2),
            "PP": round(pp, 2),
            "RP": round(rp, 2),
        })

    return repayment_plan  # List of dictionaries

def calculate_equal_principle_portion(borrowed_amount, r, n):
    repayment_plan = []

    pp = borrowed_amount / n
    rp = borrowed_amount

    for i in range(1, n + 1):
        ip = rp * r
        installment = pp + ip
        rp -= pp
        repayment_plan.append({
            "n": i,
            "C": round(installment, 2),
            "IP": round(ip, 2),
            "PP": round(pp, 2),
            "RP": round(rp, 2),
        })

    return repayment_plan

def calculate_equal_installment_changeable_ip_repayment_plan(borrowed_amount, r1, r2, n1, n2):
    repayment_plan = []
    annuity_factor = calculate_present_value_annuity_factor_end_year_payment(r1, n1)
    installment = borrowed_amount / annuity_factor
    rp = borrowed_amount

    for i in range(1, n1 + 1):
        ip = rp * r1
        pp = installment - ip
        rp -= pp
        repayment_plan.append(
            {"n": i,
             "C": round(installment, 2),
             "IP": round(ip, 2),
             "PP": round(pp, 2),
             "RP": round(rp, 2),
             })

        if i == n2:
            break

    annuity_factor = calculate_present_value_annuity_factor_end_year_payment(r2, n2)
    installment = rp / annuity_factor

    for i in range(n2 + 1, n1 + 1):
        ip = rp * r2
        pp = installment - ip
        rp -= pp
        repayment_plan.append(
            {"n": i, "C": round(installment, 2),
             "IP": round(ip, 2),
             "PP": round(pp, 2),
             "RP": round(rp, 2),
             })

    return repayment_plan


def calculate_equal_principle_portion_changeable_ip_repayment_plan(borrowed_amount, r1, r2, n1, n2):
    repayment_plan = []

    pp = borrowed_amount / n1
    rp = borrowed_amount

    for i in range(1, n1 + 1):
        if i == n2:
            break
        ip = rp * r1
        installment = pp + ip
        rp -= pp
        repayment_plan.append(
            {"n": i,
             "C": round(installment, 2),
             "IP": round(ip, 2),
             "PP": round(pp, 2),
             "RP": round(rp, 2)
             })

    for i in range(n2, n1 + 1):
        ip = rp * r2
        installment = pp + ip
        rp -= pp
        repayment_plan.append(
            {"n": i,
             "C": round(installment, 2),
             "IP": round(ip, 2),
             "PP": round(pp, 2),
             "RP": round(rp, 2),
             })

    return repayment_plan