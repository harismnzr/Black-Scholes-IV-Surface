# checking put-call parity

# set variables used to test
S = 100
X = 100
T = 1
r = 0.05
vol = 0.2

C = bs_call(S, X, T, r, vol)
P = bs_put(S, X, T, r, vol)
lhs = C - P
rhs = S - X * np.exp(-r * T)
print(lhs - rhs)
print(np.isclose(lhs, rhs))

# should output 0.0 then True
