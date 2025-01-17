# PSCP_Final

## **Overview**

This project performs data analysis on 2 datasets on gdp per capita and annual CO₂ emmissions per capita. The intention is to establish and analyse trends and correlations betweeen the two varibles, both globally and on a country by country basis.

The data is sourced from Our World in Data.

## **Table of Contents**

1. File Structure
2. Technologies and Libraries
3. Installation Instructions
4. Usage
5. Tests

## 1. File Structure

```
PSCP_Final/
│
├── .circleci/
│ └──config.yml
│
├── __pycache__/
├── data/
│ ├── gdp-per-capita-worldbank.csv
│ └── per-caita-co-emissions.csv
│
├── figures/
│ ├── brazil_line.png
│ ├── china_line.png
│ ├── scatter_plot.png
│ ├── uk_line.png
│ └── us_line.png
│
├── test_folder/
│ ├── testDataSample1.csv
│ ├── testDataSample2.csv
│ ├── test_plot.png
│ └── test_plot1.png
│
├── README.md
├── README_figures.md
├── README_functions.md
├── README_test.md
├── figures.py
├── functions.py
├── requirements.txt
└── test.py
```

## **2. Technologies and Libraries**

- Python
- pandas
- matplotlib
- spicy
- numpy
- pytest
- CircleCI

## **3. Installation Instructions**

1. Clone this repository or download the script directly

```
git clone https://github.com/nooneAhmed/PSCP_Final.git
```

2. Navigate to the project directory:

```
cd PSCP_Final
```

3. Install the required libraries:

```
pip install -r requirements.txt
```

## 4. Usage

1. Run functions.py to execute the primary functions:

```
python functions.py
```

2. Run figures.py to fenerate the figures and run the analysis

```
python figures.py
```

3. Results:

- Output figures will be saved in the `figures/` directory
- The `data/` directory contains the datasets used for analysis
- The `test_folder/` directory includes test data and outputs

4. Modify and test:

- To test your custom data, replace files in the `data/` folder with your own, ensuring the format matches the existing csv files.

## 5. Tests

Testing is perforemed using pytest. The `test.py` file contains unit tests for core funtions. Follow these steps to run the tests

1. Ensure you have pytest installed

```
pip install pytest
```

2. Run the tests:

```
pytest tests.py
```

3. Tests results, including any generated plots, will be saved in the `test_folder/` directory for review.
