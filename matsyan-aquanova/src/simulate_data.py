import random
from datetime import datetime
import json

def generate_sensor_data():
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "temperature": round(random.uniform(23.0, 34.0), 2),
        "salinity": round(random.uniform(30.0, 40.0), 2),
        "turbidity": round(random.uniform(5.0, 45.0), 2),
        "ph": round(random.uniform(6.8, 8.5), 2),
        "oxygen": round(random.uniform(3.0, 9.0), 2),
        "microplastics": round(random.uniform(50, 150), 2),
        "oil_spill": random.choice([0, 1]),
        "gps": {"lat": 12.91, "lon": 80.23}
    }

if __name__ == "__main__":
    for _ in range(10):
        data = generate_sensor_data()
        print(json.dumps(data, indent=2))
