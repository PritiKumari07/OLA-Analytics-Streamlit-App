import streamlit as st
from db import run_query

st.title("📊 SQL Queries and Outputs")

queries = {
    "Retrieve all successful bookings": """
        SELECT * 
        FROM oladata
        WHERE "Booking_Status" = 'Success';
    """,

    "Average ride distance per vehicle type": """
        SELECT "Vehicle_Type", AVG("Ride_Distance") AS avg_distance
        FROM oladata
        WHERE "Ride_Distance" > 0
        GROUP BY "Vehicle_Type";
    """,

    "Total cancelled rides by customers": """
        SELECT COUNT(*) AS total_cancelled_by_customer
        FROM oladata
        WHERE "Booking_Status" = 'Canceled by Customer';
    """,

    "Top 5 customers with most rides": """
        SELECT "Customer_ID", COUNT(*) AS total_rides
        FROM oladata
        GROUP BY "Customer_ID"
        ORDER BY total_rides DESC
        LIMIT 5;
    """,

    "Driver cancellations (personal & car issues)": """
        SELECT COUNT(*) AS driver_cancel_personal_car
        FROM oladata
        WHERE "Canceled_Rides_by_Driver" = 'Personal & Car related issue';
    """,

    "Max & Min driver ratings for Prime Sedan": """
        SELECT MAX("Driver_Ratings") AS max_rating,
               MIN("Driver_Ratings") AS min_rating
        FROM oladata
        WHERE "Vehicle_Type" = 'Prime Sedan'
          AND "Driver_Ratings" <> 'Not Applicable';
    """,

    "Rides with UPI payments": """
        SELECT *
        FROM oladata
        WHERE "Payment_Method" = 'UPI';
    """,

    "Average customer rating per vehicle type": """
        SELECT "Vehicle_Type", AVG("Customer_Rating"::numeric) AS avg_customer_rating
        FROM oladata
        WHERE "Customer_Rating" <> 'Not Applicable'
        GROUP BY "Vehicle_Type";
    """,

    "Total booking value of successful rides": """
        SELECT SUM("Booking_Value") AS total_success_booking_value
        FROM oladata
        WHERE "Booking_Status" = 'Success';
    """,

    "Incomplete rides with reasons": """
        SELECT *
        FROM oladata
        WHERE "Incomplete_Rides" <> 'No'
          AND "Incomplete_Rides_Reason" <> 'Not Applicable';
    """
}

choice = st.selectbox("🔍 Select a query to run:", list(queries.keys()))

df = run_query(queries[choice])

if df is not None and not df.empty:
    st.dataframe(df)
else:
    st.info("No results found.")
