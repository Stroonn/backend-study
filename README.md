# 🚀 Backend Study – Python API Project

This project is part of my journey learning backend development with Python.

I started with a simple CLI CRUD application and gradually improved it into a REST API using FastAPI. Along the way, I focused on writing cleaner code and understanding how real backend systems are structured.

The goal of this project is to practice and apply backend concepts in a practical way.

# 📌 Project Overview

This project includes:

- A structured backend architecture

- Separation between services and repositories

- Data validation and business rules

- REST API using FastAPI

- Basic error handling

- Automated tests with pytest

I tried to follow patterns that are commonly used in real-world applications.

## 🧠 What I Practiced

- Object-Oriented Programming (OOP)

- Separation of concerns

- Dependency injection

- REST API design

- Data validation with Pydantic

- Writing and organizing tests

- Refactoring code

## 🛠 Technologies Used

- Python 3

- FastAPI

- Pytest

- SQLite (current version)

- Git & GitHub

## 📂 Project Structure

<pre><code>backend-study/
backend-study/
│
├── app/
│   ├── core/
│   ├── database/
│   ├── errors/
│   ├── models/
│   ├── repositories/
│   ├── schemas/
│   └── services/
│
├── tests/
│
├── main_api.py      # FastAPI application
├── init_db.py       # Database initialization
└── README.md</code></pre>

## 🌐 How to Run the API

First, install the dependencies:

<pre><code>pip install fastapi uvicorn</code></pre>

Then run the server:

<pre><code>uvicorn main_api:app --reload</code></pre>

Open your browser and go to:

<pre><code>http://127.0.0.1:8000/docs</code></pre>

You will see the Swagger UI where you can test the endpoints.

## 🧪 How to Run Tests

To run the tests:

<pre><code>pytest</code></pre>

The tests cover:

- Product creation

- Validation rules

- API endpoints

- Error cases

## 🎯 Purpose of This Project

The main goal is to improve my backend development skills step by step.

In this project, I focus on:

Writing cleaner and more organized code

Understanding backend architecture

Practicing real-world patterns

Improving testing and reliability

I plan to keep improving this project over time.

## 🔮 Future Improvements

- Add authentication

- Use PostgreSQL

- Docker support

- Improve logging

## 👨‍💻 Author

Matheus Souza

Bachelor in Computer Science

Backend Developer in progress 🚀