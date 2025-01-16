### test.py documentation

This module contains unit tests for the fucntions used in this project, to ensure the functions work as expected and produce accurate results.

## Test Structures

**1. Test loadData()**

Verifies that loadData() correctly loads a CSV file into a Pandas DataFrame.

Checks:

- Output is a pd.DataFrame.
- Correct number of rows is loaded from the test data.

**2. Test cleanData**
Ensures that cleanData() removes all missing values from the data.

Checks:

- No missing values remain in the dataframe.
- The number of rows matches expectations after cleaning.

**3. Test mergeData**
Validates that mergeData() merges two datasets on 2 columns correctly.

Checks:

- The resulting DataFrame has the expected number of columns.
- The function does not flag errors.

**4. Test spearmanCorrelation**
Tests that spearmanCorrelation() calculates the Spearman correlation coefficient and p-value correctly.

Checks:

- The computed correlation matches expected values for sample inputs.
- The p-value is within an acceptable range.

**5. Test plotScatter**
Ensure that the plotScatter function generates a scatter plot without errors.

Checks:

- The function does not raise exceptions.
- The plot is saved to the specified file path.

**6. Test plotLines**
Test that the plotLines function generates a dual-axis line plot correctly.

Checks:

- The function does not raise exceptions.
- The plot file is saved at the correct location.
