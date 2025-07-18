# Agentic--Aqua-Nova
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


🔄 Sensing + Data Processing
Data collected: Temperature, pH, Turbidity, Sulfate, Dissolved Oxygen, etc.

Total: ~4000+ rows of data used for training and testing

Not real-time for now – data used is from public datasets (like Kaggle) to simulate
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

-------------------------------------------------------------------------------------------------------------------------
## 🔍 Aqua Nova – ML Model for Anomaly Detection & Prediction
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

##📦 How to Run This on Your Device (Step-by-Step)
-You can run this with no installation using Google Colab.
##Run in Google Colab (Recommended)
##Open the notebook:
Click on the .ipynb file (Aqua_Nova.ipynb)
Click the "Open in Colab" button

Upload the dataset:
-Download water_potability.csv (For the Anomaly Detection)
-Download temp, oxygen data set.csv (For Predictive Analysis)

Upload via Files > Upload in Colab
-Run the cells (Shift + Enter) one by one
-Run all cells from top to bottom

-The first part trains the model
-Then it predicts anomalies or future values
-Final cells plot the graphs

## 🔬 How the Model Works
1. Anomaly Detection using Isolation Forest
We use pH, turbidity, and sulfate as input features
The model learns normal patterns from the data
Then it flags abnormal water conditions (e.g., toxic spills, chemical spikes)

2. Prediction using Linear Regression
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

## 🚨 Alert System
When an anomaly or dangerous forecast is detected:
-Instant alert can be sent to fishers, researchers, or Coast Guard
-Format: Email, SMS, or push notification
-Alerts are location-aware and tagged with sensor timestamp

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
