#=
test_model:
- Julia version: Unknown
- Author: arosado
- Date: 2020-04-19
=#

using DifferentialEquations

f(u, p, t) = 1.01*u
u0 = 1/2
tspan = (0.0, 1.0)
prob = ODEProblem(f, u0, tspan)
sol = solve(prob, Tsit5(), reltol=1e-8, abstol=1e-8)

using Plots
plot(sol, linewidth=5, title="Solution", xaxis="Time (t)", yaxis="u(t)")

plot!(sol.t, t->0.5*exp(1.01t), lw=3, ls=:dash,label="True Solution!")