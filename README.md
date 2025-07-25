# The Fresh Connection KPI Dashboard

This interactive Streamlit dashboard provides functional and financial KPI analysis across 6 rounds of "The Fresh Connection" simulation.

## 📁 Folder Structure

/your-repo
│
├── app.py
├── requirements.txt
├── README.md
└── /data
├── finance_report.csv
├── supplier.csv
├── product.csv
├── customer.csv
├── component.csv
├── supplier_component.csv
├── warehouse.csv
├── bottling_line.csv
└── mixers.csv

markdown
Copy
Edit

## 🚀 Deployment Instructions

1. Upload all files to a GitHub repo (public or private).
2. Visit [https://streamlit.io/cloud](https://streamlit.io/cloud).
3. Click **New App** > Select your GitHub repo.
4. Set `Main file path` to `app.py`.
5. Click **Deploy**.

## 🎯 Features

- 4 Tab Layout: Purchase, Sales, Supply Chain, Operations
- Interactive filtering by Round
- Visual analysis of KPIs using bar charts
- Designed to prioritize suppliers, customers, and components impacting ROI and COGS

## 📊 KPI Coverage

### Purchase Tab
- Delivery Reliability
- Rejection %
- Raw Material Cost

### Sales Tab
- Forecast Error
- Service Level
- Attained Shelf Life

### Supply Chain Tab
- Component Availability
- Product Availability (OSA)

### Operations Tab
- Warehouse Cube Utilization
- Production Plan Adherence
