function dydt = covid_model_ga(t,y,pars,agepars)
% function dydt = stir_model_ga(t,y,pars,agepars)
% SEIaISR (open) and then I_ha I_hs D - 8 categories in total, all age-stratified

% Assign things
dydt=zeros(length(y),1);
Ia=sum(y(agepars.Ia_ids));
Is=sum(y(agepars.Is_ids));
R = sum(y(agepars.R_ids));
S = sum(y(agepars.S_ids));
E = sum(y(agepars.E_ids));

% Dynamics -  Base Model
dydt(agepars.S_ids)=-pars.beta_a*y(agepars.S_ids)*Ia-pars.beta_s*y(agepars.S_ids)*Is;
dydt(agepars.E_ids)=pars.beta_a*y(agepars.S_ids)*Ia+pars.beta_s*y(agepars.S_ids)*Is-pars.gamma_e*y(agepars.E_ids);
dydt(agepars.Ia_ids)=pars.p'.*pars.gamma_e.*y(agepars.E_ids)-pars.gamma_a*y(agepars.Ia_ids);
dydt(agepars.Is_ids)=(ones(size(pars.p))-pars.p)'.*pars.gamma_e.*y(agepars.E_ids)-pars.gamma_s*y(agepars.Is_ids);
dydt(agepars.Ihsub_ids)=agepars.hosp_frac'.*(1-agepars.hosp_crit')*pars.gamma_s.*y(agepars.Is_ids)-pars.gamma_h*y(agepars.Ihsub_ids);
dydt(agepars.Ihcri_ids)=agepars.hosp_frac'.*agepars.hosp_crit'*pars.gamma_s.*y(agepars.Is_ids)-pars.gamma_h*y(agepars.Ihcri_ids);
dydt(agepars.R_ids)=pars.gamma_a*y(agepars.Ia_ids)+pars.gamma_s*y(agepars.Is_ids).*(1-agepars.hosp_frac')+pars.gamma_h*y(agepars.Ihsub_ids)+pars.gamma_h*y(agepars.Ihcri_ids).*(1-agepars.crit_die');
dydt(agepars.D_ids)=pars.gamma_h*y(agepars.Ihcri_ids).*agepars.crit_die';

dydt(agepars.Hcum_ids)=agepars.hosp_frac'.*(1-agepars.hosp_crit')*pars.gamma_s.*y(agepars.Is_ids)+agepars.hosp_frac'.*agepars.hosp_crit'*pars.gamma_s.*y(agepars.Is_ids);
