from functions import loadData, cleanData, mergeData, filterData, plotScatter, spearmanCorrelation, plotLines
import pandas as pd
import pytest
import os

testData1 = 'C:/Users/nooni/OneDrive/Documents/Desktop/PSCP_Final-1/testDataSample1.csv'
testData2 = 'C:/Users/nooni/OneDrive/Documents/Desktop/PSCP_Final-1/testDataSample2.csv'

#Test loadData()

def testLoadData():
    df = loadData(testData1)

    assert isinstance(df, pd.DataFrame)
    assert len(df) == 10

#Test cleanData()

def testLoadData():
    df = loadData(testData1)
    clean_df = cleanData(df)

    assert clean_df.isnull().sum().sum() == 0
    assert len(clean_df) == 5

#Test mergeData()

def testMergeData():
    df1 = cleanData(loadData(testData1))
    df2 = cleanData(loadData(testData2))
    df = mergeData(df1, df2, 'c1', 'c2')

    assert df.shape[1] == 4

#Test spearmanCorrelation1()

def testSpearmanCorrelation1():
    df = pd.DataFrame({
        'ColumnX': [1, 2, 3, 4, 5],
        'ColumnY': [5, 4, 3, 2, 1] 
    })

    correlation, p_value = spearmanCorrelation(df, 'ColumnX', 'ColumnY')
    assert round(correlation, 3) == -1.000
    assert round(p_value, 3) == 0.000


#Test plotScatter()

def testPlotScatter():
    df = mergeData(cleanData(loadData(testData1)), cleanData(loadData(testData2)), 'c1', 'c2')
    try:
        plotScatter(df, 'c3', 'c4', 'test_plot.png')
    except Exception as e:
        pytest.fail(f"plotScatter raised an error: {e}")

#Test plotLines()

def testPlotLines():
    df = mergeData(cleanData(loadData(testData1)), cleanData(loadData(testData2)), 'c1', 'c2')

    try:
        plotLines(df, 'c2', 'c3', 'c4', 'Test Country', 'test_plot1.png')
    except Exception as e:
        pytest.fail(f"plotLines raised an error: {e}")

    assert os.path.exists('test_plot1.png'), "Plot file was not saved at test_plot1.png"






