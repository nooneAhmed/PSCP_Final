import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def loadData(filepath: str) -> pd.DataFrame:
    """Loads data from csv file"""

    data = pd.read_csv(filepath)
    return data

def cleanData(df: pd.DataFrame) -> pd.DataFrame:

    """Cleans the dataset by removing the missing values"""

    df = df.dropna()
    return df

def plotScatter(df: pd.DataFrame, columnX: str, columnY: str, savePath: str):

    """Plot two columns of a dataframe into a scatter graph"""

    plt.figure(figsize = (8, 6))
    plt.scatter(columnX, columnY, color = 'blue', alpha = 0.6)

    """Labels, grid and title"""

    plt.title(f'Scatter plot of {columnX} vs {columnY}')
    plt.xlabel(columnX)
    plt.ylabel(columnY)

    plt.grid(axis = 'x', linestyle = '--')
    plt.grid(axis = 'y', linestyle = '--')

    """Save figure"""

    plt.savefig(savePath)

    plt.close()

def plotLines(df: pd.DataFrame, columnX: str, columnY1: str, columnY2: str):

    """Plots a line graph with two variables against one"""

    fig, ax = plt.subplot(figsize = (8, 6))

    ax.plot(columnX, columnY1, color = 'midnightblue', label = columnY1)
    ax.set_xlabel(columnX)
    ax.set_ylabel(columnY1, color = 'midnightblue')
    ax.tick_params(axis = 'y', labelcolor = 'midnightblue')

    ax2 = ax.twin()
    ax2.plot(columnX, columnY2, color = 'deepskyblue', label = columnY2)
    ax2.set_ylabel(columnY2, color = 'deepskyblue')

    """Labels, grids, title and legend"""

    ax.set_title(f'Line Graph: {columnY1} and {columnY2} Over Time')
    ax.grid(axis = 'x', linestyle = '--')
    ax.grid(axis = 'y', linestyle = '--')
    lines1, labels1 = ax.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax.legend(lines1 + lines2, labels1 + labels2, loc='upper right')







