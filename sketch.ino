#include "DHT.h"
#define DHTPIN 15
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);

#define SAL_PIN 36  // VP
#define TURB_PIN 39 // VN
#define DO_PIN 34
#define PH_PIN 35
#define VISC_PIN 32
#define DENS_PIN 33
#define LIF_PIN 25

void setup() {
  Serial.begin(115200);
  dht.begin();
}

float normalize(int val, int in_min, int in_max) {
  return constrain((float)(val - in_min) / (in_max - in_min) * 100.0, 0, 100);
}

void loop() {
  float temp = dht.readTemperature();
  int sal = analogRead(SAL_PIN);
  int turb = analogRead(TURB_PIN);
  int dox = analogRead(DO_PIN);
  int ph = analogRead(PH_PIN);
  int visc = analogRead(VISC_PIN);
  int dens = analogRead(DENS_PIN);
  int lif = analogRead(LIF_PIN);

  float tempScore = normalize(temp, 15, 35);
  float salScore = normalize(sal, 0, 4095);
  float turbScore = normalize(4095 - turb, 0, 4095); // More blockage = more turbid
  float doScore = normalize(dox,0, 4095);
  float phScore = normalize(ph, 0 , 4095);

  float oilRisk = (visc > 3000 && dens < 2000) ? 0 : 100;
  float microplasticRisk = (lif > 2500) ? 0 : 100;

  float mhi = (tempScore + salScore + turbScore + doScore + phScore + oilRisk + microplasticRisk) / 7;

  Serial.println("\n--- Marine Health Index Report ---");
  Serial.printf("Temp: %.2f°C | Score: %.1f\n", temp, tempScore);
  Serial.printf("Salinity: %d | Score: %.1f\n", sal, salScore);
  Serial.printf("Turbidity: %d | Score: %.1f\n", turb, turbScore);
  Serial.printf("Dissolved O2: %d | Score: %.1f\n", dox, doScore);
  Serial.printf("pH: %d | Score: %.1f\n", ph, phScore);
  Serial.printf("Oil Spill Detected: %s\n", (oilRisk == 0) ? "YES" : "NO");
  Serial.printf("Microplastics Detected: %s\n", (microplasticRisk == 0) ? "YES" : "NO");
  Serial.printf("🌊 Marine Health Index: %.1f / 100\n", mhi);
  Serial.println("----------------------------------");

  delay(5000);
}
