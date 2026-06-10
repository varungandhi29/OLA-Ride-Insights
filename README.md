# OLA Ride Insights

## Project Overview
Analysis of OLA ride-sharing data to extract business insights using SQL, Python and Streamlit.

## Dataset
- 103,024 rows of OLA ride data
- 20 columns including booking status, vehicle type, ratings, revenue

## Tech Stack
- Python (Pandas, Matplotlib)
- MySQL
- Streamlit
- SQL

## Project Structure
- `data/` - Raw and cleaned dataset
- `sql/` - SQL queries
- `streamlit_app/` - Streamlit application
- `data_cleaning.py` - Data cleaning script

## Key Insights
- Booking status breakdown across all rides
- Top vehicle types by ride distance
- Revenue analysis by payment method
- Cancellation reasons by customer and driver
- Driver vs customer ratings comparison

## How to Run
1. Install dependencies: `pip install pandas pymysql streamlit matplotlib sqlalchemy`
2. Import data to MySQL: `python data_cleaning.py`
3. Run Streamlit app: `cd streamlit_app && python -m streamlit run app.py`

## Author
Varun Gandhi
