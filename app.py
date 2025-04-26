import streamlit as st

st.title("Snowflake Data Viewer")

conn = st.connection("snowflake", type="sql")

df = conn.query("SELECT * FROM SMOOTHIES”.PUBLIC.FRUIT_OPTIONS, ttl=600)

st.dataframe(df)
