## DecodeLabs Virtual Internship — Data Analytics Track  

A summer internship program where I'm working through structured, real-world data projects — from raw messy data all the way to analysis and insights.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white)
![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=flat-square&logo=visualstudiocode&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)

---

### About

**Organization:** DecodeLabs  
**Track:** Data Analytics  
**Dataset:** E-commerce orders  
**Duration:** Summer 2026  

Each project in this program focuses on one phase of a real data workflow. The projects build on each other — Project 1's cleaned output feeds directly into Project 2's analysis, and Project 3 takes the same dataset into SQL-based querying.

---

### Projects

#### Project 1 — Data Cleaning & Preparation

**What I worked on:**

- Identified and handled missing values in the `CouponCode` column
- Detected and removed duplicate records
- Validated `OrderID` uniqueness across the dataset
- Verified that `Quantity` and `UnitPrice` values were within valid ranges
- Cross-checked `TotalPrice` against expected `Quantity × UnitPrice` values
- Checked consistency between the `Quantity` and `ItemsInCart` columns
- Standardized formatting across categorical columns
- Extracted `Year` and `Month` features from the `Date` column for time-based analysis
- Exported the cleaned dataset for use in Project 2

📁 [`data_cleaning.ipynb`](./Project-1/data_cleaning.ipynb)

---

#### Project 2 — Exploratory Data Analysis (EDA)

**What I worked on:**

- Computed descriptive statistics for all numerical features
- Analyzed distributions of categorical variables
- Explored monthly and yearly sales trends using the date features from Project 1
- Ranked top-performing products by both sales volume and revenue
- Broke down orders by payment method and order status
- Analyzed which customer acquisition sources drove the most orders
- Built a correlation matrix to examine relationships between numerical variables
- Created visualizations — bar charts, distribution plots, heatmaps — to support each finding
- Documented key findings and business insights 
 
📁 [`EDA.ipynb`](./Project-2/EDA.ipynb)

---

#### Project 3 — SQL-Based Data Analysis

**What I worked on:**

- Queried the e-commerce dataset using SQL to extract business insights
- Analyzed revenue and order count by payment method, referral source, and order status
- Identified top-performing products by sales volume and revenue
- Explored monthly sales trends to find peak periods
- Analyzed customer purchase frequency and retention patterns
- Documented actionable insights based on query results

📁 [`sql_queries.sql`](./Project-3/sql_queries.sql)
📁 [`key_findings.text`](./Project-3/key_findings.text)

---

### Tools Used

| Purpose | Tool |
|---|---|
| Language | Python, SQL |
| Data manipulation | Pandas |
| Visualization | Matplotlib, Seaborn |
| Environment | Jupyter Notebook |
| Editor | VS Code |
| Version control | Git & GitHub |

---

### About Me

I'm Chandni, a 2nd-year B.Tech (IoT) student at MITS-DU (2024–28). I'm doing this internship over my summer break to build real, practical skills in data analytics — working toward a career in Data Science and Data Analytics.

