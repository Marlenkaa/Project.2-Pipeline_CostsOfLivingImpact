import cleaning
import analysis
import pandas as pd
import numpy as np
import pdf

def finalOutput(country, cost):
    costs = cleaning.costsCleaning()
    happiness = cleaning.happinessCleaning()
    merged = pd.merge(costs, happiness, how='inner', on=['country'])
    dfinal = cleaning.mergedTable(merged)
    data = analysis.compare(country, cost)
    graf = analysis.scatterPlot(cost)



    pdf.creaPDF(a)

    return 