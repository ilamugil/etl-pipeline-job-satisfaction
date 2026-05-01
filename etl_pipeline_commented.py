# ============================================================
# PROJECT  : Job Satisfaction & Work-Life Balance Analysis
# AUTHOR   : Ilamugil K
# TOOL     : Python (pandas + sqlite3)
# PURPOSE  : ETL Pipeline - Extract, Transform, Load
# ============================================================


# --- Import Libraries ---
import pandas as pd       # pandas helps us read and clean data like Excel but in code
import sqlite3            # sqlite3 helps us create and use a database to store our data


# ============================================================
# STEP 1 : EXTRACT
# Read the raw data from CSV file into Python
# ============================================================

print("STEP 1 : Extracting data from CSV file...")

df = pd.read_csv("research_xxxx.csv")   # open the CSV file and load all rows into 'df' (dataframe = like a table)

print(f"Total rows loaded   : {len(df)}")      # print how many rows were loaded (should be 125)
print(f"Total columns loaded: {len(df.columns)}")  # print how many columns were loaded (should be 21)


# ============================================================
# STEP 2 : TRANSFORM
# Clean the data - rename columns, calculate scores, add labels
# ============================================================

print("\nSTEP 2 : Transforming data...")

# The original column names are very long and messy
# We rename all 21 columns to short clean names
df.columns = [
    "gender",                      # Column 1  : Gender of the employee
    "age",                         # Column 2  : Age group
    "marital_status",              # Column 3  : Married / Unmarried
    "area_of_locality",            # Column 4  : Where they live
    "family_members",              # Column 5  : Number of people in family
    "monthly_income",              # Column 6  : Monthly salary range
    "qualification",               # Column 7  : Education level
    "work_experience",             # Column 8  : Years of work experience
    "wlb_dependent_care",          # Column 9  : WLB - dependent care distracts from job (1-5 scale)
    "wlb_mental_worries",          # Column 10 : WLB - mental worries about family and work (1-5 scale)
    "wlb_fatigue",                 # Column 11 : WLB - tiredness due to family and personal work (1-5 scale)
    "wlb_family_problems",         # Column 12 : WLB - more time at work creates family problems (1-5 scale)
    "wlb_personal_needs",          # Column 13 : WLB - unable to fulfill personal needs due to workload (1-5 scale)
    "wlb_health_issues",           # Column 14 : WLB - health issues affect organizational work (1-5 scale)
    "js_happiness",                # Column 15 : JS  - happiness in performing work (1-5 scale)
    "js_career_elevation",         # Column 16 : JS  - organization helps career growth (1-5 scale)
    "js_no_gender_bias",           # Column 17 : JS  - no gender bias in organization (1-5 scale)
    "js_optimistic_colleagues",    # Column 18 : JS  - colleagues help in best performance (1-5 scale)
    "js_interpersonal_relationship",# Column 19: JS  - smooth relationship among employees (1-5 scale)
    "js_background_not_considered",# Column 20 : JS  - background not considered for performance (1-5 scale)
    "improvement_suggestion"       # Column 21 : suggestion for improving WLB and job satisfaction
]

print("Column renaming done!")

# --- Calculate Average Work Life Balance Score ---
wlb_cols = [                       # list all 6 Work Life Balance columns
    "wlb_dependent_care",
    "wlb_mental_worries",
    "wlb_fatigue",
    "wlb_family_problems",
    "wlb_personal_needs",
    "wlb_health_issues"
]

df["avg_wlb_score"] = df[wlb_cols].mean(axis=1).round(2)  # calculate average of 6 WLB columns for each row and round to 2 decimals

# --- Calculate Average Job Satisfaction Score ---
js_cols = [                        # list all 6 Job Satisfaction columns
    "js_happiness",
    "js_career_elevation",
    "js_no_gender_bias",
    "js_optimistic_colleagues",
    "js_interpersonal_relationship",
    "js_background_not_considered"
]

