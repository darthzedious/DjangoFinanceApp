def calculate_preference_shares_price(dividends, rate_of_return):
    return dividends / rate_of_return

def calculate_ordinary_shares_price(dividends, rate_of_return, growth_rate):
    return round(dividends / (rate_of_return - growth_rate), 2)

def calculate_return_on_equity(net_profit, equity_capital):
    return round(net_profit / equity_capital, 4)


def calculate_growth_rate_of_dividends(net_profit, equity_capital, ki):
    roe = calculate_return_on_equity(net_profit, equity_capital)
    return round(roe * (1 - ki), 4)

def calculate_cpam(risk_free_rate, market_return, beta_coefficient):
    return risk_free_rate + beta_coefficient * (market_return - risk_free_rate)
