# 🚀 Backend Study – Python API Project

This repository documents my structured journey into backend development using Python.

The project evolved from a simple CLI-based CRUD system into a RESTful API built with FastAPI, following clean architecture principles and software engineering best practices.

It represents hands-on learning focused on writing production-ready backend code.

# 📌 Project Overview

This backend project includes:

Clean architecture structure

Service and repository pattern

Data validation and business rules

JSON-based persistence

Unit tests with pytest

REST API built with FastAPI

Proper HTTP error handling

Structured code organization

The goal is to simulate real-world backend development practices.

## 🧠 Concepts Practiced

Object-Oriented Programming (OOP)

Separation of concerns

Dependency injection

Error handling

API design (REST)

Pydantic schema validation

Automated testing

Code refactoring

## 🛠 Technologies Used

Python 3

FastAPI

Pytest

JSON persistence

VS Code

Git & GitHub

Future improvements:

SQLite / PostgreSQL

Docker

Authentication

Logging improvements

## 📂 Project Structure

<pre><code>backend-study/
backend-study/
│
├── app/
│   ├── models/
│   ├── repositories/
│   ├── services/
│   ├── schemas/
│   └── utils/
│
├── tests/
│
├── main.py          # CLI version
├── main_api.py      # FastAPI version
└── README.md</code></pre>

## ▶️ How to Run (CLI Version)
python main.py
🌐 How to Run (API Version)

Install dependencies:

<pre><code>pip install fastapi uvicorn</code></pre>

Run the API:

<pre><code>uvicorn main_api:app --reload</code></pre>

Open in browser:

<pre><code>http://127.0.0.1:8000/docs</code></pre>

Swagger documentation will be available automatically.

## 🧪 How to Run Tests

<pre><code>pytest</code></pre>

The project includes unit tests for:

Product creation

Validation rules

Repository behavior

CRUD operations

## 🎯 Objective

The purpose of this repository is to transition from basic Python knowledge to professional backend development skills.

Each iteration improves:

Code quality

Architecture

Test coverage

API structure

Engineering discipline

This project will continue evolving toward a production-level backend system.

## 👨‍💻 Author

Matheus Souza
Bachelor in Computer Science
Backend Developer in progress 🚀