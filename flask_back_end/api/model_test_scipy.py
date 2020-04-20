from scipy.integrate import ode
import numpy as np
from matplotlib import pyplot as plt

def dy_dt(t, y):
	#print statements, set itota, itots
	qqq='SEIiUCRD'
	print("===timestep=%i,pop=%f" % (t,sum(y)))

	Itot_a = 0
	Itot_s = 0

	for i in range(0, 10):
		Itot_a += y[i * 8 + 2]
		Itot_s += y[i * 8 + 3]

	for i in range(0, 10):
		y[i * 8 + 0] = -pars_beta_a * y[i * 8 + 0] * Itot_a - pars_beta_s * y[i * 8 + 0] * Itot_s
		y[i * 8 + 1] = pars_beta_a * y[i * 8 + 0] * Itot_a + pars_beta_s * y[i * 8 + 0] * Itot_s - pars_gamma_e * y[i * 8 + 1]
		y[i * 8 + 2] = pars_p[i] * pars_gamma_e * y[i * 8 + 1] - pars_gamma_a * y[i * 8 + 2]
		y[i * 8 + 3] = (1 - pars_p[i]) * pars_gamma_e * y[i * 8 + 1] - pars_gamma_s * y[i * 8 + 3]
		y[i * 8 + 4] = agepars_hosp_frac[i] * (1 - agepars_hosp_crit[i]) * pars_gamma_s * y[i * 8 + 3] - pars_gamma_h * y[i * 8 + 4]
		y[i * 8 + 5] = agepars_hosp_frac[i] * agepars_hosp_crit[i] * pars_gamma_s * y[i * 8 + 3] - pars_gamma_h * y[i * 8 + 5]
		y[i * 8 + 6] = pars_gamma_a * y[i * 8 + 2] + (1 - agepars_hosp_frac[i]) * pars_gamma_s * y[i * 8 + 3] + pars_gamma_h * y[i * 8 + 4] + (1 - agepars_crit_die[i]) * pars_gamma_h * y[i * 8 + 5]
		y[i * 8 + 7] = agepars_crit_die[i] * pars_gamma_h * y[i * 8 + 5]
	return y

###=====================
agepars_meanage_in=np.arange(5,95,10)
agepars_highage=np.arange(9,99,10)
agepars_lowage=np.arange(0,90,10)
#Data from 2018 census
population_N= 10666108
population_agefrac_in = [0.126,0.137,0.139,0.132,0.130,0.129,0.104,0.061,0.036,0.007]
myInt = sum(population_agefrac_in)
population_agefrac = [x / myInt for x in population_agefrac_in]
agepars_meanage= [a * b for a, b in zip(agepars_meanage_in, population_agefrac)]
population_meanage = sum(agepars_meanage)
# Check if population data sums to ~1.00
# In[6]:
# x = (sum(population_agefrac))
# y = format(x,'.5f')
# yy = format(1,'.5f')
# bool(y==yy)
# Basic parameters
pars_gamma_e=1/4;	#Transition to infectiousness
pars_gamma_a=1/6;	#Resolution rate for asymptomatic
pars_gamma_s=1/6;	#Resolution rate for symptomatic
pars_gamma_h=1/10;	#Resolution rate in hospitals
pars_beta_a=4/10;	#Transmission for asymptomatic
pars_beta_s=8/10;	#Transmission for symptomatic
pars_p=[0.95,0.95,0.90,0.8,0.7,0.6,0.4,0.2,0.2,0.2]			#Fraction asymptomatic
pars_Itrigger = 500000/population_N #Trigger at 5000 total cases, irrespective of type
# Age stratification
agepars_hosp_frac_in=[0.1,0.3,1.2,3.2,4.9,10.2,16.6,24.3,27.3,27.3]
agepars_hosp_frac = [x / 100 for x in agepars_hosp_frac_in]
agepars_hosp_crit_in=[5,5,5,5,6.3,12.2,27.4,43.2,70.9,70.9]
agepars_hosp_crit = [x / 100 for x in agepars_hosp_crit_in]
agepars_crit_die= 0.5*np.ones(len(agepars_meanage)+1) ## CHECK
agepars_num_ages = len(agepars_meanage);

N=agepars_num_ages;
agepars_S_ids= (1,N)
agepars_E_ids= ((N+1),(2*N))
agepars_Ia_ids=((2*N+1),(3*N))
agepars_Is_ids=((3*N+1),(4*N))
agepars_Ihsub_ids=((4*N+1),(5*N))
agepars_Ihcri_ids=((5*N+1),(6*N))
agepars_R_ids=((6*N+1),(7*N))
agepars_D_ids=((7*N+1),(8*N))
agepars_Hcum_ids=((8*N+1),(9*N))
agepars_IFR_2= [a * b * c * d for a, b, c, d in zip(population_agefrac, agepars_hosp_frac, agepars_hosp_crit, agepars_crit_die)]
pp = [a-b for a, b in zip(np.ones(len(pars_p)), pars_p)]
agepars_IFR_1= [a*b for a,b in zip(agepars_IFR_2,pp)]
agepars_IFR = sum(agepars_IFR_1)

# Epidemiological parameters
pars_Ra=pars_beta_a/pars_gamma_a;
pars_Rs=pars_beta_s/pars_gamma_s;

x = [a-b for a, b in zip(np.ones(len(pars_p)), pars_p)] #1-pars_p
y = [a*b for a,b in zip(x,population_agefrac)] #(1-pars_p*pop_agefrac)
z = [a*pars_Rs for a in y] #(1-pars_p*pop_agefrac*pars_Rs)
m = [a*b*pars_Ra for a,b in zip(pars_p,population_agefrac)] #(pars_p*pop_agefrac*pars_Ra)

pars_R0 = [a*b for a,b in zip(z,m)]

outbreak_pTime=365;
outbreak_pNear=30;
outbreak_pshift=0;

ga_cases  = [552,620,800,1097,1387,1643,2198]
ga_hosp =  [186,240,361,438,509,607,660]
ga_death = [25,25,38,47,56,65,79]
y0=np.zeros(80)
population_N= 10666108

#initial conditions: one person 10-19 is sick
y0[0:10]=np.multiply(population_agefrac,population_N-8025)
y0[11]=1
y0[1]-=1

# y0=np.divide(y0,population_N)

y0 = np.zeros(80)

for i in range(0, 10):
	y0[i*8+2] = 7500 * population_agefrac[i]
	y0[i*8+3] = 500 * population_agefrac[i]
	y0[i*8+7] = 25 * population_agefrac[i]
	y0[i*8] = population_agefrac[i] * population_N - y0[i*8+3] - y0[i*8+4] - y0[i*8+7]

tspan = list(range(0,outbreak_pTime,1))
r = ode(dy_dt).set_integrator('vode', method='adams')
r.set_initial_value(y0, 0)
t1 = 10
dt = 1

y = np.zeros([80,10])
t = np.zeros([80,10])

count = 0

while r.successful() and r.t < t1:
	r.integrate(r.t+dt)
	y[:,count] = r.y
	t[:,count] = r.t
	count+=1

plt.plot(t, y)
plt.show()