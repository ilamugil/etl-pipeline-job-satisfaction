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

##  Author

**Ilamugil K**
MBA — Business Analytics | Crescent School of Business, Chennai
 ilamugilk15@gmail.com
🔗 [LinkedIn](https://www.linkedin.com/in/ilamugil-kaliyaperuma)
🔗 [GitHub](https://github.com/ilamugil)
