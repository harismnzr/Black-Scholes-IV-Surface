import numpy as np

from black_scholes import bs_call, bs_put

# checking put-call parity

# (S, X, T, r, vol): in-the-money, at-the-money, out-of-the-money, varied expiries
cases = [
    (100, 100, 1.0, 0.05, 0.20),
    (100, 90, 0.5, 0.03, 0.30),
    (50, 60, 2.0, 0.01, 0.15),
    (200, 150, 0.25, 0.04, 0.40),

for S, X, T, r, vol in cases:
  C = bs_call(S, X, T, r, vol)
  P = bs_put(S, X, T, r, vol)
  lhs = C - P
  rhs = S - X * np.exp(-r * T)
  assert abs(lhs - rhs) < 1e-10, f"Parity failed for {(S, X, T, r, vol)} : {lhs - rhs}"
print("Put-call parity holds for all cases")
