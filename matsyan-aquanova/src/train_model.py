import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.linear_model import LinearRegression
import joblib

# Load your simulated sensor data
df = pd.read_csv("sensor_data.csv")  # Replace with your filename

# --- Anomaly Detection Model ---
X = df[["temperature", "turbidity", "salinity", "oxygen"]]
anomaly_model = IsolationForest(contamination=0.1)
anomaly_model.fit(X)
joblib.dump(anomaly_model, "anomaly_model.pkl")

# --- Predictive Model (Temperature Forecast) ---
last_10 = df["temperature"].tail(10).values.reshape(-1, 1)
steps = np.array(range(10)).reshape(-1, 1)
reg_model = LinearRegression()
reg_model.fit(steps, last_10)
joblib.dump(reg_model, "temp_predict_model.pkl")

print(" Models trained and saved.")
