from functions import loadData, cleanData, mergeData, filterData, plotScatter, spearmanCorrelation, plotLines
import pandas as pd
import pytest
import unittest
import os
from io import BytesIO

class RunTests(unittest.TestCase):

    @classmethod
    
    def setUpClass(cls):
        """Set up test data for all tests."""
        cls.testData1 = 'data/testDataSample1.csv'
        cls.testData2 = 'data/testDataSample2.csv'

    #Test loadData()

    def testLoadData(self):
        df = loadData(self.testData1)

     
        self.assertIsInstance(df, pd.DataFrame, "loadData should return a DataFrame.")
        self.assertGreater(len(df), 0, "The DataFrame should not be empty.")
        self.assertIn("c1", df.columns, "Expected column 'c1' in the DataFrame.")


    #Test cleanData()

    def testCleanData(self):
        df = loadData(self.testData1)
        clean_df = cleanData(df)

        self.assertEqual(clean_df.isnull().sum().sum(), 0, "There should be no missing values after cleaning.")
        self.assertEqual(len(clean_df), 5, "The cleaned DataFrame should have 5 rows.")


    #Test mergeData()

    def testMergeData(self):
        df1 = cleanData(loadData(self.testData1))
        df2 = cleanData(loadData(self.testData2))
        df = mergeData(df1, df2, 'c1', 'c2')

        self.assertEqual(df.shape[1], 4, "The merged DataFrame should have 4 columns.")


    #Test spearmanCorrelation1()

    def testSpearmanCorrelation1(self):
        df = pd.DataFrame({
            'ColumnX': [1, 2, 3, 4, 5],
            'ColumnY': [5, 4, 3, 2, 1] 
        })

        correlation, p_value = spearmanCorrelation(df, 'ColumnX', 'ColumnY')
        self.assertEqual(round(correlation, 3), -1.000, "Spearman correlation should be -1.000")
        self.assertEqual(round(p_value, 3), 0.000, "P-value should be 0.000")



    #Test plotScatter()

    def testPlotScatter(self):
        df = mergeData(cleanData(loadData(self.testData1)), cleanData(loadData(self.testData2)), 'c1', 'c2')
        try:
            plotScatter(df, 'c3', 'c4', 'test_plot.png')
        except Exception as e:
            pytest.fail(f"plotScatter raised an error: {e}")

    #Test plotLines()

    def testPlotLines(self):
        df = mergeData(cleanData(loadData(self.testData1)), cleanData(loadData(self.testData2)), 'c1', 'c2')

        try:
            plotLines(df, 'c2', 'c3', 'c4', 'Test Country', 'test_plot1.png')
        except Exception as e:
            self.fail(f"plotScatter raised an error: {e}")

        self.assertTrue(os.path.exists('test_plot.png'), "The plot file 'test_plot.png' was not created.")


if __name__ == "__main__":
    unittest.main()



