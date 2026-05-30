import streamlit as st
import pandas as pd
import plotly.express as px

# ----------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------

st.set_page_config(
    page_title="Innovation Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Innovation Analytics Dashboard")

# ----------------------------------------------------
# LOAD DATA
# ----------------------------------------------------

df = pd.read_excel(
    "data/innovation_dataset.xlsx",
    engine="openpyxl"
)

# ----------------------------------------------------
# CLEAN DATA
# ----------------------------------------------------

numeric_cols = [
    "Patent (NR)",
    "GDP",
    "GDPPC",
    "FDI inflows(% of GDP)",
    "Tradeopen",
    "R&D investment(%of GDP)",
    "Individuals using intrnet",
    "Broadband",
    "Broadband(100)"
]

for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        )

# ----------------------------------------------------
# KPI SECTION
# ----------------------------------------------------

latest_patent = df["Patent (NR)"].dropna().iloc[-1]

latest_gdp = df["GDP"].dropna().iloc[-1] / 1e12

latest_rd = df["R&D investment(%of GDP)"].dropna().iloc[-1]

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Years Covered",
        df["Year"].nunique()
    )

with col2:
    st.metric(
        "Latest Patent Count",
        f"{int(latest_patent):,}"
    )

with col3:
    st.metric(
        "GDP (Trillion USD)",
        f"{latest_gdp:.2f}"
    )

with col4:
    st.metric(
        "Latest R&D %",
        f"{latest_rd:.2f}"
    )

st.divider()

# ----------------------------------------------------
# ROW 1
# ----------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    fig1 = px.line(
        df,
        x="Year",
        y="Patent (NR)",
        markers=True,
        title="Patent Trend (2000–2023)"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

with col2:

    fig2 = px.line(
        df,
        x="Year",
        y="GDP",
        markers=True,
        title="GDP Trend"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

# ----------------------------------------------------
# ROW 2
# ----------------------------------------------------

col3, col4 = st.columns(2)

with col3:

    fig3 = px.line(
        df,
        x="Year",
        y="R&D investment(%of GDP)",
        markers=True,
        title="R&D Investment Trend"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

with col4:

    fig4 = px.line(
        df,
        x="Year",
        y="Individuals using intrnet",
        markers=True,
        title="Internet Adoption Trend"
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

# ----------------------------------------------------
# ROW 3
# ----------------------------------------------------

col5, col6 = st.columns(2)

with col5:

    fig5 = px.line(
        df,
        x="Year",
        y="FDI inflows(% of GDP)",
        markers=True,
        title="FDI Inflows Trend"
    )

    st.plotly_chart(
        fig5,
        use_container_width=True
    )

with col6:

    fig6 = px.line(
        df,
        x="Year",
        y="Broadband(100)",
        markers=True,
        title="Broadband Penetration Trend"
    )

    st.plotly_chart(
        fig6,
        use_container_width=True
    )

# ----------------------------------------------------
# DATA TABLE
# ----------------------------------------------------

with st.expander("📄 View Dataset"):
    st.dataframe(df)