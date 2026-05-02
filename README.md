#  ETL Pipeline — Job Satisfaction & Work-Life Balance

A data engineering project that builds a complete ETL (Extract, Transform, Load) pipeline using Python and SQL on real employee survey data.

---

##  Objective

To design and implement a real-world ETL pipeline that reads raw survey data, cleans and transforms it, loads it into a SQLite database, and validates the output using SQL queries.

---

##  Pipeline Overview

| Stage | What Happens |
|-------|-------------|
| **Extract** | Read 125 employee survey responses from CSV file |
| **Transform** | Rename 21 columns, calculate avg WLB & JS scores, add satisfaction labels |
| **Load** | Store clean data into SQLite database |
| **Validate** | Run SQL queries to confirm data and generate insights |

---

##  Files in This Repo

| File | Description |
|------|-------------|
| `etl_pipeline_commented.py` | Full ETL pipeline code with comments on every line |
| `research.csv` | Raw survey data — 125 employee responses |

---

##  Tools & Technologies

| Tool | Purpose |
|------|---------|
| Python | Core programming language |
| Pandas | Data reading, cleaning, transformation |
| SQLite3 | Database storage |
| SQL | Data validation and querying |
| Google Colab | Cloud-based execution |
| GitHub | Version control |

---

##  Dataset

- **Responses**: 125 employees
- **Columns**: 21 variables
- **Categories**: Demographics, Work-Life Balance (6 items), Job Satisfaction (6 items)
- **Scale**: Likert Scale 1 to 5

---

##  Key Results

| Satisfaction Level | Count | Percentage |
|-------------------|-------|------------|
| Medium | 57 | 45.6% |
| Low | 39 | 31.2% |
| High | 29 | 23.2% |

---

##  How to Run

1. Open [Google Colab](https://colab.research.google.com)
2. Upload `research.csv` using the  folder icon on the left
3. Create a new notebook and paste the code from `etl_pipeline_commented.py`
4. Change line 8 to: `df = pd.read_csv("/content/research.csv")`
5. Press ▶ Run — results will appear below!

---

##  Sample SQL Queries Used

```sql
-- Total records loaded
SELECT COUNT(*) as total_records FROM employee_data;

-- Average scores by gender
SELECT gender,
       ROUND(AVG(avg_wlb_score), 2) as avg_wlb,
       ROUND(AVG(avg_js_score), 2) as avg_js
FROM employee_data
GROUP BY gender;

-- Satisfaction level distribution
SELECT satisfaction_level, COUNT(*) as count
FROM employee_data
GROUP BY satisfaction_level
ORDER BY count DESC;
```

---
#  Job Satisfaction & Work-Life Balance Analysis

A data analysis project built using Python to study the relationship between Work-Life Balance and Job Satisfaction among employees.

---

##  Objective

To analyze how work-life balance factors such as dependent care, mental stress, fatigue, and health issues impact employee job satisfaction — using real survey data collected from 125 employees.

---

##  Dataset

- **Source**: Primary data collected via Google Forms survey
- **Responses**: 125 employees
- **Variables**: 21 columns covering demographics, work-life balance, and job satisfaction
- **Scale**: Likert Scale (1 to 5)

---

## 🛠️ Tools & Libraries Used

| Tool | Purpose |
|------|---------|
| Python | Core programming language |
| Pandas | Data cleaning and manipulation |
| NumPy | Numerical calculations |
| Matplotlib | Data visualization |
| Seaborn | Statistical charts and heatmaps |
| Scikit-learn | Linear Regression model |
| Google Colab | Cloud-based code execution |

---

##  What I Did

- Designed a structured questionnaire and collected 125 responses using Google Forms
- Cleaned and converted text data to numeric values for analysis
- Performed Exploratory Data Analysis (EDA) using histograms, KDE plots, swarm plots
- Built a correlation heatmap to find relationships between WLB and JS variables
- Applied Linear Regression with 80/20 train-test split to predict job satisfaction
- Evaluated model using R² Score and Mean Squared Error (MSE)

---

##  Key Findings

- Work overload and dependent care responsibilities significantly impact job satisfaction
- Only 23% of employees report High satisfaction
- Female employees reported slightly lower WLB and JS scores compared to male employees
- Strong negative correlation found between fatigue and job satisfaction

---

##  Results

| Satisfaction Level | Count | Percentage |
|-------------------|-------|------------|
| Medium | 57 | 45.6% |
| Low | 39 | 31.2% |
| High | 29 | 23.2% |

---

##  How to Run

1. Open [Google Colab](https://colab.research.google.com)
2. Upload the dataset CSV file
3. Open the `.ipynb` notebook file
4. Run all cells from top to bottom

---

## Author

**Ilamugil K**
MBA — Business Analytics | Crescent School of Business, Chennai
 ilamugilk15@gmail.com
🔗 [LinkedIn](https://www.linkedin.com/in/ilamugil-kaliyaperuma)

| Employee_Survey_PowerBI.pbix | Power BI Dashboard — Satisfaction, Gender, Marital analysis |
| Employee_Survey_Dashboard.xlsx | Excel Dashboard with charts and summary tables |

##  Author

**Ilamugil K**
MBA — Business Analytics | Crescent School of Business, Chennai
 ilamugilk15@gmail.com
🔗 [LinkedIn](https://www.linkedin.com/in/ilamugil-kaliyaperuma)
🔗 [GitHub](https://github.com/ilamugil)
