# Epidemiology Modeling

A population starts with 1,000 people. Every month, 10 uninfected people join the population. At the beginning, 250/1000 people are infected with a really bad disease that has a 2% monthly mortality rate. Uninfected people have a mortality rate of 0.1% monthly mortality rate. People randomly mix at a rate of once per month. When an uninfected and infected person have a risk contact, there is probability K that the infection will be transmitted.

Nomenclature for model:

Discount rate per month (r is about 3%/year): 0.25%

Exit rate from susceptible population (mortality rate) (\delta_S): 0.100%

Exit rate from infected population (mortality rate) (\delta_I): 2.000%

Arrival of new susceptible people into the population (\theta): 10 people per month

Rate of risk encounters per month (\lamda): 1/month

Infection efficiency (K)--the probability that transmission of infection occurs when an infected and uninfected person mix absent intervention: 0.04

Infection efficiency (kappa) given risk-reduction intervention K(1-y)—Here y=0.25 is a measure of the intervention’s effectiveness: 0.03

Total population size N(t). This will be higher with the intervention than without it over time, because reducing the prevalence of infection will allow people to remain longer in the population: Initial value of 1000

The number of susceptible (uninfected people)—S(t): Initial value of 750 

Disease prevalence I(t): Initial prevalence 25% (250 people)

Cost of intervention per infected person per month ($C): $5,000

Value we place on a month of life absent infection (One QALM—Quality-adjusted life month): $12,500

Value we place on a month of life with infection (Equivalent to about 0.8 Quality-adjusted life month): $10,000

Treatment costs: Completely ignored


The intervention has positive benefit if the present discounted value of the intervention exceeds the present discounted value in the absence of the intervention. 
