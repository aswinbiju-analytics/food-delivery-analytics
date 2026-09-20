import pandas as pd
import mysql.connector

# ==========================================
# FOOD DELIVERY DATA IMPORT
# CSV → MYSQL
# ==========================================

# CSV file path
csv_file = "data/cleaned/food_delivery_cleaned.csv"

# Load cleaned CSV
df = pd.read_csv(csv_file)

print("CSV loaded successfully!")
print("Total rows:", len(df))
print("Total columns:", len(df.columns))


# ==========================================
# CONNECT TO MYSQL
# ==========================================

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR SQL PASSWORD",
    database="food_delivery_analytics"
)

cursor = connection.cursor()

print("Connected to MySQL successfully!")


# ==========================================
# PREPARE DATA
# ==========================================

# Convert date columns
df["order_time"] = pd.to_datetime(df["order_time"]).dt.date
df["delivery_time"] = pd.to_datetime(df["delivery_time"]).dt.date


# Convert Boolean columns to integers
# Convert Yes/No and Boolean values to 1/0
df["small_route"] = df["small_route"].astype(int)
df["bike_friendly_route"] = df["bike_friendly_route"].astype(int)

df["traffic_avoidance"] = (
    df["traffic_avoidance"]
    .astype(str)
    .str.strip()
    .str.lower()
    .map({"yes": 1, "no": 0})
)

# Convert dataframe rows into tuples
data = list(df.itertuples(index=False, name=None))

print("Prepared rows:", len(data))
print("Values per row:", len(data[0]))


# ==========================================
# INSERT QUERY
# ==========================================

insert_query = """
INSERT INTO food_delivery (
    order_id,
    restaurant_id,
    food_item,
    order_time,
    delivery_time,
    delivery_distance,
    order_value,
    delivery_method,
    traffic_condition,
    weather_condition,
    delivery_delay,
    route_taken,
    customer_id,
    age,
    gender,
    location,
    order_history,
    customer_rating,
    preferred_cuisine,
    order_frequency,
    loyalty_program,
    food_temperature,
    food_freshness,
    packaging_quality,
    food_condition,
    customer_satisfaction,
    small_route,
    bike_friendly_route,
    route_type,
    route_efficiency,
    traffic_avoidance,
    order_year,
    order_month,
    order_month_name,
    order_day,
    order_day_name,
    delivery_status
)
VALUES (
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s, %s
)
"""


# ==========================================
# VERIFY PLACEHOLDER COUNT
# ==========================================

placeholder_count = insert_query.count("%s")

print("SQL placeholders:", placeholder_count)

if placeholder_count != len(data[0]):
    print("ERROR: Column/value count does not match!")
    cursor.close()
    connection.close()
    exit()

print("Column/value count matched!")


# ==========================================
# INSERT DATA
# ==========================================

try:

    cursor.executemany(insert_query, data)

    connection.commit()

    print("\nData inserted successfully!")
    print("Rows inserted:", cursor.rowcount)

except Exception as e:

    connection.rollback()

    print("\nError while inserting data:")
    print(e)


# ==========================================
# CLOSE CONNECTION
# ==========================================

cursor.close()
connection.close()

print("\n==========================================")
print("DATA IMPORT COMPLETED")
print("==========================================")