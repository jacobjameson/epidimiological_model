"""
Epidemiology Modeling

JACOB JAMESON   
"""
import math

class disease:
    
    def __init__(self):
        
        self.discount_rate = 0.0025
        self.exit_rate_susceptible_ds = 0.001
        self.exit_rate_infected_d1 = 0.02
        self.arrival_per_month = 10
        self.risk_encounters_per_month = 1
        self.infection_efficiency_no_intervention = 0.04
        self.infection_efficiency_intervention = 0.03
        self.pop_size = 1000
        self.susceptible_pop = 750
        self.disease_prevalence = 250
        self.cost_intervention_infected_person_per_month = 5000
        self.QALM = 12500
        self.QALM_infected = 10000
        self.month = 0
        
    def __repr__(self):
        '''
        '''
        rep =  "{} people are infected. \n".format(self.disease_prevalence)
        rep +=  "{} people are susceptible. \n".format(self.susceptible_pop)
        rep += "It has been {} months.".format(self.month)
        return rep


    def _advance_one_month_0(self):
        '''
        Advances the disease object one month without intervention.
        '''
        infected = (self.disease_prevalence +
            self.infection_efficiency_no_intervention * 
            self.risk_encounters_per_month *
            self.susceptible_pop *
            (self.disease_prevalence/self.pop_size) -
            (self.exit_rate_infected_d1 * self.disease_prevalence))

        susceptible = (self.arrival_per_month +
            self.susceptible_pop - 
            (self.infection_efficiency_no_intervention * 
            self.risk_encounters_per_month *
            self.susceptible_pop) *
            (self.disease_prevalence/self.pop_size) -
            self.exit_rate_susceptible_ds *
            self.susceptible_pop)

        self.disease_prevalence = infected
        self.susceptible_pop = susceptible
        self.pop_size = self.disease_prevalence + self.susceptible_pop
        self.month += 1


    def _simulate_0(self, month):
        '''
        Simulates disease progression without intervention for a given
        number of months (input).
        '''
        while self.month < month:
            self._advance_one_month_0()
            
    
    def _advance_one_month_1(self):
        '''
        Advances the disease object one month with intervention.
        '''
        infected = (self.disease_prevalence +
            self.infection_efficiency_intervention * 
            self.risk_encounters_per_month *
            self.susceptible_pop *
            (self.disease_prevalence/self.pop_size) -
            (self.exit_rate_infected_d1 * self.disease_prevalence))
        
        susceptible = (self.arrival_per_month +
            self.susceptible_pop - 
            (self.infection_efficiency_intervention *
            self.risk_encounters_per_month *
            self.susceptible_pop) *
            (self.disease_prevalence/self.pop_size) -
            self.exit_rate_susceptible_ds *
            self.susceptible_pop)
        
        self.disease_prevalence = infected
        self.susceptible_pop = susceptible
        self.pop_size = self.disease_prevalence + self.susceptible_pop
        self.month += 1
        
        
    def _simulate_1(self, month):
        '''
        Simulates disease progression with intervention for a given
        number of months (input).
        '''
        while self.month < month:
            self._advance_one_month_1()
    
    
    def _PDV_health_0(self, month):
        '''
        Present discounted value of well-being of the population in that month
        with no intervention.
        '''
        self._simulate_0(month)
        return (math.exp(-self.discount_rate * self.month) * 
                ((self.QALM_infected * self.disease_prevalence) +
                (self.QALM * self.susceptible_pop)))
    
    
    def _PDV_health_1(self, month):
        '''
        Present discounted value of well-being of the population in that month
        with intervention.
        '''
        self._simulate_1(month)
        return (math.exp(-self.discount_rate * self.month) * 
                ((self.QALM_infected * self.disease_prevalence) +
                (self.QALM * self.susceptible_pop)))
    

    def _intervention_cost_1(self, month):
        '''
        Present discounted value of cost of intervention in that month.
        '''
        self._simulate_1(month)
        return (math.exp(-self.discount_rate * self.month) * 
                (self.cost_intervention_infected_person_per_month * 
                 self.disease_prevalence))
    
    
def cost_effective(cost, gamma=0.25):
    '''
    Returns a boolean indicating if the intervention is cost effective.
    '''
    d1 = disease()
    d1.cost_intervention_infected_person_per_month = cost
    d1.infection_efficiency_intervention = (1 - gamma) * 0.04
    d0 = disease()
    cost_total = 0
    health_value_1 = 0
    health_value_0 = 0
    for month in range(0,241):
        cost_total += d1._intervention_cost_1(month)
        health_value_1 += d1._PDV_health_1(month)
        health_value_0 += d0._PDV_health_0(month)
    if health_value_1 - cost_total >= health_value_0:
        return True
    else:
        return False
        

def max_effective_cost(gamma):
    '''
    Given gamma as input, this function determines the max effective cost.
    '''
    cost = 0
    while cost_effective(cost, gamma) == True:
        cost += 1
    return cost
