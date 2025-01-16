import pandas as pd
import matplotlib.pyplot as plt


de loadData(filepath: str) -> pd.DataFrame:
    """Loads data from csv file"""

    data = pd.read_csv(filepath)
    return data


def cleanData(df: pd.DataFrame) -> pd.DataFrame:

    """Cleans the dataset by removing the missing values"""

    df = df.dropna()
    return df

def mergeData(df1: pd.DataFrame, df2: pd.DataFrame, column1: str, column2: str) -> pd.DataFrame:
    """Merges 2 dataframes on 2 columns"""

    df = pd.merge(df1, df2, on = [column1, column2], how = 'inner')

    return df

def filterData(df: pd.DataFrame, column: str, filter: str) -> pd.DataFrame:
    """Filters a datframe, returns the filtered dataframe"""

    df1 = df[df[column] == filter]

    return df1


def plotScatter(df: pd.DataFrame, columnX: str, columnY: str, savePath: str):

    """Plot two columns of a dataframe into a scatter graph"""

    plt.figure(figsize = (8, 6))
    plt.scatter(df[columnX], df[columnY], color = 'blue', alpha = 0.6)

    """Labels, grid and title"""

    plt.title(f'Scatter plot of {columnX} vs {columnY}')
    plt.xlabel(columnX)
    plt.ylabel(columnY)

    plt.grid(axis = 'x', linestyle = '--')
    plt.grid(axis = 'y', linestyle = '--')

    """Save figure"""

    plt.savefig(savePath)

    plt.close()

def plotLines(df: pd.DataFrame, columnX: str, columnY1: str, columnY2: str, country: str, savePath: str):

    """Plots a line graph with two variables against one"""

    fig, ax = plt.subplots(figsize = (8, 6))

    ax.plot(df[columnX], df[columnY1], color = 'midnightblue', label = columnY1)
    ax.set_xlabel(columnX)
    ax.set_ylabel(columnY1, color = 'midnightblue')
    ax.tick_params(axis = 'y', labelcolor = 'midnightblue')

    ax2 = ax.twinx()
    ax2.plot(df[columnX], df[columnY2], color='deepskyblue', label=columnY2)
    ax2.set_ylabel(columnY2, color='deepskyblue')
    ax2.tick_params(axis='y', labelcolor='deepskyblue')


    ax.set_title(f'Line Graph: {country} {columnY1} and {columnY2} Over Time')
    ax.grid(axis = 'x', linestyle = '--')
    ax.grid(axis = 'y', linestyle = '--')
    lines1, labels1 = ax.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax.legend(lines1 + lines2, labels1 + labels2, loc='upper right')

    """Save figure"""

    plt.savefig(savePath)

    plt.close()