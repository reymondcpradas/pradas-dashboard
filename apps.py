
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Palay Forecasting Dashboard",
    page_icon="🌾",
    layout="wide"
)

st.title("🌾 Palay Production Forecasting Dashboard")
st.subheader("Agusan del Sur | 2021–2025")

uploaded_file = st.file_uploader(
    "Upload your Palay Excel Dataset",
    type=["xlsx"]
)

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)

    st.success("Dataset uploaded successfully!")

    st.subheader("Dataset Preview")
    st.dataframe(df, use_container_width=True)

    st.subheader("Data Visualization")

    numeric_cols = df.select_dtypes(
        include="number"
    ).columns.tolist()

    if "Year" in df.columns:
        options = [c for c in numeric_cols if c != "Year"]

        if options:
            selected = st.selectbox(
                "Select Indicator",
                options
            )

            fig = px.line(
                df,
                x="Year",
                y=selected,
                markers=True,
                title=f"{selected} Trend"
            )

            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No numeric indicators found.")
    else:
        st.warning("Your dataset needs a Year column.")
else:
    st.info("Upload your Excel dataset to begin.")
