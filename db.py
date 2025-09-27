import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

def get_engine():
    engine = create_engine(
        f"postgresql+psycopg2://{st.secrets['postgres']['user']}:{st.secrets['postgres']['password']}@"
        f"{st.secrets['postgres']['host']}:{st.secrets['postgres']['port']}/{st.secrets['postgres']['dbname']}"
        "?sslmode=require"
    )
    return engine

def run_query(query):
    engine = get_engine()
    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
    return df

