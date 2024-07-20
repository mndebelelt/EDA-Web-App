# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 15:13:30 2024

@author: Thabo M.
"""

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Title and Subheader
st.title("Data Exploratory Analysis")
st.subheader("Analysis using Python and Streamlit")

def main():
    file_upload = st.file_uploader("Upload your dataset in CSV format")
    
    if file_upload is not None:
        try:
            data = pd.read_csv(file_upload)
            st.success("File uploaded successfully")
    
            if st.checkbox("Preview dataset"):
                preview_data(data)
                
            if st.checkbox("Datatype of each column"):
                show_data_types(data)
            
            if st.checkbox("Shape of Dataset"):
                show_shape(data)
            
            if st.checkbox("Check for Null Values"):
                check_null_values(data)
            
            if st.checkbox("Check for Duplicates"):
                check_duplicates(data)
            
            if st.checkbox("Summary of Dataset"):
                show_summary(data)
            
            if st.checkbox("Data Visualizations"):
                show_visualizations(data)
                
            if st.checkbox("Download Processed Data"):
                download_data(data)
                
        except Exception as e:
            st.error(f"An error occurred: {e}")
            
def preview_data(data):
    st.subheader("Dataset Preview")
    if st.button("Head"):
        st.write(data.head())
    if st.button("Tail"):
        st.write(data.tail())

def show_data_types(data):
    st.subheader("Data Types")
    st.write(data.dtypes)
    
def show_shape(data):
    data_shape = st.radio("What dimension do you want to see?", ('Rows', 'Columns'))
    if data_shape == 'Rows':
        st.text("Number of rows")
        st.write(data.shape[0])
    else:
        st.text("Number of columns")
        st.write(data.shape[1])
        
def check_null_values(data):
    if data.isnull().values.any():
        st.warning("This dataset contains null values.")
        sns.heatmap(data.isnull(), cbar=False, cmap='viridis')
        st.pyplot(plt)
    else:
        st.success("No missing data in this dataset.")
        
def check_duplicates(data):
    if data.duplicated().any():
        st.warning("This dataset contains duplicate values.")
        if st.button("Remove Duplicates"):
            data.drop_duplicates(inplace=True)
            st.success("Duplicate values removed.")
    else:
        st.success("No duplicate values found.")
        
def show_summary(data):
    st.subheader("Summary Statistics")
    st.write(data.describe(include='all'))
    
def show_visualizations(data):
    st.subheader("Data Visualizations")
    st.write("Histograms")
    for column in data.select_dtypes(include=['float64', 'int64']).columns:
        st.write(f"Distribution of {column}")
        sns.histplot(data[column], kde=True)
        st.pyplot(plt)
        
    st.write("Pairplot")
    sns.pairplot(data.select_dtypes(include=['float64', 'int64']).dropna())
    st.pyplot(plt)
    
    st.write("Box Plots")
    for column in data.select_dtypes(include=['float64', 'int64']).columns:
        st.write(f"Box plot of {column}")
        sns.boxplot(x=data[column])
        st.pyplot(plt)
        
    st.write("Correlation Heatmap")
    corr = data.corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    st.pyplot(plt)
    
def download_data(data): 
    st.subheader("Download Processed Data")
    csv = data.to_csv(index=False)
    st.download_button(label="Download CSV", data=csv, file_name='processed_data.csv', mime='text/csv') 
    
if __name__ == "__main__":
    main()