import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("C:/Users/asavela.ludidi/Desktop/Data Science/Streamlit/Salary_Data.csv")
st.write(data.shape)
st.write(data.head())
st.subheader("Dataset Information")
st.write(data.describe())
x=data['YearsExperience']
st.write(x)
y=data['Salary']
st.write(y)
fig, ax=plt.subplots(figsize=(10,5))
plt.scatter(x,y)
st.pyplot(fig)