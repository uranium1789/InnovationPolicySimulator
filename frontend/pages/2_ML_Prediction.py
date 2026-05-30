import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

st.set_page_config(
    page_title="ML Prediction Engine",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Innovation Prediction Engine")

BASE_DIR = Path(__file__).resolve().parent.parent.parent

model = joblib.load(
    BASE_DIR / "models" / "xgb_model.pkl"
)

st.subheader("Policy Inputs")

col1, col2 = st.columns(2)

with col1:
    gdppc = st.number_input("GDP Per Capita", value=2500.0)
    fdi = st.number_input("FDI (% GDP)", value=2.0)
    trade = st.number_input("Trade Openness", value=40.0)
    rd = st.number_input("R&D Investment (% GDP)", value=0.7)

with col2:
    internet = st.number_input("Internet Users (%)", value=45.0)
    broadband = st.number_input("Broadband(100)", value=20.0)
    export = st.number_input("Export", value=300.0)
    imp = st.number_input("Import", value=350.0)

if st.button("🚀 Predict Patent Count"):

    X = pd.DataFrame([[
        gdppc,
        fdi,
        trade,
        rd,
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

    prediction = model.predict(X)[0]

    st.success(
        f"Predicted Patent Count: {prediction:,.0f}"
    )