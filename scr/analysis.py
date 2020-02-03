import pandas as pd
import numpy as np

# Compara los datos de los filtros elegidos con la media:
def compare(dfinal, country, cost):
    filt = dfinal.loc[country, cost]
    mean = dfinal[[cost]].mean(axis=0)
    mean = round(mean,2)
    result = f'\nThe cost of {cost} represents {filt[0]}% of the average monthly salary in {country}.\n'
    result = result + f'\nThe happiness score in {country} is {filt[1]}.\n'
    if (filt[0] - mean[0]) > 0 and (filt[1] - mean[1]) > 0:
        result = result + f'\nThe cost of {cost} is {round(abs((filt[0] - mean[0])),2)}% higher than the average of 96 countries analised.\nEven so, they are happier than the average.\n'
    elif (filt[0] - mean[0]) > 0 and (filt[1] - mean[1]) < 0:
        result = result + f'\nThe cost of {cost} is {round(abs((filt[0] - mean[0])),2)}% higher than the average of 96 countries analised.\nFurthermore, they are less happy than the average.\n'
    elif (filt[0] - mean[0]) < 0 and (filt[1] - mean[1]) > 0:
        result = result + f'\nThe cost of {cost} is {round(abs((filt[0] - mean[0])),2)}% lower than the average of 96 countries analised.\nBesides, they are happier than the average.\n'
    elif (filt[0] - mean[0]) < 0 and (filt[1] - mean[1]) < 0:
        result = result + f'\nThe cost of {cost} is {round(abs((filt[0] - mean[0])),2)}% lower than the average of 96 countries analised.\nInstead, they are less happy than the average.\n'
    return result

# Muestra un diagrama de dispersión relacionando el coste elegido y el índice de felicidad para los 96 países:
def scatterPlot(dfinal, cost):
    plot = dfinal.plot.scatter(x=(cost,'happiness'), y=(cost,'% salary'), title=f'Relation between cost of {cost} and happiness in 96 countries')
    plot.set_xlabel('Happiness score')
    plot.set_ylabel(f'Cost of {cost}')
    fig = plot.get_figure()
    return fig.savefig("../OUTPUT/graph.png")