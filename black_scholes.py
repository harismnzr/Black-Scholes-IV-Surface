# calculating both d1 and d2 in d1_d2()
def d1_d2(S, X, T, r, vol):
    d1 = (np.log(S/X) + (r + 0.5 * vol**2)*T) / (vol * np.sqrt(T))
    d2 = d1 - (vol * np.sqrt(T))
    return d1, d2

# pricing call options
def bs_call(S, X, T, r, vol):
    d1 = d1_d2(S, X, T, r, vol)[0]
    d2 = d1_d2(S, X, T, r, vol)[1]
    discount = np.exp(-r * T)
    C = S * norm.cdf(d1) - X * discount * norm.cdf(d2)
    return C

# pricing put options
def bs_put(S, X, T, r, vol):
    d1 = d1_d2(S, X, T, r, vol)[0]
    d2 = d1_d2(S, X, T, r, vol)[1]
    discount = np.exp(-r * T)
    P = X* discount * norm.cdf(-d2) - S * norm.cdf(-d1)
    return P
