# *Does costs of living affect our happiness?*

<p align="center">
    <img src="https://raw.githubusercontent.com/Shurlena/Project.2-Pipeline_CostsOfLivingImpact/master/images/project.jpg">
</p>

The goal of this project is create a pipeline that shows the relationship between a chosen cost of living price and the happiness index of elected country. The final result is presented in a pdf file where we can check the cost impact on the average salary, as well as the happiness score reported in given country. Additionally, the cost impact is compared to the rest of the countries analyzed and we can find out if there is any relationship between both parameters from the scatter plot displayed.

### INPUT

To make our analysis, we need the World Happiness Report 2019, which is the csv we start from. It can be found right here in Kaggle: https://www.kaggle.com/unsdsn/world-happiness#2019.csv

Also, we need the average prices of different costs of living by country, as well as the average month salary. But to get that information, is necessary to do web scraping (webScraping_CostOfLife.ipynb) on this web: https://www.numbeo.com/cost-of-living/prices_by_country.jsp

### OUTPUT

Here we can find the csv file with the saved data after web scraping, as well as an example of the final pdf output generated from pipeline request and the scatter plot image inserted into pdf file.

### scr

All the cleaning, analysis and preparation process is condensed in the following scripts:

* *cleaning.py* -> functions that cleans and organize the data from World Happiness Report csv and Costs of Living scraped csv, merge them togheter and create the final dataframe with the impact of each cost of living on the average month salary by country and the happiness index reported.

* *analysis.py* -> functions that compare the impact of costs per country with the average impact of all countries, the same comparision with happiness index and create a scatter plot that relates both parameters for trend searches.

* *pdf.py* -> creates a pdf with the analysis made in the previous script.

* *output.py* -> holds all the previous scripts in one function to execute them in programmed order once the pipeline search is runned.

* *functions-tests.ipynb* -> checks if all created functions that were introduced in the previous scripts work properly.

* *pipelineCheck.py* -> functions designed to handle the possible value errors introduced in our pipeline whilst parameters are elected, such as misspelling or values not contemplated in our analysis.

* *webScraping_CostOfLife.ipynb* -> notebook that contains the web scraping made to obtain the necessary data about cost averages and monthly salary by country (cost_of_life_by_country.csv in OUTPUT).

### main.py

This is the main of this project and where all previous work is condensed to create our pipeline.

##### HOW IT WORKS:

Bash command to execute the pipeline: ***python3 main.py -x <chosen_country> -y <chosen_cost>***

For further instructions, a help command is available: ***python3 main.py -h***

** Pipeline parameters are case-insensitive

It will be displayed a message reporting that our request was successfully made and the pdf was created in the OUTPUT directory. The file would look like this:

<p align="center">
    <img src="https://raw.githubusercontent.com/Shurlena/Project.2-Pipeline_CostsOfLivingImpact/master/images/finalPDF.png" width="500">
</p>

In this example we have requested to see if there is any relationship between the average price of wine and the happiness index in Spain.

As we can see, the impact of wine price in the monthly salary average of spanish people represents an 0.39%, while the happiness score reported by spaniards in 2019 was 6.35 points over 10.

Comparing this data to the rest of 96 countries, the price of wine in Spain is 69.29% cheaper and also the spanish population is happier than the average (5.89 over 10).

Therefore, checking the scatter plot, we see that could exist a relashionship between these two concepts, as the cheaper the wine is the happier people are (negative tendency line).
