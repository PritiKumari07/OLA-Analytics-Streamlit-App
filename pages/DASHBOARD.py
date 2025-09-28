import streamlit as st
import streamlit.components.v1 as components

# Title for your Streamlit app
st.title("📊 OLA Dataset Analysis Dashboard")

# Tableau Public embed URL
tableau_url = "https://public.tableau.com/views/OLADATASETANALYSIS/Dashboard1?:showVizHome=no&:embed=true"

# Embed the Tableau dashboard
components.html(f"""
<html>
  <head>
    <style>
      html, body {{
        margin: 0;
        padding: 0;
        height: 100%;
        width: 100%;
      }}
      iframe {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        border: none;
      }}
    </style>
  </head>
  <body>
    <iframe src="{tableau_url}" allowfullscreen></iframe>
  </body>
</html>
""", height=900)