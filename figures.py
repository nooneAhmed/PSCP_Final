from functions import loadData, cleanData, mergeData, filterData, plotScatter, plotLines
import pandas as pd

gdp_df = loadData(r"C:/Users/nooni/OneDrive/Documents/Desktop/PSCP_Final-1/gdp-per-capita-worldbank.csv")
gdp_df = cleanData(gdp_df)
#print(gdp_df.head())

co_df = loadData(r"C:/Users/nooni/OneDrive/Documents/Desktop/PSCP_Final-1/per-capita-co-emissions.csv")
co_df = cleanData(co_df)
#print(co_df.head())

full_df = mergeData(gdp_df, co_df, 'Entity', 'Year')
#print(full_df.head())

scatter = plotScatter(full_df, 'GDP per capita', 'Annual CO₂ emissions (per capita)', "C:/Users/nooni/OneDrive/Documents/Desktop/PSCP_Final-1/figures/scatter_plot.png")

us_df = filterData(full_df, 'Entity', 'United States')
line1 = plotLines(us_df, 'Year', 'GDP per capita', 'Annual CO₂ emissions (per capita)', 'United States', "C:/Users/nooni/OneDrive/Documents/Desktop/PSCP_Final-1/figures/us_line.png")

ch_df = filterData(full_df, 'Entity', 'China')
line2 = plotLines(ch_df, 'Year', 'GDP per capita', 'Annual CO₂ emissions (per capita)', 'China', "C:/Users/nooni/OneDrive/Documents/Desktop/PSCP_Final-1/figures/china_line.png")

bz_df = filterData(full_df, 'Entity', 'Brazil')
line3 = plotLines(bz_df, 'Year', 'GDP per capita', 'Annual CO₂ emissions (per capita)', 'Brazil', "C:/Users/nooni/OneDrive/Documents/Desktop/PSCP_Final-1/figures/brazil_line.png")

uk_df = filterData(full_df, 'Entity', 'United Kingdom')
line4 = plotLines(uk_df, 'Year', 'GDP per capita', 'Annual CO₂ emissions (per capita)', 'United Kingdom', "C:/Users/nooni/OneDrive/Documents/Desktop/PSCP_Final-1/figures/uk_line.png")
