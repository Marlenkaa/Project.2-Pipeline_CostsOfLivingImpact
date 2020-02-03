#!/usr/local/bin/python3

import pandas as pd
import numpy as np
import output
import argparse

import sys
import subprocess
import getpass
import os


def getFilters():
    parser = argparse.ArgumentParser(description='Given a cost of living, we can see how much it costs depending of the average monthly salary of the chosen country (purchasing power), as well as the happiness index of that country, compared to the total average of 96 countries analyzed. In addition, we can check whether there is a relationship between both parameters')
    parser.add_argument('-x','--Country',
                        metavar = '',
                        required = True,
                        help='Choose a country',
                        default="Spain"
                        )
    parser.add_argument('-y','--Cost',
                        metavar = '',
                        required = True,
                        help='Choose a cost of living between: supermarket, restaurant, mid-range restaurant, mcdonalds, wine, wine, cigarettes, rent, utilities, internet, fitness, cinema, public transport and car',
                        default="wine"
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
    country = data.Country
    cost = data.Cost
    result = output.finalOutput(country, cost)
    return result

if __name__ == '__main__':
    print(main())