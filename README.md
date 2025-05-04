
# 🌍 EcoProphet : Intelligent CO2 Forecasting

This project is a machine learning-based web application that predicts **CO2 emissions** based on user inputs such as engine size, fuel type, and other relevant vehicle or industrial parameters. It also provides AI-generated recommendations to help reduce emissions.

---

## 📌 Project Highlights

- Built with **Flask** for backend API and UI rendering.
- Utilizes a **Multiple Linear Regression** model for CO2 prediction.
- Integrates **Gemini API** for generating personalized sustainability recommendations.
- Responsive UI using **HTML + CSS**.
- Locally deployable with lightweight dependencies.

---

## 📊 Tech Stack

- **Backend:** Python, Flask  
- **Machine Learning:** Scikit-Learn, NumPy, Pandas  
- **Frontend:** HTML5, CSS3  
- **AI Integration:** Gemini API (for eco-friendly suggestions)  
- **Tools:** Jupyter Notebook, VS Code  

---

## 📂 Folder Structure

```
CO2-Emission-Predictor/
│
├── static/                   # CSS stylesheets
│   └── style.css
│
├── templates/                # HTML templates
│   ├── index.html
│   ├── results.html
│
├── app.py                    # Main Flask application
├── model.pkl                 # Trained regression model
├── recommendations.py        # Gemini API integration logic
├── requirements.txt          # List of Python dependencies
└── README.md                 # Project documentation
```

---

## 🧠 How the Model Works

- Input features: e.g., engine size, cylinders, fuel type, etc.
- Output: Predicted CO2 emission value (in grams/km).
- The model is trained using a labeled dataset and tested for accuracy.
- Gemini API processes input parameters to recommend eco-friendly actions.

---

## 🚀 Local Deployment Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/CO2-Emission-Predictor.git
   cd CO2-Emission-Predictor
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   ```bash
   python app.py
   ```

4. **Access the App**
   Open your browser and visit: `http://127.0.0.1:5000/`

---

## 💡 Features

- 🔍 Real-time CO2 prediction  
- 📢 AI-powered green recommendations  
- 🔐 Secure and efficient local deployment  
- 📊 Scalable for integration with real-world sensors or data streams  

---

## 🧪 Accuracy and Performance

- The model achieved an improved prediction accuracy of **98%** on test data.
- Optimized for fast response and lightweight deployment.

---

## 📈 Future Enhancements

- Deploy on cloud (Heroku/AWS)  
- Add support for multiple ML models  
- Real-time sensor data integration  
- User dashboard for emission history tracking  

---

## 📬 Contact

Feel free to connect for contributions, questions, or suggestions:

- Email: [work.abhiinavv@email.com]  
- GitHub: [@mr-kamenari](https://github.com/mr-kamenari)   

---

> 🌱 *"Small predictions, big impact. Reduce emissions, one click at a time."*
