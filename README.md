# 🍎 AI Nutritionist App

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red?style=for-the-badge&logo=streamlit)
![Gemini](https://img.shields.io/badge/Google-Gemini_AI-orange?style=for-the-badge&logo=google)
![AI](https://img.shields.io/badge/AI-Multimodal-success?style=for-the-badge)
![Computer Vision](https://img.shields.io/badge/Computer-Vision-purple?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Live-success?style=for-the-badge)

</p>

---

# 🌐 Live Application

🚀 **Streamlit Deployment:**  
https://nutrition-app-1135.streamlit.app/

---

# 📌 Project Overview

The **AI Nutritionist App** is a multimodal AI-powered nutrition analysis system built using:

- Streamlit
- Google Gemini AI
- Python
- Pillow (PIL)

The application allows users to upload food images and receive:

- calorie estimates
- macronutrient breakdown
- nutrition insights
- AI-generated health recommendations

The system uses Google Gemini's multimodal reasoning capabilities to analyze food images and generate real-time nutritional assessments.

---

# 🎯 What This Application Actually Does

The application performs:

```text
Food Image Upload
        ↓
Image Processing
        ↓
Gemini Multimodal Analysis
        ↓
Nutrition Estimation
        ↓
Health Insight Generation
        ↓
Interactive Streamlit Output
```

Users can:
1. Upload a food image
2. Enter an optional prompt
3. Generate AI-powered nutrition analysis
4. Review calorie and macronutrient estimates

---

# 🧠 How The AI Analysis Works

The system uses:

```text
Google Gemini Multimodal Models
```

to process both:
- image input
- text instructions

The model analyzes:
- visible food items
- meal composition
- approximate serving sizes
- nutritional characteristics

and generates a structured nutrition report.

---

# 📊 Understanding The Results

The application estimates:

| Output | Meaning |
|---|---|
| Calories | Estimated total energy intake |
| Protein | Approximate protein content |
| Carbohydrates | Estimated carbohydrate amount |
| Fats | Estimated fat content |
| Health Insights | AI-generated nutritional observations |

---

## 📌 Example Interpretation

If the uploaded image contains:
- rice
- chicken
- vegetables

The AI may estimate:

- total calories
- protein-rich components
- carbohydrate-heavy portions
- overall meal balance

This enables users to quickly understand:
- meal composition
- nutritional density
- estimated calorie intake
- dietary balance

---

# 🏗️ System Architecture

```text
Food Image Upload
        ↓
Image Processing Layer (PIL)
        ↓
Gemini Multimodal AI Model
        ↓
Nutrition Reasoning Engine
        ↓
Structured Nutrition Output
        ↓
Streamlit Interactive Dashboard
```

---

# ⚙️ Architecture Breakdown

## 📷 Image Processing Layer

Implemented using:

- Pillow (PIL)

Responsibilities:
- image loading
- image formatting
- image preprocessing

---

## 🤖 AI Inference Layer

Powered by:

- Google Gemini AI

Responsible for:
- multimodal understanding
- food recognition
- nutritional reasoning
- text generation

---

## 🖥️ Streamlit UI Layer

Responsible for:
- image upload
- user interaction
- response rendering
- deployment interface

---

# ✨ Core Features

## 📷 Food Image Upload

Users can upload:
- JPG
- JPEG
- PNG

food images directly through the dashboard.

---

## 🤖 AI-Powered Nutrition Analysis

The Gemini model generates:
- food recognition
- calorie estimation
- macronutrient analysis
- meal-level insights

---

## 🔥 Calorie Estimation

The application estimates:
- total meal calories
- relative calorie density
- energy contribution

---

## 🥩 Macronutrient Breakdown

Provides estimated:
- protein
- carbohydrates
- fats

for uploaded meals.

---

## 💡 Health Insights

The AI generates:
- nutritional observations
- meal balance comments
- dietary suggestions

---

## ⚡ Real-Time Inference

Fast multimodal inference powered by:
- Gemini 2.5 Flash

---

# 📸 Application Preview

## 🖥️ Home Interface

![Home Interface](https://github.com/user-attachments/assets/374a2a77-563d-4a4e-9176-55caf8a0bce0)

---

## 📊 Nutrition Analysis Output

![Nutrition Analysis](https://github.com/user-attachments/assets/db1ad838-692f-40f1-b7ab-206230a4a1fc)

---

# 🛠️ Tech Stack

| Technology | Usage |
|---|---|
| Python | Backend Logic |
| Streamlit | Web Application |
| Google Gemini AI | Multimodal Food Analysis |
| Pillow (PIL) | Image Processing |

---

# 📂 Project Structure

```text
AI-Nutritionist-App/
│
├── app.py
├── requirements.txt
├── runtime.txt
└── README.md
```

---

# ⚙️ Local Setup & Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/AI-Nutritionist-App.git
cd AI-Nutritionist-App
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Gemini API Setup

Create:

```text
.streamlit/secrets.toml
```

Add:

```toml
GOOGLE_API_KEY="your_gemini_api_key"
```

Get API key from:

:contentReference[oaicite:1]{index=1}

---

# ▶️ Run Application

```bash
streamlit run app.py
```

---

# 📦 Requirements

```txt
streamlit==1.39.0
google-generativeai>=0.8.3
Pillow
```

---

# 🧠 AI Model Used

The application uses:

```python
models/gemini-2.5-flash
```

Capabilities include:

- multimodal image understanding
- food recognition
- nutrition reasoning
- fast inference
- real-time AI responses

---

# 📊 Engineering Highlights

- Multimodal AI application
- Gemini AI integration
- Image-to-text reasoning workflow
- Real-time AI inference
- Streamlit cloud deployment
- AI-powered nutrition estimation
- Interactive AI dashboard
- Production-ready secrets handling
- Image processing pipeline

---

# 📈 Potential Future Improvements

Planned enhancements include:

- Meal history tracking
- Daily calorie dashboard
- BMI calculator
- Personalized diet plans
- User authentication
- MongoDB integration
- AI meal recommendation engine
- Nutrition tracking system
- Cloud-native backend architecture
- API-based AI inference layer

---

# 🎯 What This Project Demonstrates

This project demonstrates practical understanding of:

- Multimodal AI systems
- Generative AI integration
- Streamlit deployment workflows
- AI-powered image analysis
- Real-time inference systems
- Interactive AI applications
- Computer vision workflows
- Production AI application design

---

# 📌 Strategic Engineering Value

This project demonstrates significantly more engineering depth than basic chatbot applications because it includes:

- multimodal AI integration
- image processing workflows
- AI reasoning pipelines
- production deployment
- real-time inference systems
- interactive AI application architecture

---

# 👨‍💻 Author

## Rudra Tyagi

### Focus Areas

- ML Systems
- MLOps
- AI Infrastructure
- Generative AI Systems
- Applied Machine Learning

---

# ⭐ Recruiter Notes

This repository demonstrates:

- Multimodal AI engineering
- Gemini AI integration
- Real-time inference systems
- Interactive AI application design
- Streamlit deployment capability
- AI-powered analytical workflows

---

# 📜 License

This project is intended for educational, research, and portfolio purposes.

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
