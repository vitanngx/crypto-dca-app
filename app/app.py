import streamlit as st
import pandas as pd

st.title("Hello, Streamlit 👋")

file = st.file_uploader("Upload a CSV", type=["csv"])
if file:
    df = pd.read_csv(file)
    st.dataframe(df.head())
    # nếu cột đầu là ngày, cột thứ 2 là giá:
    st.line_chart(df.set_index(df.columns[0]).iloc[:, 1])
else:
    st.info("Upload a CSV to preview & plot.")
