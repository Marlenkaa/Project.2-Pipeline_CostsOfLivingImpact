#!/usr/local/bin/python3

import pandas as pd
import numpy as np
import src.output
import src.pipelineCheck as P
import argparse
from argparse import RawTextHelpFormatter
import sys
import subprocess
import os

def getFilters():
    parser = argparse.ArgumentParser(description='Given a cost of living, we can see the purchasing power of a chosen country, as well as the happiness index, compared to the total average of 96 countries analyzed. In addition, we can check whether there is a relationship between both parameters', formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-x','--Country',
                        metavar = '',
                        required = True,
                        help='Choose a country',
                        default='spain',
                        type=P.countryCheck
                        )
    parser.add_argument('-y','--Cost',
                        metavar = '',
                        required = True,
                        help='''

    Choose one cost of living:
    
    supermarket: contain costs of basic products simulating a shopping basket.
    restaurant: Meal in Inexpensive Restaurant.
    mid-range restaurant: Meal for 2 People in Mid-range Restaurant.
    mcdonalds: McMeal at McDonalds (or Equivalent Combo Meal).
    wine: Bottle of Wine (Mid-Range).
    cigarettes: 20 Pack (Marlboro).
    rent: Apartment (1 bedroom) in City Centre.
    utilities: (Electricity, Heating, Cooling, Water, Garbage) for 85m2 Apartment.
    internet: 60 Mbps or More, Unlimited Data, Cable/ADSL.
    fitness: Fitness Club, Monthly Fee for 1 Adult.
    cinema: International Release, 1 Seat.
    public transport: Monthly Pass (Regular Price).
    car: Volkswagen Golf 1.4 90 KW Trendline (Or Equivalent New Car).
    
    ''', 
                        default='wine',
                        type=P.costCheck
                        )
    args = parser.parse_args()
    print(args)
    return args

def main():
    # Pipeline
    print(sys.argv)
    # Receive filters
    data = getFilters()
    # Print data
    country = data.Country.lower()
    cost = data.Cost.lower()
    result = src.output.finalOutput(country, cost)
    print ('\n ----- \n')
    print('DATA ANALYZED. Please check your OUTPUT folder to find a pdf file with your requested data.')
    print ('\n ----- \n')
    return result

if __name__ == '__main__':
    main()
    