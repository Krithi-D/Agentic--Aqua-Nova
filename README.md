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

The system:
- Sends real-time data to a simulated backend  
- Uses basic ML for anomaly detection  
- Calculates a Marine Health Index score  
- Shows everything on a live dashboard  
- Sends alerts when environmental thresholds are crossed

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


🔍 Aqua Nova – ML Model for Anomaly Detection & Prediction
The goal of this ML model is to detect anomalies in water parameters like pH, turbidity, and sulfate, and to predict future temperature and dissolved oxygen levels using simple linear regression.

🧠 What This Module Solves
Monitors water health using real-time sensor data
Detects pollution events or abnormal conditions using anomaly detection
Predicts future values of temperature and oxygen levels to raise early alerts

⚙️ Tech Stack Used
  Tool/Library	    |    Why We Used It
    Python	        | Easy to write, highly readable
    Pandas	        | For working with datasets
  Scikit-learn	    | For training ML models (Isolation Forest, Regression)
   Matplotlib       |	For visualising anomalies and predictions
  Google Colab	    | For easy cloud-based coding with GPU/CPU access

🧾 Files Included
Aqua_Nova.ipynb      – Google Colab notebook for training Isolation Forest and for temperature & oxygen forecasting
forecast_results.csv – Sample output of predictions
assets/              – Folder with charts and output visuals

📦 How to Run This on Your Device (Step-by-Step)
You can run this with no installation using Google Colab.

Run in Google Colab (Recommended)
Open the notebook:
Visit the GitHub repo
Click on the .ipynb file (Aqua_Nova.ipynb)
Click "Open in Colab" button

Upload the dataset:
Download water_potability.csv (For the Anomaly Detection)
Download temp, oxygen data set.csv (For Predictive Analysis)


Upload via Files > Upload in Colab
Run the cells (Shift + Enter) one by one

First part trains the model
Then it predicts anomalies or future values
Final cells plot the graphs

🔬 How the Model Works
1. Anomaly Detection using Isolation Forest
We use ph, turbidity, and sulfate as input features
The model learns normal patterns from the data
Then it flags abnormal water conditions (e.g., toxic spills, chemical spikes)

2. Prediction using Linear Regression
Input: time in minutes
Output: predicted temperature (°C) and dissolved oxygen (mg/L)
The model fits a straight line to historical data and forecasts future trends

📊 Output Examples
Scatter plot showing anomalies in red and normal data in blue
Line graph showing actual vs predicted temperature and oxygen levels

🧪 Sample Use Cases
Predict algal blooms, oxygen depletion, or thermal pollution
Alert aquaculture teams or coastal authorities before disaster strikes
