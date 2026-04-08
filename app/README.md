# CommerceAI – AI-Powered E-commerce Backend with ML Prediction Engine

## Overview

A production-style FastAPI backend with PostgreSQL and an ML-powered price prediction endpoint.

## Features

* FastAPI REST APIs (CRUD for Products)
* PostgreSQL + SQLAlchemy ORM
* Swagger docs (`/docs`)
* ML price prediction (scikit-learn)
* Clean modular architecture

## Tech Stack

* Python, FastAPI
* PostgreSQL
* SQLAlchemy
* scikit-learn, pandas

## Setup

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```bash
python -m uvicorn app.main:app --reload
```

## Endpoints

* POST `/products/` — create product
* GET `/products/` — list products
* PUT `/products/{product_id}` — update
* DELETE `/products/{product_id}` — delete
* GET `/products/predict-price/?name=` — ML prediction

## Project Structure

```
app/
  main.py
  database.py
  models/
  schemas/
  routes/
  ml/
```

## Author

Anvesh Dubey
