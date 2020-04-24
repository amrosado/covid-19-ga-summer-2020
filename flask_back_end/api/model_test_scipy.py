from scipy.integrate import ode
import numpy as np
from matplotlib import pyplot as plt

params = {}

params['age_group_n'] = 10

params['gamma_e'] = 1./4
params['gamma_a'] = 1./6
params['gamma_s'] = 1./10
params['gamma_h'] = 4./10
params['beta_a'] = 4./10
params['beta_s'] = 8./10

params['pop_asymptomatic'] = np.array([0.95,0.95,0.90,0.8,0.7,0.6,0.4,0.2,0.2,0.2])
params['pop_asymptomatic'] = params['pop_asymptomatic'] / np.sum(params['pop_asymptomatic'])

params['hosp_frac'] = np.array([0.1,0.3,1.2,3.2,4.9,10.2,16.6,24.3,27.3,27.3])
params['hosp_frac'] = params['hosp_frac'] / np.sum(params['hosp_frac'])

params['hosp_crit'] = np.array([5,5,5,5,6.3,12.2,27.4,43.2,70.9,70.9])
params['hosp_crit'] = params['hosp_crit'] / np.sum(params['hosp_crit'])

params['crit_die'] = np.array(np.ones(10)*0.5)

def dy_dt(t, y, params):
	Itot_a = 0
	Itot_s = 0

	dydt = np.zeros(params['age_group_n']*8)

	Itot_a += y[20:30]
	Itot_s += y[30:40]

	for i in range(0, 10):
		dydt[:10] = -params['beta_a'] * y[:10] * Itot_a - params['beta_s'] * y[:10] * Itot_s
		dydt[10:20] = params['beta_a'] * y[:10] * Itot_a + params['beta_s'] * y[:10] * Itot_s - params['gamma_e'] * y[10:20]
		dydt[20:30] = params['pop_asymptomatic'][i] * params['gamma_e'] * y[10:20] - params['gamma_a'] * y[20:30]
		dydt[30:40] = (1 - params['pop_asymptomatic'][i]) * params['gamma_e'] * y[10:20] - params['gamma_s'] * y[30:40]
		dydt[40:50] = params['hosp_frac'][i] * (1 - params['hosp_crit'][i]) * params['gamma_s'] * y[30:40] - params['gamma_h'] * y[40:50]
		dydt[50:60] = params['hosp_frac'][i] * params['hosp_crit'][i] * params['gamma_s'] * y[30:40] - params['gamma_h'] * y[50:60]
		dydt[60:70] = params['gamma_a'] * y[20:30] + (1 -  params['hosp_frac'][i]) * params['gamma_s'] * y[30:40] + params['gamma_h'] * y[40:50] + (1 - params['crit_die'][i]) * params['gamma_h'] * y[50:60]
		dydt[70:80] = params['crit_die'][i] * params['gamma_h'] * y[50:60]

	return dydt

population_N= 10666108
population_agefrac = [0.126,0.137,0.139,0.132,0.130,0.129,0.104,0.061,0.036,0.007]

pars_Itrigger = 500000/population_N #Trigger at 5000 total cases, irrespective of type

outbreak_pTime=365;
outbreak_pNear=30;
outbreak_pshift=0;

ga_cases  = [552,620,800,1097,1387,1643,2198]
ga_hosp =  [186,240,361,438,509,607,660]
ga_death = [25,25,38,47,56,65,79]
y0=np.zeros(80)
population_N= 10666108

#initial conditions: one person 10-19 is sick
y0[0:10]=population_agefrac
y0[11]+=population_agefrac[1] * (1 / population_N)
y0[1]-=population_agefrac[1] * (1 / population_N)

tspan = list(range(0,outbreak_pTime,1))
r = ode(dy_dt).set_integrator('vode', method='adams')
r.set_initial_value(y0, 0).set_f_params(params)
t1 = 10
dt = 1

y = np.zeros([80,10])
t = np.zeros(10)

count = 0

while r.successful() and r.t < t1:
	r.integrate(r.t+dt)
	y[:,count] = r.y
	t[count] = r.t
	count+=1

plt.plot(t, y[50:60:])
plt.legend()
plt.show()