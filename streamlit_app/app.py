import streamlit as st
import pandas as pd
import pymysql
import matplotlib.pyplot as plt

def get_connection():
    return pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='root123',
        database='ola_db'
    )

def run_query(query):
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df

st.set_page_config(page_title="OLA Ride Insights", layout="wide")
st.title("🚗 OLA Ride Insights Dashboard")

menu = st.sidebar.selectbox("Select View", [
    "Overall",
    "Vehicle Type",
    "Revenue",
    "Cancellation",
    "Ratings"
])

if menu == "Overall":
    st.header("Overall Analysis")
    
    df = run_query("SELECT Booking_Status, COUNT(*) as Count FROM ola_rides GROUP BY Booking_Status")
    st.subheader("Booking Status Breakdown")
    fig, ax = plt.subplots()
    ax.pie(df['Count'], labels=df['Booking_Status'], autopct='%1.1f%%')
    st.pyplot(fig)
    
    df2 = run_query("SELECT DATE(Date) as Date, COUNT(*) as Rides FROM ola_rides GROUP BY DATE(Date) ORDER BY Date")
    st.subheader("Ride Volume Over Time")
    st.line_chart(df2.set_index('Date'))

elif menu == "Vehicle Type":
    st.header("Vehicle Type Analysis")
    df = run_query("SELECT Vehicle_Type, AVG(Ride_Distance) as Avg_Distance FROM ola_rides GROUP BY Vehicle_Type ORDER BY Avg_Distance DESC LIMIT 5")
    st.subheader("Top 5 Vehicle Types by Ride Distance")
    st.bar_chart(df.set_index('Vehicle_Type'))
    st.dataframe(df)

elif menu == "Revenue":
    st.header("Revenue Analysis")
    
    df = run_query("SELECT Payment_Method, SUM(Booking_Value) as Total_Revenue FROM ola_rides GROUP BY Payment_Method ORDER BY Total_Revenue DESC")
    st.subheader("Revenue by Payment Method")
    st.bar_chart(df.set_index('Payment_Method'))
    
    df2 = run_query("SELECT Customer_ID, SUM(Booking_Value) as Total_Value FROM ola_rides GROUP BY Customer_ID ORDER BY Total_Value DESC LIMIT 5")
    st.subheader("Top 5 Customers by Booking Value")
    st.bar_chart(df2.set_index('Customer_ID'))
    
    df3 = run_query("SELECT DATE(Date) as Date, SUM(Ride_Distance) as Total_Distance FROM ola_rides GROUP BY DATE(Date) ORDER BY Date")
    st.subheader("Ride Distance Distribution Per Day")
    st.line_chart(df3.set_index('Date'))

elif menu == "Cancellation":
    st.header("Cancellation Analysis")
    
    df = run_query("SELECT Canceled_Rides_by_Customer, COUNT(*) as Count FROM ola_rides WHERE Canceled_Rides_by_Customer != 'Not Cancelled' GROUP BY Canceled_Rides_by_Customer")
    st.subheader("Cancellation Reasons by Customer")
    st.bar_chart(df.set_index('Canceled_Rides_by_Customer'))
    st.dataframe(df)
    
    df2 = run_query("SELECT Canceled_Rides_by_Driver, COUNT(*) as Count FROM ola_rides WHERE Canceled_Rides_by_Driver != 'Not Cancelled' GROUP BY Canceled_Rides_by_Driver")
    st.subheader("Cancellation Reasons by Driver")
    st.bar_chart(df2.set_index('Canceled_Rides_by_Driver'))
    st.dataframe(df2)

elif menu == "Ratings":
    st.header("Ratings Analysis")
    
    df = run_query("SELECT Vehicle_Type, AVG(Driver_Ratings) as Avg_Driver_Rating, AVG(Customer_Rating) as Avg_Customer_Rating FROM ola_rides GROUP BY Vehicle_Type")
    st.subheader("Driver vs Customer Ratings by Vehicle Type")
    st.bar_chart(df.set_index('Vehicle_Type'))
    st.dataframe(df)