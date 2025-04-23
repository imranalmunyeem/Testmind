# 🧠 TestMind — AI-Powered Test Case Generation Tool

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

## 🛠 Tools & Libraries Used

### 💡 Core Technologies  
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)  
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)  
[![Gemini API](https://img.shields.io/badge/Google%20Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/)

---

### 🧪 Supported Test Frameworks  
[![Cypress](https://img.shields.io/badge/Cypress-17202C?style=for-the-badge&logo=cypress&logoColor=white)](https://www.cypress.io/)  
[![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)](https://www.selenium.dev/)  
[![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=for-the-badge&logo=playwright&logoColor=white)](https://playwright.dev/)  
[![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)](https://www.postman.com/)

---

### 🛠 Development & Tooling  
[![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)](https://code.visualstudio.com/)  
[![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)  
[![Markdown](https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white)](https://daringfireball.net/projects/markdown/)  
[![Mochawesome Reports](https://img.shields.io/badge/Mochawesome-7C4DFF?style=for-the-badge&logo=mochawesome&logoColor=white)](https://www.npmjs.com/package/mochawesome) 


## 📁 Project Structure
```
|-- .github
|     |-- workflows
|          |-- testmind-ci.yml                  # GitHub Actions CI/CD workflow for TestMind
|-- src
|     |-- components
|          |-- ui_components.py                 # Streamlit UI layout and reusable components
|     |-- handlers
|          |-- ai_handler.py                    # Handles prompt calls to Google Gemini API
|     |-- utils
|          |-- utils.py                         # Export, theme toggle, and helper utilities
|     |-- config.py                             # Configuration settings (API keys, model name)
|-- assets
|     |-- images
|          |-- logo.png                         # Logo used in the header
|-- testmind_app
|     |-- main.py                               # Main Streamlit app script
|-- requirements.txt                            # Python dependencies
|-- README.md                                   # Project documentation and usage guide
|-- .gitignore                                  # Files and folders to ignore in Git
```

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
