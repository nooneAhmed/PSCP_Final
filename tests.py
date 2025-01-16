from functions import loadData, cleanData, mergeData, filterData, plotScatter, plotLines
import pandas as pd

testData1 = 'C:/Users/nooni/OneDrive/Documents/Desktop/PSCP_Final-1/testDataSample1.csv'
testData2 = 'C:/Users/nooni/OneDrive/Documents/Desktop/PSCP_Final-1/testDataSample2.csv'

#Test loadData()

def testLoadData():
    df = loadData(testData1)

    assert isinstance(df, pd.DataFrame)
    assert len(df) == 7






