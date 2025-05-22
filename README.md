# 🤖 AI-Assisted Sensor Data Interpretation

A lightweight integration was developed to process environmental sensor data using a Large Language Model (LLM). The pipeline involves the following components:
## 📦 Data Input

   - Sensor data is provided in JSON format.

   - Each entry includes measurements like temperature, humidity, CO2 (ppm), and battery level.

## 🔄 Processing Pipeline

  Prompt Engineering:
   Each JSON object is serialized into a string and passed to the LLM with a carefully structured prompt that defines:

   - The units of measurement

   - Thresholds for comfort and health concerns

   - Appropriate responses and advisory actions

  Model Usage:

   - Model: gpt-3.5-turbo-16k

   - Mode: Chat completion API

   Role definitions and assistant guidelines are set dynamically per prompt to instruct the LLM on how to interpret sensor data.

  Health and System Advisories:
   The LLM is instructed to:

   - Warn about CO₂ levels above 500 ppm

   - Comment on temperature (cold < 10°C, hot > 30°C)

   - Detect battery issues (<20% = low, >100% = faulty sensor)

   -  Evaluate humidity comfort range (30%–50%)

## ✅ Output Format

Each response provides a short advisory comment tailored to the sensor conditions, including warnings, comfort evaluation, and maintenance suggestions.
## ⚠️ Note

Due to confidentiality agreements, no real data or proprietary implementation details are included.
