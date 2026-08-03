# 🤖 VeriAssist

### AI-Powered Verilog Learning & Debugging Assistant
![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web_App-black?logo=flask)
![Gemini](https://img.shields.io/badge/Google-Gemini_AI-blue?logo=google)
![Icarus Verilog](https://img.shields.io/badge/Icarus-Verilog-green)
![HTML](https://img.shields.io/badge/HTML-Frontend-orange?logo=html5)
![License](https://img.shields.io/badge/License-MIT-success)
---

# 📖 About VeriAssist

Learning Verilog can be challenging because most existing tools focus on **compilation and simulation** rather than helping beginners understand compiler errors.

As an Electronics and Communication Engineering (ECE) student, I found that while compilers could detect syntax errors, they rarely explained **why the error occurred, how to fix it, or what the corrected code should look like**. This often made the learning process slower and more frustrating.

**VeriAssist** was built to bridge this gap by combining traditional Verilog compilation with AI-powered explanations. Instead of simply displaying compiler messages, it helps users understand the logic behind the errors, suggests possible fixes, and generates corrected Verilog code.

The goal of VeriAssist is to make learning Verilog more interactive, intuitive, and educational for students, beginners, and anyone starting their journey in digital design.
---

# ✨ Features

- 📄 Upload Verilog (`.v`) source files through a simple web interface.
- ⚙️ Compile Verilog designs using **Icarus Verilog**.
- 🤖 Generate AI-powered explanations of compiler errors using **Google Gemini**.
- 💡 Identify likely causes and suggest practical fixes.
- 📝 Generate corrected Verilog code based on the detected error.
- 🎨 Modern and responsive user interface.
- 📌 Highlight compiler error lines in the original source code.
- 📜 Side-by-side view of original and AI-corrected code.
- 📋 One-click copy of the corrected code.
- ⏳ AI loading screen with real-time analysis messages.
- 🛡️ Graceful fallback when the AI service is temporarily unavailable.
---

# 🏗️ System Architecture

```text
                User

                  │

                  ▼

        Upload Verilog File

                  │

                  ▼

           Flask Backend

        ┌───────────────┐
        │               │
        ▼               ▼

 Icarus Verilog     Gemini AI

        │               │

        └──────┬────────┘
               ▼

     AI Error Analysis

               │

               ▼

 Interactive Results Dashboard
```
---

# 🚀 Workflow

```text
Upload Verilog File
        │
        ▼
Compile using Icarus Verilog
        │
        ▼
Parse Compiler Errors
        │
        ▼
Generate AI Explanation
        │
        ▼
Generate Corrected Code
        │
        ▼
Display Interactive Dashboard
```

---

# 🛠 Technology Stack

## Backend

- Python
- Flask

## Compiler

- Icarus Verilog

## Artificial Intelligence

- Google Gemini API

## Frontend

- HTML5
- CSS3
- JavaScript

## Version Control

- Git
- GitHub

---

# 📂 Project Structure

```text
AI-Powered-Verilog-Bug-Detector
│
├── ai/
│   ├── explain.py
│   ├── knowledge.py
│   ├── llm.py
│   └── prompts.py
│
├── compiler/
│   ├── compile.py
│   └── parser.py
│
├── static/
│   ├── css/
│   └── js/
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── examples/
├── uploads/
├── app.py
├── requirements.txt
└── README.md
```

---

# 📸 Screenshots

> *(Screenshots will be added after deployment.)*

### 🏠 Landing Page

*(Insert screenshot here)*

---

### 🤖 AI Loading Screen

*(Insert screenshot here)*

---

### 📊 Analysis Dashboard

*(Insert screenshot here)*

---

### 📄 Original vs Corrected Code

*(Insert screenshot here)*

---

# ⚙ Installation

## Clone the repository

```bash
git clone https://github.com/Chetan-Nandam/AI-Powered-Verilog-Bug-Detector.git

cd AI-Powered-Verilog-Bug-Detector
```

---

## Install dependencies

```bash
pip install -r requirements.txt
```

---

## Configure API Key

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

## Run the application

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

# 🚧 Challenges & Learnings

One of the biggest challenges during development was managing a growing frontend while integrating AI and compiler services into a seamless user experience.

Working on VeriAssist helped me strengthen my understanding of:

- Flask web application development
- AI API integration
- Compiler error parsing
- HTML, CSS and JavaScript
- Git and GitHub workflows
- Modular Python application design
- Building educational software around real engineering problems

---

# 🔮 Future Improvements

- ☁ Deploy VeriAssist to the cloud
- 📈 RTL simulation support
- 🌊 Waveform generation and visualization
- 💬 Interactive AI chat assistant for Verilog
- 📁 Multi-file Verilog project support
- 📚 Learning mode with Verilog tutorials and examples

---

# 👨‍💻 Author

**Chetan Nandam**

Electronics & Communication Engineering Student

Interested in Semiconductor Technology, VLSI Design, Digital Design, FPGA Development and AI-assisted Engineering Tools.

GitHub:
https://github.com/Chetan-Nandam

---

# ⭐ Support

If you found this project interesting, consider giving it a ⭐ on GitHub