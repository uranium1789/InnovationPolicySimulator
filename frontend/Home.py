import streamlit as st
import pandas as pd

         
# PAGE CONFIG
         

st.set_page_config(
    page_title="Innovation Policy Simulator",
    page_icon="📈",
    layout="wide"
)

         
# TITLE SECTION
         

st.title(
    "A ML Framework for Precision Funding and ROI Maximisation in the Context of India's Innovation Policy"
)

st.markdown(
"""
### Capstone-II Project

**Indian Institute of Technology Patna**

**Group No.** -  111

---
"""
)

         
# LOAD DATASET
         

try:
    df = pd.read_excel("data/innovation_dataset.xlsx")

    st.success("Dataset Loaded Successfully")

             
    # KPI CARDS
             

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Records",
        df.shape[0]
    )

    col2.metric(
        "Total Features",
        df.shape[1]
    )

    if "Year" in df.columns:
        col3.metric(
            "Years Covered",
            f"{df['Year'].min()} - {df['Year'].max()}"
        )
    else:
        col3.metric(
            "Years Covered",
            "N/A"
        )

    st.divider()

             
    # DATA PREVIEW
             

    st.subheader("Dataset Preview")

    st.dataframe(df.head())

    st.divider()

             
    # COLUMN NAMES
             

    st.subheader("Dataset Columns")

    st.write(df.columns.tolist())

except Exception as e:
    st.error(f"Error Loading Dataset: {e}")

    