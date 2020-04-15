from diffeqpy import de

def covid_model_ga(dy, t, y, pars, agepars):
	dy[0] = -pars[0]