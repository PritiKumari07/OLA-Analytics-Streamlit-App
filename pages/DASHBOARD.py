import streamlit as st
import streamlit.components.v1 as components

# Title for your Streamlit app
st.title("📊 OLA Dataset Analysis Dashboard")

# Tableau Public embed URL
tableau_url = "https://public.tableau.com/views/OLADATASETANALYSIS/Dashboard1?:showVizHome=no&:embed=true"

# Embed the Tableau dashboard
components.html(f"""
<div style="width: 100%; display: flex; justify-content: center;">
    <iframe 
        src="{tableau_url}" 
        style="width: 100%; max-width: 1200px; height: 827px; border: none;"
        allowfullscreen
    ></iframe>
</div>
""", height=850)