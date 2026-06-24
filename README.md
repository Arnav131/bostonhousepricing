<div align="center">
  <h1>🏡 Boston House Pricing Prediction</h1>
  <p>An End-to-End Machine Learning Project with Flask API and Web Interface</p>

  [![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
  [![Flask](https://img.shields.io/badge/Flask-2.0+-lightgrey.svg)](https://flask.palletsprojects.com/)
  [![Docker](https://img.shields.io/badge/Docker-Enabled-blue.svg)](https://www.docker.com/)
  [![scikit-learn](https://img.shields.io/badge/scikit--learn-Enabled-orange.svg)](https://scikit-learn.org/)
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
</div>

<br />

## 📖 Overview

The **Boston House Pricing Prediction** project is a comprehensive Machine Learning application that predicts the price of houses in Boston based on various features such as crime rate, number of rooms, and proximity to employment centers.

The core of the project is a trained **Linear Regression model**, serialized and served via a **Flask API**. It provides both a programmatic API endpoint and a user-friendly Web UI.

---

## ✨ Key Features

- **Robust ML Model**: Predicts house prices utilizing multiple features mapped to a pre-trained model.
- **RESTful API**: Allows external services to interact with the prediction engine via JSON payloads.
- **Web Interface**: A clean HTML/CSS frontend to input data manually and instantly see the predicted price.
- **Dockerized**: Fully containerized using Docker for seamless cross-platform deployment.
- **CI/CD Integrated**: Configured with GitHub Actions for automated deployment to cloud platforms like Render.

---

## 🛠️ Tech Stack

- **Machine Learning**: `scikit-learn`, `numpy`, `pandas`
- **Backend Framework**: `Flask`, `gunicorn`
- **Frontend**: HTML, CSS, Jinja2 Templates
- **Containerization**: `Docker`
- **Deployment**: Render, GitHub Actions

---

## 🚀 Getting Started

Follow these steps to set up the project locally on your machine.

### Prerequisites

Ensure you have the following installed:
- [Python 3.8+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)
- [Docker](https://www.docker.com/products/docker-desktop/) (optional, for containerized run)

### Local Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Arnav131/bostonhousepricing.git
   cd bostonhousepricing
   ```

2. **Create a virtual environment**
   ```bash
   conda create -p venv python=3.8 -y
   conda activate venv/
   # Or using venv: python -m venv venv && source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```
   The application will be accessible at `http://127.0.0.1:5000/`.

---

## 🔌 API Reference

You can test the programmatic endpoints using tools like [Postman](https://www.postman.com/downloads/) or `curl`.

### **Predict Price**

- **URL:** `/predict_api`
- **Method:** `POST`
- **Content-Type:** `application/json`

**Request Body:**
```json
{
  "data": {
    "CRIM": 0.00632,
    "ZN": 18.0,
    "INDUS": 2.31,
    "CHAS": 0.0,
    "NOX": 0.538,
    "RM": 6.575,
    "AGE": 65.2,
    "DIS": 4.09,
    "RAD": 1.0,
    "TAX": 296.0,
    "PTRATIO": 15.3,
    "B": 396.9,
    "LSTAT": 4.98
  }
}
```

**Response:**
```json
24.02031
```
*(The response represents the predicted price in $1000s)*

---

## 🐳 Deployment Methods

### 1. Deploying via Docker

To run the application inside a Docker container:

1. **Build the Docker Image**
   ```bash
   docker build -t boston-house-pricing .
   ```

2. **Run the Docker Container**
   ```bash
   docker run -p 5000:5000 boston-house-pricing
   ```

### 2. Deploying to Render (with CI/CD)

This project contains a GitHub Actions workflow `.github/workflows/render.yml` to automatically deploy the application.

1. Create a free account on [Render.com](https://render.com/).
2. Create a new **Web Service** and connect this GitHub repository.
3. Configuration settings:
   - **Environment:** Docker (or Python with Start Command: `gunicorn --workers=1 --bind 0.0.0.0:$PORT app:app`)
4. Upon every push to the `main` branch, the GitHub Actions pipeline will seamlessly deploy the latest version.

---

## 📁 Project Structure

```text
bostonhousepricing/
│
├── .github/workflows/           # CI/CD pipelines
├── templates/                   # HTML Templates (home.html)
├── app.py                       # Main Flask Application
├── Dockerfile                   # Instructions for containerization
├── requirements.txt             # Python dependencies
├── regmodel.pkl                 # Pre-trained ML model
├── scaling.pkl                  # Scaler for data standardization
├── Linear_Regression_ML_Project.ipynb # Jupyter Notebook for ML Training
└── README.md                    # Project Documentation
```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! 
Feel free to check out the [issues page](https://github.com/Arnav131/bostonhousepricing/issues).

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the [MIT License](LICENSE) - see the `LICENSE` file for details.
