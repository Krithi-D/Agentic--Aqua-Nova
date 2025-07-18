# MatysaN-Aqua-Nova
# Smart Marine Health Monitoring Using AI-Enabled Buoy System  
**Team Name:** Aqua Nova  
**Team Members** 
1. Dharshini R
2. Krithi D
3. Dheekshitha R
4. Dharanisri T

---

## 🔍 Problem Statement  
Oceans are under constant threat from pollution, climate change, and unregulated human activity. Traditional water monitoring is manual and delayed, which limits rapid response to threats like algal blooms, oil spills, or oxygen depletion.  

This project aims to create an **AI-powered smart buoy system** that can continuously track ocean parameters, detect anomalies, and send real-time alerts to local authorities and stakeholders.

---

## 💡 Our Solution  
We simulate a **solar-powered smart buoy** with sensors that monitor:
- Temperature  
- Salinity  
- Turbidity  
- pH  
- Dissolved Oxygen  
- Oil Spill Detection  
- Microplastics  
- GPS location

  Location-Based Data + Conditions
Sensors on the buoy track location (GPS), temperature, turbidity, pH, sulfate, and oxygen

Weather data like rainfall, sunlight, and wind can be added from open APIs like OpenWeather

Geo-fencing helps set up alert zones (restricted or high-risk areas)

