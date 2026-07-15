# 🤖 AI Resume Analyzer

An AI-powered Resume Analyzer built using **Python** and **Streamlit** that evaluates a resume against a job description, calculates an ATS (Applicant Tracking System) score, identifies missing skills, and provides personalized suggestions to improve the resume.

---

## 🚀 Overview

The **AI Resume Analyzer** helps job seekers understand how well their resume matches a specific job description. It extracts technical skills from both the resume and the job description, compares them, calculates an ATS score, highlights missing skills, and provides actionable suggestions to improve resume quality.

---

## ✨ Features

- 📄 Upload Resume in PDF format
- 📝 Paste Job Description
- 🔍 Automatic Resume Skill Extraction
- 💼 Automatic Job Skill Extraction
- 📊 ATS Score Calculation
- 📈 Detailed Score Breakdown
- ❌ Missing Skills Detection
- 💡 Resume Improvement Suggestions
- 🎨 Interactive Web Interface using Streamlit

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Streamlit | Web Application |
| PyPDF2 | PDF Text Extraction |
| Git | Version Control |
| GitHub | Source Code Hosting |

---

## 📂 Project Structure

```text
AI_Resume_Analyzer/
│
├── app.py
├── parser.py
├── skills.py
├── job_parser.py
├── ats_score.py
├── missing_skills.py
├── suggestions.py
├── utils.py
├── requirements.txt
├── sample_resume.pdf
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Jayanthi740/AI_Resume_Analyzer.git
```

### 2. Navigate to the Project Folder

```bash
cd AI_Resume_Analyzer
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
streamlit run app.py
```

The application will automatically open in your browser.

---

## 📌 How to Use

1. Launch the application.
2. Upload your Resume (PDF).
3. Paste the Job Description.
4. Click **Analyze**.
5. View:
   - Resume Skills
   - Job Skills
   - ATS Score
   - Score Breakdown
   - Missing Skills
   - Resume Suggestions

---

## 📊 Sample Output

### Resume Skills

- Python
- SQL
- HTML
- CSS
- JavaScript
- Git
- Machine Learning

### Job Required Skills

- Python
- SQL
- Django
- AWS
- Git

### ATS Report

- ✅ Overall ATS Score
- ✅ Skills Score
- ✅ Projects Score
- ✅ Education Score
- ✅ Experience Score
- ✅ Missing Skills
- ✅ Resume Suggestions

---

## 📸 Screenshots

### 🏠 Home Page

> Upload your Resume and paste the Job Description.

*Add `screenshots/home.png` here.*

### 📈 Analysis Result

Displays:

- Resume Skills
- Job Skills
- ATS Score
- Score Breakdown
- Missing Skills
- Suggestions

*Add `screenshots/result.png` here.*

---

## 🎯 Future Enhancements

- NLP-Based Resume Matching
- AI Resume Recommendations
- Resume Ranking System
- Download ATS Report as PDF
- Resume Keyword Highlighting
- Support for DOCX Files
- Dashboard with Charts

---

## 👩‍💻 Author

**Jayanthi**

🎓 B.Tech – Computer Science & Engineering

💻 Python Full Stack Developer

- 🐙 GitHub: https://github.com/Jayanthi740
- 💼 LinkedIn: https://www.linkedin.com/in/gh-jayanthi-397b67337/

---

## 🤝 Contributing

Contributions are welcome!

If you'd like to improve this project:

1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Push your branch.
5. Open a Pull Request.

---

## ⭐ Show Your Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

---

## 📄 License

This project is developed for educational and learning purposes.
