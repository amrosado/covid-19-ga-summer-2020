import numpy as np
import matplotlib.pyplot as plt
import numba

from numba import jit

from diffeqpy import de
from datetime import datetime


# ## Parameters

# Population parameters

# In[5]:


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


x = (sum(population_agefrac))
y = format(x,'.5f')
yy = format(1,'.5f')
bool(y==yy)


# Basic parameters

# In[7]:


pars_gamma_e=1/4;	#Transition to infectiousness
pars_gamma_a=1/6;	#Resolution rate for asymptomatic
pars_gamma_s=1/6;	#Resolution rate for symptomatic
pars_gamma_h=1/10;	#Resolution rate in hospitals
pars_beta_a=4/10;	#Transmission for asymptomatic
pars_beta_s=8/10;	#Transmission for symptomatic

pars_p=[0.95,0.95,0.90,0.8,0.7,0.6,0.4,0.2,0.2,0.2]			#Fraction asymptomatic

pars_overall_p= sum([a * b for a, b in zip(pars_p, population_agefrac)])

pars_Itrigger = 500000/population_N #Trigger at 5000 total cases, irrespective of type


# Age stratification

# In[8]:


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

# In[9]:


pars_Ra=pars_beta_a/pars_gamma_a;
pars_Rs=pars_beta_s/pars_gamma_s;


x = [a-b for a, b in zip(np.ones(len(pars_p)), pars_p)] #1-pars_p
y = [a*b for a,b in zip(x,population_agefrac)] #(1-pars_p*pop_agefrac)
z = [a*pars_Rs for a in y] #(1-pars_p*pop_agefrac*pars_Rs)
m = [a*b*pars_Ra for a,b in zip(pars_p,population_agefrac)] #(pars_p*pop_agefrac*pars_Ra)
pars_R0 = [a*b for a,b in zip(z,m)]


#SEIaIS (open) and then I_ha I_hs and then R (open) and D (cumulative) age stratified

# Vector for each age group has structure - [agefrac (S), E, Ia, Is, Ihsub, Ihcrit, R, D, Hcum]
# Ages 9-19
outbreak_y0_9_19=([population_agefrac[0],0,0,0,0,0,0,0,0])
outbreak_y0_9_19=[a*population_N for a in outbreak_y0_9_19]
outbreak_y0_9_19=[a/population_N for a in outbreak_y0_9_19]


# Ages 19-29
outbreak_y0_19_29=([population_agefrac[1],0,0,0,0,0,0,0,0])
outbreak_y0_19_29=[a*population_N for a in outbreak_y0_19_29]
outbreak_y0_19_29[0] = outbreak_y0_19_29[0]-1
outbreak_y0_19_29[1]= 1
outbreak_y0_19_29=[a/population_N for a in outbreak_y0_19_29]

# Ages 29-39
outbreak_y0_29_39=([population_agefrac[2],0,0,0,0,0,0,0,0])
outbreak_y0_29_39=[a*population_N for a in outbreak_y0_29_39]
outbreak_y0_29_39=[a/population_N for a in outbreak_y0_29_39]

# Ages 39-49
outbreak_y0_39_49=([population_agefrac[3],0,0,0,0,0,0,0,0])
outbreak_y0_39_49=[a*population_N for a in outbreak_y0_39_49]
outbreak_y0_39_49=[a/population_N for a in outbreak_y0_39_49]

# Ages 49-59
outbreak_y0_49_59=([population_agefrac[4],0,0,0,0,0,0,0,0])
outbreak_y0_49_59=[a*population_N for a in outbreak_y0_49_59]
outbreak_y0_49_59=[a/population_N for a in outbreak_y0_49_59]

# Ages 59-69
outbreak_y0_59_69=([population_agefrac[5],0,0,0,0,0,0,0,0])
outbreak_y0_59_69=[a*population_N for a in outbreak_y0_59_69]
outbreak_y0_59_69=[a/population_N for a in outbreak_y0_59_69]

