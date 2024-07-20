# Data Exploratory Analysis

This is a Streamlit application for performing exploratory data analysis on CSV datasets. 

## Live Application 
You can view the live application [here](https://eda-web-app-4aa663388421.herokuapp.com/).

## Features

- **Upload CSV files**: Easily upload your dataset in CSV format.
- **Preview dataset**: View the first and last few rows of your dataset.
- **Data types**: Display the data types of each column.
- **Shape of dataset**: Show the number of rows and columns in the dataset.
- **Check for null values**: Identify and visualize missing data in the dataset.
- **Check for duplicates**: Detect and optionally remove duplicate rows.
- **Summary statistics**: Generate summary statistics for numerical and categorical columns.
- **Data visualizations**: Create histograms, pairplots, box plots, and a correlation heatmap.
- **Download processed data**: Download the cleaned and processed dataset.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/mndebelelt/EDA-Web-App.git
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:

    ```bash
    streamlit run edaWebApp.py
    ```

## Usage

1. Open the Streamlit app.
2. Upload your CSV file.
3. Use the checkboxes to explore and analyze your data.

