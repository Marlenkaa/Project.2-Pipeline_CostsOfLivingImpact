#!/usr/local/bin/python3

import pandas as pd
import numpy as np

import sys
import argparse
import subprocess
import getpass
import json
import os
import requests
import re
import datos

def getFilters():
    parser = argparse.ArgumentParser(description='XXXXXXXXXXXXXX')
    parser.add_argument('--Country',
                        help='XXXXXXXXXXXXX',
                        default="Spain"
                        )
    parser.add_argument('--Cost',
                        help='XXXXXXXXXXXXXXXX',
                        default="wine"
                        )

    args = parser.parse_args()
    print(args)
    return args

def main():
    # Pipeline
    print(sys.argv)
    # Recibe filters
    data = getFilters()
    # Print data
    country = data.Country
    cost = data.Cost
    print(FUNCION QUE HAGA TODO A LA VEZ(country, cost))

if __name__=="__main__":
    main()