import pandas as pd
import numpy as np

# Compara los datos de los filtros elegidos con la media:
def compare(country, cost):
    filt = dfinal.loc[country, cost]
    mean = dfinal[[cost]].mean(axis=0)
    mean = round(mean,2)
    print(f'The cost of {cost} represents {filt[0]}% of the average monthly salary in {country}\n')
    print(f'The happiness score in {country} is {filt[1]}\n')
    if (filt[0] - mean[0]) > 0 and (filt[1] - mean[1]) > 0:
        return f'The cost of {cost} is {abs((filt[0] - mean[0]))}% higher than the average of 96 countries analised.\nEven so, they are happier than the average.'
    elif (filt[0] - mean[0]) > 0 and (filt[1] - mean[1]) < 0:
        return f'The cost of {cost} is {abs((filt[0] - mean[0]))}% higher than the average of 96 countries analised.\nFurthermore, they are less happy than the average.'
    elif (filt[0] - mean[0]) < 0 and (filt[1] - mean[1]) > 0:
        return f'The cost of {cost} is {abs((filt[0] - mean[0]))}% lower than the average of 96 countries analised.\nBesides, they are happier than the average.'
    elif (filt[0] - mean[0]) < 0 and (filt[1] - mean[1]) < 0:
        return f'The cost of {cost} is {abs((filt[0] - mean[0]))}% lower than the average of 96 countries analised.\nInstead, they are less happy than the average.'
