def calculate_preference_shares_price(dividends, rate_of_return):
    """
        Calculate the price of preference shares.

        Args:
            dividends (float): The fixed dividend paid by the preference share.
            rate_of_return (float): The required rate of return (as a decimal, e.g., 0.08 for 8%).

        Returns:
            float: The price of the preference share.
        """
    return dividends / rate_of_return

def calculate_ordinary_shares_price(dividends, rate_of_return, growth_rate):
    """
           Calculate the price of ordinary shares using the Gordon Growth Model.

           Args:
               dividends (float): The expected dividend in the next period.
               rate_of_return(float): The required rate of return (as a decimal, e.g., 0.08 for 8%).
               growth_rate (float): The growth rate of dividends (as a decimal, e.g., 0.02 for 2%).

           Returns:
               float: The estimated price of the ordinary share.
           """
    return round(dividends / (rate_of_return - growth_rate), 2)

def calculate_return_on_equity(net_profit, equity_capital):
    """
        Calculate the return on equity (ROE).

        Args:
            net_profit (float): The net profit of the company.
            equity_capital (float): The total equity capital of the company.

        Returns:
            float: The return on equity (ROE) as a decimal.
        """
    return round(net_profit / equity_capital, 4)


def calculate_growth_rate_of_dividends(net_profit, equity_capital, ki):
    """
            Calculate the growth rate of dividends using the ROE and payout ratio.

            Args:
                net_profit (float): The net profit of the company.
                equity_capital (float): The equity capital of the company.
                ki (float): The payout ratio (as a decimal, e.g., 0.4 for 40%).

            Returns:
                float: The growth rate of dividends.
            """
    roe = calculate_return_on_equity(net_profit, equity_capital)
    return round(roe * (1 - ki), 4)

def calculate_cpam(risk_free_rate, market_return, beta_coefficient):
    """
        Calculate the expected return using the Capital Asset Pricing Model (CAPM).

        Args:
            risk_free_rate (float): The risk-free rate of return (as a decimal, e.g., 0.03 for 3%).
            market_return (float): The expected return of the market (as a decimal, e.g., 0.08 for 8%).
            beta_coefficient (float): The beta coefficient representing the asset's volatility relative to the market.

        Returns:
            float: The expected return of the asset based on CAPM.
        """
    return risk_free_rate + beta_coefficient * (market_return - risk_free_rate)

