def implied_vol(price, S, X, T, r, option_type):

# storing the option type
    if option_type == "call":
        bs_option = bs_call
        no_arbitrage_lb = S - X * np.exp(-r * T) # setting no-arbitrage lower bound for call option type
    elif option_type == "put":
        bs_option = bs_put
        no_arbitrage_lb = X * np.exp(-r * T) - S # setting no-arbitrage lower bound for put option type
    else:
        raise ValueError("option_type must be 'call' or 'put'")

# nan checks:
    if price < max(no_arbitrage_lb, 0):  # returning nan if the market price of the option is below the no-arbitrage lower bound
        return np.nan

    low, high = 0.001, 5  # setting the bracket to execute bisection solver

    if price > bs_option(S, X, T, r, high) or price < bs_option(S, X, T, r, low): # returning nan if the market price of the option is above the price at vol=5 (upper cut-off of the bracket since vols of 500% are well above what would actually occur) or below the price at vol=0.001
        return np.nan

    if np.isnan(price):  # returning nan if a quote is missing for price
        return np.nan

# bisection solver loop:
    for _ in range(100):
        mid = (low+high)/2
        est_price = bs_option(S, X, T, r, mid)
        if est_price < price:
            low = mid
        else:
            high = mid

    return (low + high)/2
