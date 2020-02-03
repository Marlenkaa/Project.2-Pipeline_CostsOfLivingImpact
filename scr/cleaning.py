import pandas as pd
import numpy as np

# Extrae y organiza la tabla de costes de vida.
def costsCleaning():
    df = pd.read_csv('../OUTPUT/cost_of_life_by_country.csv')
    # Renaming columns of use:
    df.rename(columns={'Meal, Inexpensive Restaurant':'restaurant',
                      'Meal for 2 People, Mid-range Restaurant, Three-course':'mid-range restaurant',
                      'McMeal at McDonalds (or Equivalent Combo Meal)':'mcdonalds',
                      'Bottle of Wine (Mid-Range)':'wine',
                      'Cigarettes 20 Pack (Marlboro)':'cigarettes',
                      'Monthly Pass (Regular Price)':'public transport',
                      'Volkswagen Golf 1.4 90 KW Trendline (Or Equivalent New Car)':'car',
                      'Internet (60 Mbps or More, Unlimited Data, Cable/ADSL)':'internet',
                      'Basic (Electricity, Heating, Cooling, Water, Garbage) for 85m2 Apartment':'utilities',
                      'Fitness Club, Monthly Fee for 1 Adult':'fitness',
                      'Cinema, International Release, 1 Seat':'cinema',
                      'Apartment (1 bedroom) in City Centre':'rent',
                      'Average Monthly Net Salary (After Tax)':'salary',
                      'Country':'country'
                     }, inplace=True)
    # Creating new column that groups all supermarket products simulating a shopping basket:
    df['supermarket'] = df['Milk (regular), (1 liter)'] + df['Loaf of Fresh White Bread (500g)'] + df['Rice (white), (1kg)'] + df['Eggs (regular) (12)'] + df['Local Cheese (1kg)'] + df['Chicken Breasts (Boneless, Skinless), (1kg)'] + df['Beef Round (1kg) (or Equivalent Back Leg Red Meat)'] + df['Apples (1kg)'] + df['Banana (1kg)'] + df['Oranges (1kg)'] + df['Tomato (1kg)'] + df['Potato (1kg)'] + df['Onion (1kg)'] + df['Lettuce (1 head)']
    # Creating final dataset:
    costs = df[['country', 'supermarket', 'restaurant', 'mid-range restaurant', 'mcdonalds', 'wine', 'cigarettes', 'rent', 'utilities', 'internet', 'fitness', 'cinema', 'public transport', 'car', 'salary']]
    # Removing Venezuela from the analysis as it is an outlier:
    costs = costs[costs.country != 'Venezuela']
    return costs

# Extrae y organiza la tabla de índice de felicidad.
def happinessCleaning():
    df = pd.read_csv('../INPUT/2019.csv')
    # Renaming columns of use:
    df.rename(columns={'Country or region':'country',
                       'Score':'happiness',
                     }, inplace=True)
    happiness = df[['country', 'happiness']]
    happiness = happiness.round({'happiness':2})
    return happiness

# Reorganiza el DataFrame fusionado y lo prepara para dar datos finales.
def mergedTable(merged):
    # Renaming column salary as it will represent the % of cost over salary:
    merged.rename(columns={'salary':'% salary'}, inplace=True)
    # Creating a MultiIndex for every cost of living related with salary and happiness score:
    cols = ['supermarket', 'restaurant', 'mid-range restaurant', 'mcdonalds', 'wine', 'cigarettes', 'rent', 'utilities', 'internet', 'fitness', 'cinema', 'public transport', 'car']
    mix = pd.MultiIndex.from_product([cols, ['% salary', 'happiness']])
    # Dividing every cost by salary:
    dfinal = round(merged[cols].div(merged['% salary'], axis=0).mul(100).reindex(mix, axis=1, level=0),2)
    idx = pd.IndexSlice
    # Reset the values from happiness score:
    dfinal.loc[:, idx[:, 'happiness']] = merged[['happiness']*len(cols)].to_numpy()
    # Including back the countries as index:
    dfinal['country'] = merged['country']
    dfinal = dfinal.set_index(['country'])
    return dfinal