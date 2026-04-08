# 🚀 CommerceAI – AI-Powered E-commerce Backend with ML Prediction Engine

## 📌 Overview

CommerceAI is a production-ready backend system built using **FastAPI**, **PostgreSQL**, and **Machine Learning**.
It provides scalable REST APIs for managing products along with an intelligent **price prediction engine** powered by ML.

---

## ⚡ Key Features

* 🛒 Product Management (Create, Read, Update, Delete)
* 🧠 AI-based Price Prediction (Linear Regression)
* ⚡ FastAPI high-performance backend
* 🗄️ PostgreSQL database integration
* 📊 SQLAlchemy ORM for clean database handling
* 📑 Auto-generated API docs (Swagger UI)
* 🧩 Modular & scalable architecture

---

## 🛠️ Tech Stack

* **Backend:** FastAPI, Python
* **Database:** PostgreSQL
* **ORM:** SQLAlchemy
* **ML:** scikit-learn, pandas
* **Server:** Uvicorn

---

## 📂 Project Structure

```
app/
│── main.py
│── database.py
│
├── models/
│   └── product.py
│
├── schemas/
│   └── product.py
│
├── routes/
│   └── product_routes.py
│
├── ml/
│   └── model.py
```

---

## 🚀 Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/commerceai-fastapi-ml-backend.git
cd commerceai-fastapi-ml-backend
```

### 2️⃣ Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

## ⚙️ Database Setup

Make sure PostgreSQL is running.

Update your connection string in `database.py`:

```
postgresql://postgres:yourpassword@127.0.0.1:5432/commerceai
```

---

## ▶️ Run the Server

```
python -m uvicorn app.main:app --reload
```

---

## 🌐 API Documentation

Open in browser:

```
http://127.0.0.1:8000/docs
```

---

## 📡 API Endpoints

### 🛒 Product APIs

* `POST /products/` → Create product
* `GET /products/` → Get all products
* `PUT /products/{product_id}` → Update product
* `DELETE /products/{product_id}` → Delete product

### 🤖 ML API

* `GET /products/predict-price/?name=product_name`
  → Predict product price using ML

---

## 🧠 ML Model Details

* Model: Linear Regression
* Features: Product-based heuristic mapping
* Library: scikit-learn

---

## 📈 Future Improvements

* 🔐 JWT Authentication
* 📊 Advanced ML models (Random Forest / XGBoost)
* 📦 Docker support
* ☁️ Cloud deployment (AWS / Render)
* 🛍️ Order & User modules

---

## 👨‍💻 Author

**Anvesh Dubey**
AI | Data | Backend Engineering Enthusiast

---

## ⭐ Show your support

If you like this project, give it a ⭐ on GitHub!
