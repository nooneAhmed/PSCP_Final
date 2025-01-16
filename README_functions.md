### functions.py documentation

This module contains functions for:

- Reading data
- Cleaning data
- Merging data
- Filtering data
- Running a Spearman Correlation Test
- Creating a scatter plot
- Creating a dual axis line graph

## Functions

### loadData(filepath: str) -> pd.DataFrame

Reads data from a csv file into a dataframe

**Parameters**

- str: csv file path

**Returns**
Dataframe of csv file

### cleanData(df: pd.DataFrame) -> pd.DataFrame

Cleans a dataframe by removing missing values

**Parameters**

- sdf (pd.DataFrame): dataframe to clean

**Returns**
Cleaned dataframe

### mergeData(df1: pd.DataFrame, df2: pd.DataFrame, column1: str, column2: str) -> pd.DataFrame

Merges 2 dataframes on two columns

**Parameters**

- df1, df2 (pd.dataframes): dataframes to be merged
- column1, column2 (str): names of columns for merging

**Assumptions**

- Data being mereged is already in a cleand dataframe
- The data is to be merged on two columns

**Returns**
Merged dataframe

### filterData(df: pd.DataFrame, column: str, filter: str) -> pd.DataFrame

Filters data from a dataframe, based on a specified criteria

**Parameters**

- df1 (pd.DataFrame): dataframe being filtered
- column (str): name of column being filtered
- filter (str): criteria being filtered

**Returns**

- df: filtered dataframe

### plotScatter(df: pd.DataFrame, columnX: str, columnY: str, savePath: str)

Plots a scatter plot using data in a dataframe and saves the plot as a png

**Parameters**

- df (pd.DataFrame): dataframe containing the data to be plotted
- columnX (str): name of column containing the data to be plotted on the x axis
- columnY (str): name of column containing data to be plotted on the y axis
- savePath (str): path where png of the plot is to be saved

**Assumptions**

- Data being plotted is in a cleaned dataframe

- Plot is to be saved as a png

### spearmanCorrelation(df: pd.DataFrame, columnX: str, columnY: str)-> tuple

Runs a Spearman Correlation test on two variables in a dataframe, and returns the results

**Parameters**

- df (pd.DataFrame): dataframe containing the data being tested

- columnX (str): name of the column containing the first variable being tested
- columnY (str): name of the column containing the second variable being tested

**Returns**
Tuple containing the Spearman coefficient and the p-value

**Assumptions**

- Both variables being tested are in one cleaned dataframe

### plotLines(df: pd.DataFrame, columnX: str, columnY1: str, columnY2: str, country: str, savePath: str)

Plots a line graph with 2 axes and saves it as a png

**Parameters**

- df (pd.DataFrame): dataframe containing the variables being plotted
- columnX (str): name of the column containing the varible that is to be plotted on the x axis
- columnY1 (str): name of the column containing the variable being plotted on the first (left) y axis
- columnY2 (str): name of the column containing the varibale being plotted on the second (right) y axis
- savePath (str): path where the png is to be stored

**Assumptions**

- The variables being plotted all exist in one cleaned dataframe
- Plot is to be saved as png
