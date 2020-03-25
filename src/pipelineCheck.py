import src.cleaning
import pandas as pd
import numpy as np
import argparse

def countryCheck(country):
    '''Handles value errors such as misspelling or country not contemplated in our analysis'''
    costsliving = src.cleaning.costsCleaning()
    happiness = src.cleaning.happinessCleaning()
    merged = pd.merge(costsliving, happiness, how='inner', on=['country'])
    countries = list(merged.country)
    if country.lower() in countries:
        return country.lower()
    else:
        sms = 'Country not valid. Please choose one from the following list: '+str(countries)
        raise argparse.ArgumentTypeError(sms)

def costCheck(cost):
    '''Handles value errors such as misspelling or cost of living not contemplated in our analysis'''
    costsliving = src.cleaning.costsCleaning()
    happiness = src.cleaning.happinessCleaning()
    merged = pd.merge(costsliving, happiness, how='inner', on=['country'])
    costs = list(merged.columns)
    if cost.lower() in costs:
        return cost.lower()
    else:
        sms = 'Cost not valid. Please choose one from the following list: '+str(costs)
        raise argparse.ArgumentTypeError(sms)


# Tried make class to refactor code but couldn't fix the bash error showed:
# main.py: error: argument -x/--Country: invalid countryCheck value: 'Spain'

'''
class Check:
    def __init__(self, country='spain', cost='wine'):
        self.country = country
        self.cost = cost
        costsliving = src.cleaning.costsCleaning()
        happiness = src.cleaning.happinessCleaning()
        self.merged = pd.merge(costsliving, happiness, how='inner', on=['country'])
    def countryCheck(self):
        countries = list(self.merged.country)
        if self.country.lower() in countries:
            return self.country.lower()
        else:
            sms = 'Country not valid. Please choose one from the following list: '+str(countries)
            raise argparse.ArgumentTypeError(sms)
    def costCheck(self):
        costs = list(self.merged.columns)
        if self.cost.lower() in costs:
            return self.cost.lower()
        else:
            sms = 'Cost not valid. Please choose one from the following list: '+str(costs)
            raise argparse.ArgumentTypeError(sms)
'''