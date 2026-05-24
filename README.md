# 🍎 AI Nutritionist App

An AI-powered nutrition analysis application built using **Streamlit** and **Google Gemini AI**.  
Upload a food image and receive an instant breakdown of:

- Estimated Calories
- Protein
- Carbohydrates
- Fats
- Meal Health Insights

The app uses **Google Gemini Multimodal Models** to analyze food images and generate nutrition recommendations in real time.

---

## 🚀 Live Demo

🌐 **Streamlit Deployment:**  
 https://nutrition-app-1.streamlit.app/

---

# 📸 Application Preview

## Home Interface

![Screenshot 2024-10-21 234213](https://github.com/user-attachments/assets/374a2a77-563d-4a4e-9176-55caf8a0bce0)

---

## Nutrition Analysis Output

![Screenshot 2024-10-21 234230](https://github.com/user-attachments/assets/db1ad838-692f-40f1-b7ab-206230a4a1fc)

---

# ✨ Features

- 📷 Upload food images
- 🤖 AI-powered nutrition analysis
- 🔥 Calorie estimation
- 🥩 Protein / Carbs / Fat breakdown
- 💡 Health suggestions
- ⚡ Fast Gemini 2.5 Flash inference
- 🌐 Fully deployed Streamlit application

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

```bash
AI-Nutritionist-App/
│
├── app.py
├── requirements.txt
├── runtime.txt
└── README.md
```

---

# ⚙️ Installation & Local Setup

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

Create a `.streamlit/secrets.toml` file:

```toml
GOOGLE_API_KEY="your_gemini_api_key"
```

Get your API key from:

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

This model supports:
- Multimodal image understanding
- Fast inference
- Nutrition reasoning
- Real-time AI responses

---

# 📌 Future Improvements

- Meal history tracking
- Daily calorie dashboard
- BMI calculator
- Personalized diet plans
- User authentication
- MongoDB integration
- AI meal recommendation system

---

# 👨‍💻 Author

**Rudra Tyagi**

- AWS ML Engineer
- ML Systems & MLOps Enthusiast
- AI Infrastructure Learner

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
