from diffeqpy import de

# def covid_model_ga(dy, t, y, pars, agepars):
# 	pass

def f(u, p, t):
	return -u

u0 = 0.5
tspan = (0., 1.)
prob = de.ODEProblem(f, u0, tspan)
sol = de.solve(prob)

import matplotlib.pyplot as plt
plt.plot(sol.t, sol.u)
plt.show()