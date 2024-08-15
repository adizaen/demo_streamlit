import streamlit as st

import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Loan Analytics Dashboard",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("<h1 style='text-align: center;'>Financial Insights Dashboard: <br> Loan Performance & Trends</h1>", unsafe_allow_html=True)

st.markdown("---")

# Sidebar section
st.sidebar.title("Dashboard Filters and Features")

# List of Features
st.sidebar.header("Features")
st.sidebar.write("""
- **Overview**: Provides a summary of key loan metrics.
- **Loan Performance**: Analyzes loan conditions and distributions.
- **Financial Analysis**: Examines loan amounts and distributions based on conditions.
- **Time-Based Analysis**: Shows trends over time and loan amounts.
""")


## ----- Import Data ------
loan = pd.read_pickle('data_input/loan_clean')

### ******* SELECT BOX **********
# List unique loan conditions for the selectbox
loan_conditions = loan['loan_condition'].unique()

# Create a selectbox in the sidebar for filtering loan conditions
selected_condition = st.selectbox(
    "Select Loan Condition",
    options=loan_conditions,
    index=0  # Default selected index
)

# Filter data based on selected loan condition
condition = loan[loan['loan_condition'] == selected_condition]

### -------------- Wrangling And Visualization

# **1. Loan Amount Distribution**
loan_amount_hist = px.histogram(
    condition,
    x='loan_amount',
    nbins=30,  # Number of bins in the histogram
    color='term',
    title='Loan Amount Distribution by Condition',
    template='seaborn',
    labels={
        'loan_amount': 'Loan Amount',
        'term': 'Loan Term'
    }
)

# **2. Loan Amount Distribution by Purpose**
loan_amount_box = px.box(
    condition,
    x='purpose',
    y='loan_amount',
    color='term',
    title='Loan Amount Distribution by Purpose',
    template='seaborn',
    labels={
        'loan_amount': 'Loan Amount',
        'term': 'Loan Term',
        'purpose': 'Loan Purpose'
    }
)

### ------- Display Dashboard
with st.container(border=True):

    tab1, tab2 = st.tabs([
        'Loan Amount Distribution',
        'Loan Amount Distribution by Purpose',
    ])

    with tab1:
        st.plotly_chart(loan_amount_hist)

    with tab2:
        st.plotly_chart(loan_amount_box)


import plotly.express as px
df = px.data.gapminder()
mind = px.scatter(df, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
           size="pop", color="continent", hover_name="country",
           log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90])

st.plotly_chart(mind)