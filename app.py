import streamlit as st
import pandas as pd
import chardet

st.header("💡 CSV uploader with auto-encoding")

uploaded_file = st.file_uploader("Choose a CSV file")

if uploaded_file is not None:

    result = chardet.detect(uploaded_file.getvalue())
    # Get encoding value
    encoding_value = result["encoding"]
    df = pd.read_csv(
        uploaded_file,
        encoding=encoding_value,
    )
    # Print encoding value
    st.caption("File encoding is 👉'" + str(encoding_value) + "'")
    st.write(df)
