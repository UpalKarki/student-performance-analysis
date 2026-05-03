# Student Performance Analysis and Prediction System

A complete Data Science project analyzing student academic performance using Python, Pandas, and Machine Learning.

## 📌 Project Overview

This project explores how attendance and subject marks affect student academic performance. It follows a full Data Science workflow — from raw data to machine learning predictions.

**Built by:** Upal Karki  
**Goal:** Practice real-world Data Science skills as part of a learning roadmap toward a Data Scientist career.

---

## 📁 Project Structure

```
student-performance-analysis/
│
├── data/
│   ├── students.csv                      # Raw dataset (50 students)
│   ├── students_day4_analysis.csv        # Feature engineered data
│   ├── students_day6_cleaned.csv         # Cleaned data (missing values handled)
│   ├── students_day7_results.csv         # Performance categories added
│   ├── students_day9_predictions.csv     # Rule-based predictions
│   ├── students_day10_predictions.csv    # Linear Regression predictions
│   ├── students_day11_evaluation.txt     # Model evaluation metrics
│   ├── students_day12_evaluation.txt     # Improved model metrics
│   ├── students_day13_model_fit.txt      # Overfitting analysis
│   └── students_day14_classification.csv # Classification results
│
├── notebooks/
│   └── analysis.ipynb                    # Main Jupyter Notebook (Days 1–14)
│
├── src/
│   ├── day1_read_csv.py                  # Basic CSV reading script
│   └── day2_analysis.py                  # Manual analysis script
│
└── README.md
```

---

## 📊 Dataset

- **50 students** with realistic performance distribution
- **Columns:** student_id, name, gender, attendance (%), math, science, english

| Performance Level | Count |
|------------------|-------|
| High (avg ≥ 80)  | 15    |
| Medium (avg 60–79) | 25  |
| Low (avg < 60)   | 10    |

---

## 🔬 What This Project Covers

| Day | Topic |
|-----|-------|
| Day 1–2 | Reading CSV data with Python and Pandas |
| Day 3 | Exploratory Data Analysis (EDA) |
| Day 4 | Feature Engineering (total, average marks) |
| Day 5 | Correlation Analysis (attendance vs performance) |
| Day 6 | Data Cleaning (missing values, validation) |
| Day 7 | Performance Categorization (High / Medium / Low) |
| Day 8 | Data Visualization (bar charts, scatter plots) |
| Day 9 | Rule-Based Prediction |
| Day 10 | Linear Regression (first ML model) |
| Day 11 | Model Evaluation (MAE, R² Score) |
| Day 12 | Feature Engineering for ML improvement |
| Day 13 | Overfitting vs Underfitting analysis |
| Day 14 | Classification with Logistic Regression |

---

## 🔑 Key Findings

- **Attendance and average marks have a strong positive correlation (0.98+)**
- Students with attendance above 85% consistently fall in the High performance group
- Low-performing students had an average attendance below 55%
- Linear Regression achieved MAE ≈ 1.03 marks on test data
- Classification model correctly predicted performance categories with high accuracy

---

## 🛠️ Tools & Technologies

- **Python 3**
- **Pandas** — data manipulation
- **NumPy** — numerical operations
- **Matplotlib** — data visualization
- **Scikit-learn** — machine learning (LinearRegression, LogisticRegression, train_test_split)
- **Jupyter Notebook** — interactive analysis
- **Git & GitHub** — version control

---

## 🚀 How to Run

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/student-performance-analysis.git
cd student-performance-analysis

# Install dependencies
pip install pandas numpy matplotlib scikit-learn jupyter

# Launch Jupyter Notebook
jupyter notebook notebooks/analysis.ipynb
```

---

## 📈 Learning Goal

This project is part of a structured Data Science learning roadmap with the goal of becoming a Data Scientist, applying for internships in Nepal, and pursuing a Master's degree in Data Science abroad.