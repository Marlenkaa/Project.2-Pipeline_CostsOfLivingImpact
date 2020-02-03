import cleaning
import analysis
import pdf
import pandas as pd
import numpy as np


def finalOutput(country, cost):
    costs = cleaning.costsCleaning()
    happiness = cleaning.happinessCleaning()
    merged = pd.merge(costs, happiness, how='inner', on=['country'])
    dfinal = cleaning.mergedTable(merged)
    data = analysis.compare(dfinal, country, cost)
    graf = analysis.scatterPlot(dfinal, cost)
    result = pdf.createPDF(data, country, cost)
    return result