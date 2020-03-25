# Shark Attacks Analysis

<p align="center">
    <img src="https://raw.githubusercontent.com/Shurlena/Project.1-SharkAttacksAnalysis/master/images/sharks.jpg" width="600">
</p>

The goal of this project is to analyze the data collected about attacks arisen around the globe by sharks. The analysis is comprehended between 1800 and 2016, looking for season and year trends as well as the countries most affected.

### INPUT
We start from Kaggle's csv, which can be find right here: https://www.kaggle.com/teajay/global-shark-attacks

### OUTPUT
After all data cleaning we have done in Shark_Attack_Analysis.ipynb, a csv copy is made for further analysis.

### scr
Here we can find a script with functions that we will need to use in Shark_Attack_Analysis.ipynb.

### Shark_Attack_Analysis.ipynb
This is the main of this project. All data cleaning and analysis is made in this notebook. Steps followed:

*STEP 1: Data Inspection*

Check what kind of data we have available, cleaning and analysis complexity, duplicated data, percentage of null values and data reliability.

*STEP 2: Data cleaning*

Once we know which data we want to keep, we proceed to make the hole data cleaning process to output a tidy csv, which will be used for further analysis.

*STEP 3: Analysis and Data Visualization*

The conclusions we have been able to get are:

- The highest number of attacks are registered between 2001 and 2016. This is probably due to the increasing documentation work over the years.
- Most attacks occur in summer. Countries above Equator line suffer more shark attacks in july, august and september, while countries underneath Equator line have most cases in december and january.
- USA and Australia are the countries where higher number of attacks occur. The main reason could be that both countries have the largest population and surfing culture.
- In USA, the most affected are surfers, injured mostly in the legs.
- In Australia, the most affected are bathers, injured mostly in the legs as well. However, there are 17% of chances that the attack ends in death, while in USA this percentage is just 7%.
