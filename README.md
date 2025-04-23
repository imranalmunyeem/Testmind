# 🧠 TestMind — AI-Powered Test Case Generation Tool

![TestMind Logo](https://cdn-icons-png.flaticon.com/512/3039/3039525.png)

🚀 **TestMind** is an AI-augmented test automation assistant that generates automated and manual test cases for web applications using **Google Gemini API**. It supports multiple testing frameworks including **Cypress**, **Selenium**, **Playwright**, and **Postman**.

Built for **QA professionals, developers, and researchers**, TestMind can transform DOMs, endpoint descriptions, or free text into structured test scripts or manual test case documentation.

---

## ✨ Features

- 🧠 **LLM-Assisted Generation**: Uses Google's Gemini API for intelligent test case generation.
- 🎯 **Framework Support**: Cypress, Selenium, Playwright, Postman (with extensibility).
- 📋 **Manual or Automated Tests**: Choose test case type based on your needs.
- 🧾 **Custom Input Modes**: Accepts HTML DOM, raw text, endpoint specs, or user-defined scenarios.
- 💾 **Export & Save Results**: Automatically logs results with metadata and timestamps.
- 🌙 **Dark Mode UI**: Seamless toggling for personal preference.
- 📊 **Real Testing Datasets**: Applied to real-world apps like SauceDemo, nopCommerce, OpenCart, etc.

---

## 📁 Project Structure



## 🛠️ Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/testmind.git
cd testmind
```

### 2. Install Dependencies
```bash
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows

pip install -r requirements.txt

```

### 3. Configure Google Gemini API
Create a file named .env or modify config.py:
```bash
MODEL_TO_USE = "gemini-pro"  # or gemini-pro-vision
```

### 4. Launch TestMind
```bash
streamlit run main.py
```

## 🚀 How to Use
Choose Test Parameters from the sidebar:

Input type: DOM, endpoint, text, scenario

Test case type: Manual or Automated

Framework: Cypress, Selenium, Playwright, Postman

Paste Input (e.g., HTML snippet or scenario description)

Click ✨ Generate AI Test Cases

🎉 Test cases will appear in the interface with export options

## 📦 Export Options
Download results as .txt or .json

Auto-logs each session with timestamp, input, framework, and test type

Saved in the results/ folder