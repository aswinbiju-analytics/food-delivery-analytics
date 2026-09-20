import pandas as pd
import matplotlib.pyplot as plt
import os

# ==========================================
# FOOD DELIVERY ANALYSIS
# DATA VISUALIZATION
# ==========================================

# Load cleaned dataset
df = pd.read_csv("data/cleaned/food_delivery_cleaned.csv")

# Create Screenshot folder if it does not exist
os.makedirs("Screenshot", exist_ok=True)


# ==========================================
# 1. TOP 10 FOOD ITEMS BY ORDERS
# ==========================================

food_orders = (
    df.groupby("food_item")["order_id"]
    .count()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10, 6))
food_orders.plot(kind="bar")

plt.title("Top 10 Food Items by Number of Orders")
plt.xlabel("Food Item")
plt.ylabel("Number of Orders")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("Schreenshot/01_top_food_items.png", dpi=300)
plt.close()


# ==========================================
# 2. ORDERS BY LOCATION
# ==========================================

location_orders = (
    df.groupby("location")["order_id"]
    .count()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))
location_orders.plot(kind="bar")

plt.title("Orders by Location")
plt.xlabel("Location")
plt.ylabel("Number of Orders")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("Schreenshot/02_orders_by_location.png", dpi=300)
plt.close()


# ==========================================
# 3. REVENUE BY LOCATION
# ==========================================

location_revenue = (
    df.groupby("location")["order_value"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))
location_revenue.plot(kind="bar")

plt.title("Revenue by Location")
plt.xlabel("Location")
plt.ylabel("Revenue")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("Schreenshot/03_revenue_by_location.png", dpi=300)
plt.close()


# ==========================================
# 4. DELIVERY METHOD
# ==========================================

delivery_orders = df["delivery_method"].value_counts()

plt.figure(figsize=(8, 5))
delivery_orders.plot(kind="bar")

plt.title("Orders by Delivery Method")
plt.xlabel("Delivery Method")
plt.ylabel("Number of Orders")

plt.tight_layout()
plt.savefig("Schreenshot/04_orders_by_delivery_method.png", dpi=300)
plt.close()


# ==========================================
# 5. AVERAGE DELIVERY DELAY
# ==========================================

delay_by_method = (
    df.groupby("delivery_method")["delivery_delay"]
    .mean()
)

plt.figure(figsize=(8, 5))
delay_by_method.plot(kind="bar")

plt.title("Average Delivery Delay by Delivery Method")
plt.xlabel("Delivery Method")
plt.ylabel("Average Delay")

plt.tight_layout()
plt.savefig("Schreenshot/05_average_delay_by_method.png", dpi=300)
plt.close()


# ==========================================
# 6. MONTHLY ORDERS
# ==========================================

monthly_orders = (
    df.groupby("order_month")["order_id"]
    .count()
)

plt.figure(figsize=(10, 6))
monthly_orders.plot(kind="line", marker="o")

plt.title("Monthly Order Trend")
plt.xlabel("Month")
plt.ylabel("Number of Orders")

plt.xticks(range(1, 13))
plt.grid(True)

plt.tight_layout()
plt.savefig("Schreenshot/06_monthly_order_trend.png", dpi=300)
plt.close()


# ==========================================
# 7. TRAFFIC VS DELIVERY DELAY
# ==========================================

traffic_delay = (
    df.groupby("traffic_condition")["delivery_delay"]
    .mean()
)

plt.figure(figsize=(8, 5))
traffic_delay.plot(kind="bar")

plt.title("Average Delivery Delay by Traffic Condition")
plt.xlabel("Traffic Condition")
plt.ylabel("Average Delivery Delay")

plt.tight_layout()
plt.savefig("Schreenshot/07_traffic_vs_delay.png", dpi=300)
plt.close()


# ==========================================
# 8. WEATHER VS DELIVERY DELAY
# ==========================================

weather_delay = (
    df.groupby("weather_condition")["delivery_delay"]
    .mean()
)

plt.figure(figsize=(8, 5))
weather_delay.plot(kind="bar")

plt.title("Average Delivery Delay by Weather Condition")
plt.xlabel("Weather Condition")
plt.ylabel("Average Delivery Delay")

plt.tight_layout()
plt.savefig("Schreenshot/08_weather_vs_delay.png", dpi=300)
plt.close()


# ==========================================
# 9. LOYALTY PROGRAM
# ==========================================

loyalty_orders = df["loyalty_program"].value_counts()

plt.figure(figsize=(7, 5))
loyalty_orders.plot(kind="bar")

plt.title("Orders by Loyalty Program")
plt.xlabel("Loyalty Program")
plt.ylabel("Number of Orders")

plt.tight_layout()
plt.savefig("Schreenshot/09_loyalty_program.png", dpi=300)
plt.close()


# ==========================================
# 10. CUSTOMER SATISFACTION
# ==========================================

satisfaction_orders = (
    df["customer_satisfaction"]
    .value_counts()
    .sort_index()
)

plt.figure(figsize=(8, 5))
satisfaction_orders.plot(kind="bar")

plt.title("Customer Satisfaction Distribution")
plt.xlabel("Satisfaction Score")
plt.ylabel("Number of Orders")

plt.tight_layout()
plt.savefig("Schreenshot/10_customer_satisfaction.png", dpi=300)
plt.close()


# ==========================================
# COMPLETED
# ==========================================

print("\n==========================================")
print("VISUALIZATION COMPLETED")
print("==========================================")

print("\n10 charts saved successfully in:")
print("Schreenshot/")
