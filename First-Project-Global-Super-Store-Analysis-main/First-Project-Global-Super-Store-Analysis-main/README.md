# First-Project-Global-Super-Store-Analysis

# Global Superstore Sales Analysis
The Global Superstore Sales Analysis repository showcases a comprehensive Power BI dashboard that provides valuable insights into sales performance. This project is designed to present key information and trends to stakeholders, enabling informed decision-making.
### Check out the presentation of the Global Superstore Sales Analysis Dashboard here⤵:
Link to watch 
## Key Features
### ✅Key Performance Indicators (KPIs): 
The dashboard prominently displays essential metrics such as total sales, total profit, total units sold, total number of products, total number of customers, and total orders. These KPIs provide a snapshot of the company's sales performance.

### ✅Doughnut Charts: 
The dashboard includes four interactive doughnut charts offering insights into different sales aspects. These charts depict the distribution of orders by ship mode, sales by category, top 5 states by sales, and top 5 cities by sales. This information helps identify trends, preferences, and opportunities for targeted strategies.

### ✅Sales Trend Column Chart: 
The main sales trend column chart illustrates the overall sales trend over time, specifically by quarter. It highlights the upward trend, indicating consistent growth in sales. The chart also enables a deeper analysis of individual sales figures for countries, states, and cities.

### ✅Map Chart: 
A map chart is incorporated to provide a geographic perspective on sales. It visually represents sales data across different regions, allowing stakeholders to identify regional strengths and opportunities for expansion.

## Power BI Dashboard
## Power BI Dashboard
<img width="757" alt="Global Store Sales pix" src="https://github.com/user-attachments/assets/5cb69e33-59e1-47b3-88da-66f170ccb2bb" />

[![Power BI Dashboard](https://github.com/EphzibahBehulah/First-Project-Global-Super-Store-Analysis/assets/your-image-id)](https://app.powerbi.com/groups/me/reports/02eadeae-00c5-47f0-8c10-803973255708/742bbb5a7d7cc14ae90d?experience=power-bi)

### Main code

import pandas as pd
import openpyxl
file_path = "GlobalSuperstore.xlsx"
df = pd.read_excel(file_path)
print(df.head())

# check the data types of the columns
print(df.dtypes)