# Ages 69-79
outbreak_y0_69_79=([population_agefrac[6],0,0,0,0,0,0,0,0])
outbreak_y0_69_79=[a*population_N for a in outbreak_y0_69_79]
outbreak_y0_69_79=[a/population_N for a in outbreak_y0_69_79]

# Ages 79-89
outbreak_y0_79_89=([population_agefrac[7],0,0,0,0,0,0,0,0])
outbreak_y0_79_89=[a*population_N for a in outbreak_y0_79_89]
outbreak_y0_79_89=[a/population_N for a in outbreak_y0_79_89]

# Ages 89-99
outbreak_y0_89_99=([population_agefrac[8],0,0,0,0,0,0,0,0])
outbreak_y0_89_99=[a*population_N for a in outbreak_y0_89_99]
outbreak_y0_89_99=[a/population_N for a in outbreak_y0_89_99]

# ### Data and dates from GA survey - I am still fiddling with this

outbreak_pTime=365;
outbreak_pNear=30;
outbreak_pshift=0;


# In[42]:


# Set timings for plots
now = datetime.now()

#tickdates = [(now - outbreak_pTime),10,10]
now.strftime("%d/%m/%Y %H:%M:%S")
#tickdates.strftime("%d/%m/%Y %H:%M:%S")

# Through 3/28 - last 7 days
ga_cases  = [552,620,800,1097,1387,1643,2198]
ga_hosp =  [186,240,361,438,509,607,660]
ga_death = [25,25,38,47,56,65,79]
#ga_date = [(now-6),now]

u0=np.zeros([10,8])
population_N= 10666108
population_agefrac_in = np.array([0.126,0.137,0.139,0.132,0.130,0.129,0.104,0.061,0.036,0.007])
population_agefrac = np.divide(population_agefrac_in,sum(population_agefrac_in))
u0[:,0]=population_agefrac
u0[1,1]=1/population_N
u0[1,0]-=1/population_N

age_group_number = 10

u0 = np.transpose(u0)

@jit(nopython=False)
def f(dy, y, t): #Y is the 81 len arr from prob, t is pycall.jlwrap.diffeqbase.nullparameters(); is this intended?
	#define total asym and sym for system of equations

	Itot_a = np.sum(y[2])
	Itot_s = np.sum(y[3])

	for i in range(0, 10):
		dy[0,i] = -pars_beta_a*y[0,i]*Itot_a - pars_beta_s*y[0,i]*Itot_s

		dy[1,i] = pars_beta_a*y[0,i]*Itot_a + pars_beta_s*y[0,i]*Itot_s - pars_gamma_e*y[1,i]

		dy[2,i] = pars_p[i]*pars_gamma_e*y[1,i] - pars_gamma_a * y[2,i]

		dy[3,i] = (1 - pars_p[i])*pars_gamma_e*y[1,i] - pars_gamma_s*y[3,i]

		dy[4,i] = agepars_hosp_frac[i]*(1 - agepars_hosp_crit[i])*pars_gamma_s*y[3,i] - pars_gamma_h*y[4,i]

		dy[5,i] = agepars_hosp_frac[i]*agepars_hosp_crit[i]*pars_gamma_s*y[3,i] - pars_gamma_h * y[4,i]

		dy[6,i] = pars_gamma_a*y[2,i] + (1 - agepars_hosp_frac[i])*pars_gamma_s*y[3,i] + pars_gamma_h*y[4,i] + (1 - agepars_crit_die[i])*pars_gamma_h*y[5,i]

		dy[7,i] = agepars_crit_die[i]*pars_gamma_h*y[5,i]

# Run solver and initialise solver parameters
tspan = (0., outbreak_pTime)
prob = de.ODEProblem(f, u0, tspan)
sol = de.solve(prob)

plt.plot(sol.t,sol.u)
plt.show()