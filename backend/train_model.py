import pandas as pd
import joblib

from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# -------------------------
# LOAD DATA
# -------------------------

df = pd.read_excel(
    "data/innovation_dataset.xlsx",
    engine="openpyxl"
)

# -------------------------
# CLEAN DATA
# -------------------------

features = [
    "GDPPC",
    "FDI inflows(% of GDP)",
    "Tradeopen",
    "R&D investment(%of GDP)",
    "Export",
    "Import",
    "Individuals using intrnet",
    "Broadband(100)"
]

target = "Patent (NR)"

for col in features + [target]:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

df = df.dropna()

# -------------------------
# TRAIN
# -------------------------

X = df[features]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = XGBRegressor(
    n_estimators=200,
    max_depth=4,
    learning_rate=0.05,
    random_state=42
)

model.fit(X_train, y_train)

pred = model.predict(X_test)

score = r2_score(y_test, pred)

print(f"R2 Score = {score:.4f}")

# -------------------------
# SAVE MODEL
# -------------------------

joblib.dump(
    model,
    "models/xgb_model.pkl"
)

print("Model Saved Successfully")