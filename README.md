# 🌾 AgriMind AI

<p align="center">
  <img src="assets/logo.png" width="180">
</p>

<h3 align="center">
AI-Powered Smart Crop Recommendation System
</h3>

<p align="center">
Machine Learning • Gemini AI • Weather API • Streamlit
</p>

---

# 📌 Project Overview

AgriMind AI is an intelligent agriculture assistant that helps farmers make informed crop decisions using Artificial Intelligence.

The system predicts the most suitable crop based on soil nutrients and weather conditions, then provides fertilizer recommendations, irrigation guidance, live weather information, AI-generated explanations using Google Gemini, downloadable PDF reports, and prediction history.

The project aims to support precision agriculture by improving productivity and reducing farming risks.

---

# ✨ Features

✅ Intelligent Crop Recommendation using Machine Learning

✅ Live Weather Integration (WeatherAPI)

✅ AI Expert Explanation using Google Gemini

✅ Fertilizer Recommendation

✅ Irrigation Recommendation

✅ Crop Images

✅ AI Confidence Gauge

✅ Prediction History

✅ Professional PDF Report Generation

✅ Modern Streamlit Dashboard

---

# 🏗️ System Architecture

```
                User Input
                     │
                     ▼
      Soil + Weather Information
                     │
                     ▼
         Crop Prediction Model
                     │
                     ▼
      Recommended Crop & Confidence
                     │
      ┌──────────────┼──────────────┐
      ▼              ▼              ▼
 Fertilizer      Irrigation     Weather API
 Recommendation Recommendation
      │              │
      └──────────────┼──────────────┘
                     ▼
              Gemini AI Analysis
                     │
                     ▼
             Final AI Recommendation
                     │
                     ▼
          PDF Report & Prediction History
```

---

# 📂 Project Structure

```
AI-Crop-Recommendation-Agent/
│
├── app.py
├── requirements.txt
├── README.md
│
├── assets/
│   ├── logo.png
│   └── crops/
│
├── components/
│
├── core/
│
├── services/
│
├── data/
│
├── database/
│
├── models/
│
└── test_files/
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/vamsi098P/DSIS-CROP_AGENT.git
```

Go to project

```bash
cd DSIS-CROP_AGENT
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 🚀 Usage

1. Enter soil nutrient values (N, P, K)
2. Enter city name
3. Fetch live weather
4. Click **Predict Crop**
5. View:
   - Recommended Crop
   - AI Confidence
   - Fertilizer Recommendation
   - Irrigation Recommendation
   - Gemini AI Explanation
6. Download the AI-generated PDF Report
7. Review Prediction History

---

# 📸 Screenshots

## Home Page

> *(Add screenshot here)*

```
screenshots/home.png
```

---

## Prediction Result

> *(Add screenshot here)*

```
screenshots/result.png
```

---

## PDF Report

> *(Add screenshot here)*

```
screenshots/pdf.png
```

---

# 🛠️ Tech Stack

### Frontend

- Streamlit

### Backend

- Python

### Machine Learning

- Scikit-learn
- Joblib
- NumPy
- Pandas

### AI

- Google Gemini AI

### Weather

- WeatherAPI

### Visualization

- Plotly

### Database

- SQLite

### Report Generation

- ReportLab

---

# 📊 Key Functionalities

✔ Crop Prediction

✔ Live Weather

✔ Fertilizer Suggestion

✔ Irrigation Advice

✔ AI Explanation

✔ Confidence Score

✔ Crop Images

✔ Prediction History

✔ Downloadable PDF Report

---

# 📈 Future Enhancements

- 📍 GPS-based Weather Detection
- 🌍 Multi-language Support (Telugu, Hindi)
- 🎤 Voice Assistant
- 📱 Mobile Application
- 📈 Analytics Dashboard
- 🌱 Soil Health Monitoring
- ☁ Cloud Deployment
- 🔔 Smart Farming Alerts

---

# 👨‍💻 Developer

**Vamsi Garapati**

B.Tech – Computer Science & Data Science

NRI Institute of Technology

📧 Email:
vamsigarapati40@gmail.com

🔗 LinkedIn:
https://www.linkedin.com/in/vamsi-garapati-36ab4632b

💻 GitHub:
https://github.com/vamsi098P

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

---

# 📄 License

This project is developed for educational and research purposes.

© 2026 Vamsi Garapati. All Rights Reserved.