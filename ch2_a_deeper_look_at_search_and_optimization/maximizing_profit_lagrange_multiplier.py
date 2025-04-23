import sympy as sym

# x = number of physical tickets sold
# y = number of virtual tickets sold
x, y = sym.symbols('x y', positive=True)

f = 155 * x + (0.001 * x**sym.Rational(3,2) + 70) * y - 1000000

# Constraint (max number of tickets: 10000)
g = x + y - 10000

lambda_ = sym.symbols('lambda')

Lagrange = f - lambda_ * g

eqs = [sym.diff(Lagrange, x), sym.diff(Lagrange, y), g]

sol = sym.solve(eqs,  [x, y, lambda_], dict=True)

assert len(sol) == 1, "There should be only one solution"

profit = [f.subs(p) for p in sol]

sol = sol[0]

print(f"Optimal numer of physical tickets sold: x = {sol[x]:.1f}")
print(f"Optimal numer of virtual tickets sold: y = {sol[y]:.1f}")
print(f"Expected profit: f(x,y) = {profit[0]:.2f}")
