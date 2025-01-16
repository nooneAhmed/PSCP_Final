### figures.py documentation

This module creates figures and runs a spearman correlation test to analyse the relationship between GDP per capita and annual CO₂ emissions per capita. The datasets are sourced from Our World in Data and are availible in the repository

The script generates:

- A scatter plot showing the relationship between GDP per capita and annual CO₂ emmissions per capita
- Spearman Correaltion coefficients and p-value to quantify the relationship between the variables
- Line plots showing the treand of the variables over time in select countries

### Functions

The following functions are imported from functions.py:

- loadData()
- cleanData()
- mergeData()
- filterData()
- plotScatter()
- spearmanCorrelation()
- plotLines()

### Detailed Workflow

## 1. Data loading, cleaning and merging

- Using loadData(), dataframed gdp_df and co_df are created by reading data from "C:/Users/nooni/OneDrive/Documents/Desktop/PSCP_Final-1/gdp-per-capita-worldbank.csv" and "C:/Users/nooni/OneDrive/Documents/Desktop/PSCP_Final-1/per-capita-co-emissions.csv" respectively

- Both dataframes are cleaned using cleanData()

- The dataframe full_df is created by merging gdp_df and co_df on 'Entity' and 'Year'

## 2. Scatter Plot

- A scatter plot is created to visualise the relationship between the variables.
- The png is saved to "C:/Users/nooni/OneDrive/Documents/Desktop/PSCP_Final-1/figures/scatter_plot.png"

## 3. Spearman Correlation

- The spearman correlation coefficient and p value are computed for the two variables using spearmanCorrelation() and printed.

## 4. Line Graps

- Dataframes are made for the US, UK, China and Brazil using the filterData()
- Line plots are made for each country and saved in "C:/Users/nooni/OneDrive/Documents/Desktop/PSCP_Final-1/figures" using plotLines()
