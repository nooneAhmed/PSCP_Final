from functions import loadData, cleanData, mergeData, filterData, plotScatter, plotLines
import pandas as pd

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







