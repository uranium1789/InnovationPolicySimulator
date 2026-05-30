import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Budget Impact Simulator",
    page_icon="💰",
    layout="wide"
)

st.title("💰 Budget Impact Simulator")

st.write(
    """
    This module simulates the effect of increased R&D investment
    on innovation output using the trained XGBoost model.
    """
)

# =====================================================
# LOAD MODEL
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent.parent

model = joblib.load(
    BASE_DIR / "models" / "xgb_model.pkl"
)

# =====================================================
# INPUTS
# =====================================================

st.subheader("Current Scenario")

col1, col2 = st.columns(2)

with col1:

    gdppc = st.number_input(
        "GDP Per Capita",
        value=2500.0
    )

    fdi = st.number_input(
        "FDI Inflows (% GDP)",
        value=2.0
    )

    trade = st.number_input(
        "Trade Openness",
        value=40.0
    )

with col2:

    export = st.number_input(
        "Exports",
        value=300.0
    )

    imp = st.number_input(
        "Imports",
        value=350.0
    )

    internet = st.number_input(
        "Internet Users (%)",
        value=45.0
    )

# =====================================================
# R&D SCENARIO
# =====================================================

st.subheader("Funding Simulation")

current_rd = st.slider(
    "Current R&D Investment (% GDP)",
    0.0,
    5.0,
    0.7
)

target_rd = st.slider(
    "Target R&D Investment (% GDP)",
    0.0,
    5.0,
    1.2
)

broadband = st.slider(
    "Broadband Penetration",
    0.0,
    100.0,
    20.0
)

# =====================================================
# SIMULATE
# =====================================================

if st.button("Run Simulation"):

    current_input = pd.DataFrame([[
        gdppc,
        fdi,
        trade,
        current_rd,
        export,
        imp,
        internet,
        broadband
    ]], columns=[
        "GDPPC",
        "FDI inflows(% of GDP)",
        "Tradeopen",
        "R&D investment(%of GDP)",
        "Export",
        "Import",
        "Individuals using intrnet",
        "Broadband(100)"
    ])

    target_input = pd.DataFrame([[
        gdppc,
        fdi,
        trade,
        target_rd,
        export,
        imp,
        internet,
        broadband
    ]], columns=current_input.columns)

    current_prediction = model.predict(current_input)[0]

    target_prediction = model.predict(target_input)[0]

    increase = target_prediction - current_prediction

    growth_pct = (
        increase / current_prediction
    ) * 100

    st.divider()

    st.subheader("Simulation Results")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Current Patent Output",
            f"{current_prediction:,.0f}"
        )

    with col2:
        st.metric(
            "Predicted Patent Output",
            f"{target_prediction:,.0f}"
        )

    with col3:
        st.metric(
            "Growth (%)",
            f"{growth_pct:.2f}%"
        )

    st.success(
        f"""
        Increasing R&D expenditure from
        {current_rd:.2f}% to {target_rd:.2f}% GDP
        is estimated to increase patent output by
        approximately {increase:,.0f}.
        """
    )