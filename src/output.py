import src.cleaning
import src.analysis
import src.pdf
import pandas as pd
import numpy as np


def finalOutput(country, cost):
    '''Unifies all functions together to generate the final output through pipeline'''
    costs = src.cleaning.costsCleaning()
    happiness = src.cleaning.happinessCleaning()
    merged = pd.merge(costs, happiness, how='inner', on=['country'])
    dfinal = src.cleaning.mergedTable(merged)
    data = src.analysis.compare(dfinal, country, cost)
    graf = src.analysis.scatterPlot(dfinal, cost)
    result = src.pdf.createPDF(data, country, cost)
    return result