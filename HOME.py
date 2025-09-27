import streamlit as st


st.set_page_config(page_title="Home", layout="wide")
st.title("🏠 Welcome to the Ola Data Analytics App!")

st.write("""Problem Statement:
The rise of ride-sharing platforms has transformed urban mobility, offering convenience and affordability to millions of users. OLA, a leading ride-hailing service, generates vast amounts of data related to ride bookings, driver availability, fare calculations, and customer preferences. However, deriving actionable insights from this data remains a challenge. To enhance operational efficiency, improve customer satisfaction, and optimize business strategies, this project focuses on analyzing OLA’s ride-sharing data. By leveraging data analytics, visualization techniques, and interactive applications, the goal is to extract meaningful insights that can drive data-informed decisions. The project will involve cleaning and processing raw ride data, performing exploratory data analysis (EDA), developing a dynamic Power BI dashboard, and creating a Streamlit-based web application to present key findings in an interactive and user-friendly manner.
""")

st.subheader("About This Project")
st.write("""
    * This project aims to provide insights into Ola's ride-hailing data.
    * Users can explore various SQL queries to analyze booking patterns, customer behavior, and driver performance.
    * The data is sourced from a PostgreSQL database and visualized using Streamlit.
    * Navigate through the sidebar to access different SQL queries and their results.

""")