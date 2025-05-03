import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("AlgoTrade Analyzer - Basic Version")
st.write("This is a minimal version to ensure deployment works.")

# Create some sample data
data = pd.DataFrame({
    'Date': pd.date_range(start='2023-01-01', periods=30),
    'Profit': np.random.normal(100, 50, 30).cumsum(),
    'Pnl_Percentage': np.random.normal(0.5, 2, 30)
})

# Display basic chart
st.line_chart(data.set_index('Date')['Profit'])

# Display metrics
col1, col2 = st.columns(2)
with col1:
    st.metric("Total Profit", f"${data['Profit'].iloc[-1]:.2f}")
with col2:
    st.metric("Win Rate", f"{(data['Profit'] > 0).mean() * 100:.1f}%")

# Show data table
st.dataframe(data)