df["avg_js_score"] = df[js_cols].mean(axis=1).round(2)    # calculate average of 6 JS columns for each row and round to 2 decimals

# --- Add Satisfaction Label for each employee ---
def satisfaction_label(score):     # create a function that gives a label based on the score
    if score >= 4:                 # if average score is 4 or above → High satisfaction
        return "High"
    elif score >= 3:               # if average score is between 3 and 4 → Medium satisfaction
        return "Medium"
    else:                          # if average score is below 3 → Low satisfaction
        return "Low"

df["satisfaction_level"] = df["avg_js_score"].apply(satisfaction_label)  # apply the function to every row in avg_js_score column

print("Scores calculated and satisfaction labels added!")

# Show a small preview of the transformed data
print("\nSample of transformed data (first 5 rows):")
print(df[["gender", "age", "avg_wlb_score", "avg_js_score", "satisfaction_level"]].head())


# ============================================================
# STEP 3 : LOAD
# Save the cleaned data into a SQLite Database
# ============================================================

print("\nSTEP 3 : Loading data into database...")

conn = sqlite3.connect("employee_survey.db")   # create a new database file called employee_survey.db (or connect if it already exists)

df.to_sql(                          # save our dataframe into the database
    "employee_data",                # name of the table inside the database
    conn,                           # which database connection to use
    if_exists="replace",            # if table already exists, replace it with new data
    index=False                     # do not save the row numbers as a column
)

print("Data loaded into database table : employee_data")


# ============================================================
# STEP 4 : VALIDATE
# Run SQL queries to confirm data loaded correctly
# ============================================================

print("\nSTEP 4 : Validating data with SQL queries...")

# --- Query 1 : Check total number of records ---
total = pd.read_sql(
    "SELECT COUNT(*) as total_records FROM employee_data",   # SQL query to count all rows
    conn                                                      # run it on our database
)
print("\nTotal Records in Database:")
print(total)                        # should show 125

# --- Query 2 : Average WLB and JS scores grouped by gender ---
avg_by_gender = pd.read_sql("""
    SELECT
        gender,                                       -- group results by gender
        ROUND(AVG(avg_wlb_score), 2) as avg_wlb,     -- calculate average WLB score per gender
        ROUND(AVG(avg_js_score), 2)  as avg_js,      -- calculate average JS score per gender
        COUNT(*) as count                             -- count how many employees per gender
    FROM employee_data
    GROUP BY gender                                   -- separate results by each gender value
""", conn)
print("\nAverage Scores by Gender:")
print(avg_by_gender)

# --- Query 3 : How many employees fall in each satisfaction level ---
satisfaction_dist = pd.read_sql("""
    SELECT
        satisfaction_level,                           -- High / Medium / Low
        COUNT(*) as count,                            -- number of employees in each level
        ROUND(COUNT(*) * 100.0 /
            (SELECT COUNT(*) FROM employee_data), 1)  -- calculate percentage out of total
            as percentage
    FROM employee_data
    GROUP BY satisfaction_level                       -- group by satisfaction level
    ORDER BY count DESC                               -- show highest count first
""", conn)
print("\nSatisfaction Level Distribution:")
print(satisfaction_dist)

# --- Query 4 : Average scores grouped by marital status ---
by_marital = pd.read_sql("""
    SELECT
        marital_status,                               -- married / unmarried
        ROUND(AVG(avg_wlb_score), 2) as avg_wlb,     -- average WLB score
        ROUND(AVG(avg_js_score), 2)  as avg_js,      -- average JS score
        COUNT(*) as count                             -- number of employees
    FROM employee_data
    GROUP BY marital_status                           -- separate by marital status
""", conn)
print("\nScores by Marital Status:")
print(by_marital)

conn.close()                        # close the database connection after we are done

# ============================================================
# PIPELINE COMPLETE
# ============================================================

print("\n ETL Pipeline completed successfully!")
print(" Database saved as : employee_survey.db")
print(" Total records processed : 125")
