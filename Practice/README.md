# 🧪 Selenium Automation Framework (Python | Pytest | Data-Driven)

## 📌 Project Overview
This project demonstrates my hands-on learning in Selenium automation using Python.

It starts with a basic Selenium script and evolves into a structured Pytest-based framework, showcasing the transition from simple scripting to scalable test automation.

---

## 🚀 Key Highlights
- End-to-end UI automation using Selenium WebDriver
- Data-driven testing using JSON inputs
- Implementation of Pytest framework
- Use of parameterization and assertions
- Real-world e-commerce workflow automation

---

## 🧠 Learning Approach

### 🔹 Step 1: Basic Automation (`Project1.py`)
- Developed a basic Selenium script
- Automated login, product selection, and checkout flow
- Focused on understanding WebDriver interactions and locators

### 🔹 Step 2: Pytest Framework (`test_project1.py`)
- Refactored the same flow using Pytest
- Implemented:
  - `@pytest.mark.parametrize` for data-driven testing
  - Assertions for validation
- Improved code maintainability and reusability

👉 This demonstrates my progression from basic scripting to structured automation testing.

---

## 🧪 Test Scenario
- Authenticate user with valid credentials
- Identify and select products priced at **$15.99**
- Add selected items to cart
- Validate that only the correct items are present in the cart
- Complete checkout process and verify order confirmation

---

## 🛠 Tech Stack
- Python
- Selenium WebDriver
- Pytest
- JSON (Test Data)

---

## 📂 Project Structure

Practice/
│
├── Project1.py # Basic Selenium script
├── test_project1.py # Pytest implementation
├── test_Project.json # Test data (JSON)
├── conftest.py # Pytest fixtures
└── POM_Project1/ # Work in progress (POM structure)


---

## ▶️ How to Run

### 🔹 Install dependencies

pip install selenium pytest


### 🔹 Run tests

pytest


---

## 📈 Future Enhancements
- Implement Page Object Model (POM)
- Add logging and reporting
- Improve locator strategies
- Integrate CI/CD using GitHub Actions

---

## 💡 Note
This project reflects my hands-on learning and progression in automation testing, focusing on writing clean, maintainable, and scalable test code.