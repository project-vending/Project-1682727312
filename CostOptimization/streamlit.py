python
import streamlit as st
import pandas as pd

# Load the data
cost_data = pd.read_csv("cost_data.csv")

# Display the dashboard
st.title("Cost Optimization Dashboard")

# Define the widgets
start_date = st.date_input("Select start date", value=pd.to_datetime(cost_data["date"]).min())
end_date = st.date_input("Select end date", value=pd.to_datetime(cost_data["date"]).max())

# Filter the data based on the selected dates
filtered_data = cost_data[(pd.to_datetime(cost_data["date"]) >= start_date) & (pd.to_datetime(cost_data["date"]) <= end_date)]

# Display the data
st.header("Filtered Data")
st.write(filtered_data)

# Display insights about the data
total_cost = filtered_data["cost"].sum()
average_cost = filtered_data["cost"].mean()

st.header("Cost Insights")
st.write(f"Total cost: ${total_cost:,.2f}")
st.write(f"Average cost: ${average_cost:,.2f}")
