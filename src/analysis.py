import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def compare(dfinal, country, cost):
    '''Compares the parameters chosen in pipeline with the average'''
    filt = dfinal.loc[country, cost]
    mean = dfinal[[cost]].mean(axis=0)
    mean = round(mean,2)
    result = f'\nThe cost of {cost} represents {filt[0]}% of the average monthly salary in {country}.\n'
    result = result + f'\nThe happiness score in {country} is {filt[1]} over 10.\n'
    if (filt[0] - mean[0]) > 0 and (filt[1] - mean[1]) > 0:
        result = result + f'\nThe cost of {cost} is {round(((abs((filt[0] - mean[0])))/mean[0])*100,2)}% higher than the average of 96 countries analyzed ({mean[0]}%).\nEven so, they are happier than the average ({mean[1]}).\n'
    elif (filt[0] - mean[0]) > 0 and (filt[1] - mean[1]) < 0:
        result = result + f'\nThe cost of {cost} is {round(((abs((filt[0] - mean[0])))/mean[0])*100,2)}% higher than the average of 96 countries analyzed ({mean[0]}%).\nFurthermore, they are less happy than the average ({mean[1]}).\n'
    elif (filt[0] - mean[0]) < 0 and (filt[1] - mean[1]) > 0:
        result = result + f'\nThe cost of {cost} is {round(((abs((filt[0] - mean[0])))/mean[0])*100,2)}% lower than the average of 96 countries analyzed ({mean[0]}%).\nBesides, they are happier than the average ({mean[1]}).\n'
    elif (filt[0] - mean[0]) < 0 and (filt[1] - mean[1]) < 0:
        result = result + f'\nThe cost of {cost} is {round(((abs((filt[0] - mean[0])))/mean[0])*100,2)}% lower than the average of 96 countries analyzed ({mean[0]}%).\nInstead, they are less happy than the average ({mean[1]}).\n'
    return result

def scatterPlot(dfinal, cost):
    '''Displays a scatter plot with trend line that compares the cost of living chosen and the 
    happiness index by country.'''
    dfinal['Hapiness score'] = dfinal[cost]['happiness']
    dfinal[f'Cost of {cost}'] = dfinal[cost]['% salary']
    plot = sns.lmplot(x='Hapiness score', y=f'Cost of {cost}', data=dfinal)
    ax = plt.gca()
    ax.set_title(f'Relation between cost of {cost} and happiness in 96 countries')
    return plot.savefig("OUTPUT/graph.png")