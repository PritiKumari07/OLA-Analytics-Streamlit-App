import streamlit as st

st.set_page_config(page_title="Dashboard", layout="wide")

st.title("📊 Ola Analytics Dashboard")

st.write("Below is the integrated dashboard from Tableau/Power BI.")

tableau_url = "https://public.tableau.com/app/profile/priti.kumari2802/viz/OLADATASETANALYSIS/Dashboard1"
st.markdown(f'<iframe src="{tableau_url}" width="100%" height="600"></iframe>', unsafe_allow_html=True)