# 🤖 AI Resume Analyzer

An AI-powered Resume Analyzer built using **Python** and **Streamlit** that analyzes a resume against a job description, calculates an ATS (Applicant Tracking System) score, identifies missing skills, and provides personalized suggestions to improve the resume.

---

## 📖 Overview

The AI Resume Analyzer helps job seekers evaluate how well their resume matches a specific job description. It extracts technical skills from both the resume and the job description, compares them, calculates an ATS score, highlights missing skills, and provides useful recommendations to improve the chances of passing ATS screening.

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

## 🛠️ Technologies Used

- Python
- Streamlit
- PyPDF2
- Git
- GitHub

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

## 🚀 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Jayanthi740/AI_Resume_Analyzer.git
```

### 2️⃣ Navigate to the Project Folder

```bash
cd AI_Resume_Analyzer
```

### 3️⃣ Install Required Packages

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

## 📌 How to Use

1. Launch the application.
2. Upload your Resume (PDF format).
3. Paste the Job Description into the text box.
4. The system will:
   - Extract Resume Skills
   - Extract Job Skills
   - Calculate ATS Score
   - Display Score Breakdown
   - Identify Missing Skills
   - Provide Resume Improvement Suggestions

---

## 📊 Example Output

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

### ATS Analysis

- Overall ATS Score
- Skills Score
- Projects Score
- Education Score
- Experience Score

### Missing Skills

- Django
- AWS

### Suggestions

- Improve your resume by adding Django skill.
- Improve your resume by adding AWS skill.

---

## 📸 Screenshots

### Home Page

Upload your Resume and paste the Job Description.

> Add a screenshot here after uploading your project.

### Analysis Result

Displays:

- Resume Skills
- Job Skills
- ATS Score
- Score Breakdown
- Missing Skills
- Suggestions

> Add a screenshot here after uploading your project.

---

## 🎯 Future Improvements

- NLP-based Resume Matching
- AI Resume Recommendations
- Resume Ranking System
- Download ATS Report as PDF
- Resume Keyword Highlighting
- Support for DOCX Files
- Dashboard with Charts and Graphs

---

## 👩‍💻 Author

**Jayanthi**

🎓 B.Tech – Computer Science & Engineering

💻 Python Full Stack Developer

🐙 GitHub: https://github.com/Jayanthi740

💼 LinkedIn: https://www.linkedin.com/in/gh-jayanthi-397b67337/

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

If you would like to contribute:

1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Push your branch.
5. Create a Pull Request.

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

---

## 📄 License

This project is developed for educational and learning purposes.