![WhatsApp Image 2025-07-18 at 09 34 54_173c5447](https://github.com/user-attachments/assets/abfb9356-2c2d-428a-8e68-861fb89c7028)

How the Buoy Communicates
The buoy is assumed to be fitted with multi-parameter sensors

Data is transmitted via LoRa (for long-range, low-power coastal communication)

The GPS module tracks drift or movement

A small onboard system pushes data to the cloud or local dashboard using Wi-Fi/GSM fallback

The system:
- Sends real-time data to a simulated backend  
- Uses basic ML for anomaly detection  
- Calculates a Marine Health Index score  
- Shows everything on a live dashboard  
- Sends alerts when environmental thresholds are crossed

![WhatsApp Image 2025-07-18 at 09 35 30_6f35da2e](https://github.com/user-attachments/assets/73e51806-72de-40cf-90b9-f69215510862)

🔄 Sensing + Data Processing
Data collected: Temperature, pH, Turbidity, Sulfate, Dissolved Oxygen, etc.

Total: ~4000+ rows of data used for training and testing

Not real-time for now – data used is from public datasets (like Kaggle) to simulate
![WhatsApp Image 2025-07-18 at 09 34 26_6d292c18](https://github.com/user-attachments/assets/f392778d-49e6-42ed-b7fa-c8e26955ea89)

---

## 🧰 Tech Stack Used  
| Area | Tools |
|------|-------|
| Simulation | Python |
| Frontend | HTML, CSS, JavaScript |
| Dashboard | Firebase (optional), Google Maps API |
| ML | Python (basic anomaly detection) |
| Hosting | GitHub Pages / Hostinger |
| Visualization | Google Maps, Custom Chart Elements |

---

## 🛠️ Installation & Setup  

1. Clone this repo  
git clone https://github.com/YOUR-USERNAME/matsyan-aquanova.git
cd matsyan-aquanova

2. Run the simulation
cd src
python simulate_data.py

3. (Optional) Run anomaly detection

python anomaly_detector.py

4. Open the dashboard
Open src/dashboard/index.html in your browser.

 HARDWARE SIMULATION 

 
🎯 Objective:
To continuously monitor marine parameters and provide a Marine Health Index using real-time data from various sensors, aiding in early detection of water pollution and ecological threats.

📍 Platform:
Wokwi Simulator

ESP32 Microcontroller

🧰 Hardware Components (Simulated):
Sensor	Function	ESP32 Pin
DHT22	Temperature & Humidity	15
Potentiometer (x6)	Simulated analog sensors	25–36
Turbidity Sensor	Water clarity	34
Salinity Sensor	Salt content (simulated)	36
pH Sensor	Acidity/alkalinity level	35
DO Sensor	Dissolved Oxygen	34
Oil Density Sensor	Oil spill detection	32
LIF Sensor	Microplastics detection	25

📊 Parameters Monitored
🌡 Temperature
🧂 Salinity
🌫 Turbidity
🧪 pH Level
🫧 Dissolved Oxygen (DO)
🛢 Oil Density
♻️ LIF Sensor (Microplastics)

⚙️ Functionality
Reads real-time data from sensors.

Normalizes readings to a 0–100 scale.

Calculates individual scores for each parameter.

Combines scores into a final Marine Health Index (MHI).

Detects:

Oil spills

Microplastics

Displays readable output in the serial monitor.

STEPS:

1.Go to Wokwi Arduino Simulator
   Create a new project using the ESP32 Dev Board.

2.Add Components:
   Add an ESP32 Dev Module
   Add a DHT22 sensor
   Add potentiometers (for salinity, pH, viscosity, oxygen, oil density, and LIF)
   Add a turbidity sensor (can be simulated with another analog sensor or potentiometer)

3.Wire the Circuit:

     Connect all sensors to the ESP32:

DHT22       -> GPIO15
Salinity    -> GPIO36
Turbidity   -> GPIO39
Oxygen      -> GPIO34
PH          -> GPIO35
Viscosity   -> GPIO32
Oil Density -> GPIO33
LIF         -> GPIO25
Use the analogRead() pins for potentiometers.

Provide 3.3V or 5V and GND accordingly.

4.Upload the Code:
    Copy the code from sketch.ino.
    Paste it into Wokwi's code editor.

5.Start Simulation:
    Click the green Start Simulation ▶️ button.
    Open the Serial Monitor to view readings.

🔁 Normalization Logic
cpp
Copy
Edit
float normalize(int val, int in_min, int in_max) {
  return constrain((float)(val - in_min) / (in_max - in_min) * 100.0, 0, 100);
}
Each sensor value is normalized to ensure equal weighting in the final MHI calculation.

📦 Project Files
sketch.ino - Main Arduino code.

diagram.json - Wokwi simulation wiring.

libraries.txt - List of required libraries.

README.md - Project documentation.

🧪 Sample Output (Serial Monitor)
yaml
Copy
Edit
Turbidity: 1001 | Score: 75.6
Dissolved O2: 0 | Score: 0.0
pH: 0 | Score: 0.0
Oil Spill Detected: NO
Microplastics Detected: NO
🌊 Marine Health Index: 45.8 / 100
📈 Future Improvements
Cloud integration (e.g., ThingsBoard, Firebase).

SMS/email alerts for anomaly detection.

Solar charging simulation.

Real GPS coordinates via a map.

👩‍💻 Developed Using
Language: C++ (Arduino)

Simulator: Wokwi IoT & MCU Simulator

Microcontroller: ESP32 Dev Board

-------------------------------------------------------------------------------------------------------------------------
## 🔍 Aqua Nova – ML Model for Anomaly Detection & Prediction
<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/09569dce-bf86-45e7-8d94-592af6b581a5" />

-The goal of this ML model is to detect anomalies in water parameters like pH, turbidity, and sulfate, and to predict future temperature and dissolved oxygen levels using simple linear regression. 
-It focuses on detecting harmful changes in water quality using machine learning and forecasting future conditions to support early warning systems for coastal authorities, fisheries, and researchers.

## 🧠 What This Module Solves
-Monitors water health using real-time sensor data.
-Detects pollution events or abnormal conditions and dangerous shifts in temperature, oxygen levels, turbidity, salinity, or pH using anomaly detection.
-Predicts future values of temperature and oxygen levels using real-time inputs to raise early alerts
Sends alerts to local authorities, fishers, and research teams.


##⚙️ Tech Stack Used
  Tool/Library	    |    Why We Used It
    Python	        | Easy to write and test models, highly readable
    Pandas	        | For working, handling and cleaning the water quality datasets
  Scikit-learn	    | For training ML models (Isolation Forest, Linear Regression)
   Matplotlib       |	For visualising anomalies and the prediction of results early
  Google Colab	    | For easy cloud-based coding, fast prototyping, no setup required, with GPU/CPU access

##🧪 Anomaly Detection
-We used Isolation Forest for anomaly detection.
-It checks if the water conditions are normal or suspicious

## Sends alerts/Flags:
-Sudden temperature spikes
-Dangerous drops in dissolved oxygen
-Unusual turbidity or salinity
-Patterns possibly caused by microplastics or pollution

We plotted the results using matplotlib, which helps visually identify where the pH is unusually low or high compared to turbidity values.

## 📈 Predictive Analysis
-Model used: Linear Regression
-Predicts water conditions for the next 15 minutes or more
## Example:
-Forecasts a drop in oxygen → alerts fishers in advance
-Predicts heat buildup → warns aquaculture centres or researchers


## 🧾 Files Included
Aqua_Nova.ipynb      – Google Colab notebook for training Isolation Forest and for temperature & oxygen forecasting
forecast_results.csv – Sample output of predictions
assets/              – Folder with charts and output visuals

## 📦 How to Run This on Your Device (Step-by-Step)
-You can run this with no installation using Google Colab.
## Run in Google Colab (Recommended)
## Open the notebook:
Click on the .ipynb file (Aqua_Nova.ipynb)
Click the "Open in Colab" button

Upload the dataset:
-Download water_potability.csv (For the Anomaly Detection)


<img width="1440" height="625" alt="image" src="https://github.com/user-attachments/assets/d3d785d9-64e6-4152-acf5-87c97792350a" />

<img width="1349" height="648" alt="image" src="https://github.com/user-attachments/assets/5c469c53-6152-436b-9271-6543e880f777" />



Upload via Files > Upload in Colab
-Run the cells (Shift + Enter) one by one
-Run all cells from top to bottom

-The first part trains the model
<img width="679" height="264" alt="image" src="https://github.com/user-attachments/assets/500a4ad9-e8ba-4bf3-81d1-18c563de49be" />

-Then it predicts anomalies or future values
 Predicts the next 5 values for Turbidity
 <img width="1459" height="416" alt="image" src="https://github.com/user-attachments/assets/4050f3ed-7f6e-45f6-8bfc-2919df8d6ff3" />

-Download temp, oxygen data set.csv (For Predictive Analysis):
<img width="1048" height="552" alt="image" src="https://github.com/user-attachments/assets/21bb64e5-c78e-48ab-898c-0fff70bb13d6" />

-Final cells plot the graphs

## 🔬 How the Model Works
1. Anomaly Detection using Isolation Forest
We use pH, turbidity, and sulfate as input features
The model learns normal patterns from the data
Then it flags abnormal water conditions (e.g., toxic spills, chemical spikes)

2. Prediction using Linear Regression
   <img width="609" height="566" alt="image" src="https://github.com/user-attachments/assets/ff69017e-3f08-4375-a285-49ea480da9d8" />

Input: time in minutes
Output: predicted temperature (°C) and dissolved oxygen (mg/L)
The model fits a straight line to historical data and forecasts future trends

## 📊 Output Examples
Scatter plot showing anomalies in red and normal data in blue
Line graph showing actual vs predicted temperature and oxygen levels
## 📊 Output
-Graphs show:
Anomaly points (normal vs abnormal)
Line chart of actual vs predicted temperature and oxygen
Output is also saved in CSV for further processing or dashboard integration

<img width="1920" height="897" alt="anamoly detection" src="https://github.com/user-attachments/assets/e75f61df-ae58-440c-aefc-856475a33397" />

<img width="1920" height="898" alt="oxygen prediction" src="https://github.com/user-attachments/assets/b52809a8-4a2b-4cf1-b2ba-fa015d243d23" />

<img width="1920" height="898" alt="temperature prediction" src="https://github.com/user-attachments/assets/3d5aeab3-ba15-4048-b776-c547fb5d2f93" />

## 🚨 Alert System
When an anomaly or dangerous forecast is detected:
-Instant alert can be sent to fishers, researchers, or Coast Guard
-Format: Email, SMS, or push notification
-Alerts are location-aware and tagged with sensor timestamp
![WhatsApp Image 2025-07-18 at 09 33 55_4b02deb2](https://github.com/user-attachments/assets/a1ad7a8c-4459-4537-b08b-0472eed3c9e0)


## 🧪 Sample Use Cases
-Predict algal blooms, oxygen depletion, or thermal pollution
-Alert aquaculture teams or coastal authorities before disaster strikes

This tool is useful for:
-Local authorities for pollution control
-Fisheries to monitor algal bloom risks, oxygen levels, and water salinity
-Marine researchers studying climate impact, microplastics, or fish mortality


## 🔮 What’s Next (Future Scope)
-Add real-time data ingestion from sensors via MQTT or REST APIs
-Build a mobile app for fishermen with weather + water insights
-Integrate satellite imagery for algal bloom detection
-Improve model accuracy using time-series models (e.g., LSTM)

## 💼 Business Model
Fisheries: Healthier yield, early pollution alerts
Govt Authorities, Environmental monitoring, quick response
Researchers'	Long-term marine studies & pollution data


NGOs, 	Clean water campaigns & reporting

## Revenue Stream:
-SaaS dashboard for water monitoring
-Paid API access to real-time forecasts
-Subscription plans for research or fisheries
-Hardware kits (buoy + LoRa + sensors)



