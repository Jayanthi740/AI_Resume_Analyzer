# 🤖 AI Resume Analyzer

An AI-powered Resume Analyzer built using **Python** and **Streamlit** that evaluates a resume against a job description, calculates an **ATS (Applicant Tracking System) Score**, identifies missing skills, and provides personalized suggestions to improve resume quality.

---

## 🔗 Project Links

🐙 **GitHub Repository**

https://github.com/Jayanthi740/AI_Resume_Analyzer

📥 **Clone Repository**

```bash
git clone https://github.com/Jayanthi740/AI_Resume_Analyzer.git
```

🌐 **Live Demo**

Coming Soon...

---

## 🚀 Overview

The **AI Resume Analyzer** helps job seekers evaluate how well their resume matches a job description. It extracts technical skills from both the resume and the job description, compares them, calculates an ATS score, highlights missing skills, and provides recommendations to improve the resume for better job opportunities.

---

## ✨ Features

- 📄 Upload Resume in PDF format
- 📝 Paste Job Description
- 🔍 Automatic Resume Skill Extraction
- 💼 Automatic Job Skill Extraction
- 📊 Overall ATS Score Calculation
- 📈 Detailed Score Breakdown
- ❌ Missing Skills Detection
- 💡 Resume Improvement Suggestions
- 🎨 Interactive Streamlit Web Interface

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Streamlit | Web Application |
| PyPDF2 | PDF Parsing |
| Git | Version Control |
| GitHub | Repository Hosting |

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

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Jayanthi740/AI_Resume_Analyzer.git
```

### 2️⃣ Navigate to the Project Folder

```bash
cd AI_Resume_Analyzer
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```bash
streamlit run app.py
```

The application will automatically open in your browser at:

```text
http://localhost:8501
```

---

## 📌 How to Use

1. Launch the application.
2. Upload your Resume (PDF format).
3. Paste the Job Description.
4. Click **Analyze**.
5. View:
   - Resume Skills
   - Job Required Skills
   - Overall ATS Score
   - Score Breakdown
   - Missing Skills
   - Resume Improvement Suggestions

---

## 📊 Sample Output

### 📌 Resume Skills

- Python
- SQL
- HTML
- CSS
- JavaScript
- Git
- Machine Learning

### 📌 Job Required Skills

- Python
- SQL
- Django
- AWS
- Git

### 📊 ATS Report

- Overall ATS Score
- Skills Score
- Projects Score
- Education Score
- Experience Score

### ❌ Missing Skills

- Django
- AWS

### 💡 Suggestions

- Improve your resume by adding Django skill.
- Improve your resume by adding AWS skill.

---

## 📸 Screenshots

### 🏠 Home Page

Upload your resume and paste the job description.

> Add a screenshot named **home.png** inside the `screenshots` folder.

### 📈 Analysis Result

Displays:

- Resume Skills
- Job Required Skills
- ATS Score
- Score Breakdown
- Missing Skills
- Suggestions

> Add a screenshot named **result.png** inside the `screenshots` folder.

---

## 🎯 Future Enhancements

- NLP-Based Resume Matching
- AI Resume Recommendations
- Resume Ranking System
- Download ATS Report as PDF
- Resume Keyword Highlighting
- Support for DOCX Files
- Interactive Dashboard
- Multi-Resume Comparison

---

## 👩‍💻 Author

**Jayanthi**

🎓 B.Tech – Computer Science & Engineering

💻 Python Full Stack Developer

🐙 GitHub: https://github.com/Jayanthi740

💼 LinkedIn: https://www.linkedin.com/in/gh-jayanthi-397b67337/

---

## 🤝 Contributing

Contributions are welcome!

If you would like to contribute:

1. Fork this repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push your branch.
5. Open a Pull Request.

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

---

## 📄 License

This project is developed for educational and learning purposes.

---

### 🙏 Thank You

Thank you for visiting this repository. If you have any suggestions or feedback, feel free to open an issue or submit a pull request.
