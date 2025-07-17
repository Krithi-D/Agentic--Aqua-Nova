import joblib
import numpy as np

# Example sensor input (replace this with live or simulated data)
input_data = [[30.5, 20.1, 36.5, 5.4]]  # temp, turbidity, salinity, oxygen

# Load trained models
anomaly_model = joblib.load("anomaly_model.pkl")
reg_model = joblib.load("temp_predict_model.pkl")

# Predict anomaly
anomaly_result = anomaly_model.predict(input_data)[0]
print("Anomaly:", "YES" if anomaly_result == -1 else "NO")

# Predict next temperature
next_temp = reg_model.predict([[10]])[0][0]
print(f"Predicted next temp: {next_temp:.2f} °C")
