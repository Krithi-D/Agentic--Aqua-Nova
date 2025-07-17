def check_anomaly(data):
    alerts = []
    if data["temperature"] > 32:
        alerts.append("High Temperature")
    if data["turbidity"] > 35:
        alerts.append("Turbidity Spike")
    if data["oxygen"] < 4:
        alerts.append("Low Oxygen Level")
    if data["oil_spill"] == 1:
        alerts.append("Oil Spill Detected")
    return alerts

if __name__ == "__main__":
    from simulate_data import generate_sensor_data
    data = generate_sensor_data()
    print("Data:", data)
    print("Alerts:", check_anomaly(data))
