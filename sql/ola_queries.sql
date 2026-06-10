USE ola_db;

-- Query 1: All successful bookings
SELECT * FROM ola_rides WHERE Booking_Status = 'Success';

-- Query 2: Average ride distance per vehicle type
SELECT Vehicle_Type, AVG(Ride_Distance) AS Avg_Distance 
FROM ola_rides GROUP BY Vehicle_Type;

-- Query 3: Total cancelled rides by customers
SELECT COUNT(*) AS Total_Cancelled 
FROM ola_rides WHERE Canceled_Rides_by_Customer != 'Not Cancelled';

-- Query 4: Top 5 customers by number of rides
SELECT Customer_ID, COUNT(*) AS Total_Rides 
FROM ola_rides GROUP BY Customer_ID 
ORDER BY Total_Rides DESC LIMIT 5;

-- Query 5: Driver cancellations
SELECT COUNT(*) AS Driver_Cancelled 
FROM ola_rides WHERE Canceled_Rides_by_Driver != 'Not Cancelled';

-- Query 6: Max and min driver ratings for Prime Sedan
SELECT MAX(Driver_Ratings) AS Max_Rating, MIN(Driver_Ratings) AS Min_Rating 
FROM ola_rides WHERE Vehicle_Type = 'Prime Sedan';

-- Query 7: All UPI payment rides
SELECT * FROM ola_rides WHERE Payment_Method = 'UPI';

-- Query 8: Average customer rating per vehicle type
SELECT Vehicle_Type, AVG(Customer_Rating) AS Avg_Customer_Rating 
FROM ola_rides GROUP BY Vehicle_Type;

-- Query 9: Total booking value of completed rides
SELECT SUM(Booking_Value) AS Total_Revenue 
FROM ola_rides WHERE Booking_Status = 'Success';

-- Query 10: All incomplete rides with reasons
SELECT Booking_ID, Incomplete_Rides_Reason 
FROM ola_rides WHERE Incomplete_Rides = 'Yes';