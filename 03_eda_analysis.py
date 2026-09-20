import pandas as pd

# ==========================================
# FOOD DELIVERY ANALYSIS
# EXPLORATORY DATA ANALYSIS
# ==========================================

# Load cleaned dataset
df = pd.read_csv("data/cleaned/food_delivery_cleaned.csv")

print("Dataset Shape:", df.shape)


# ==========================================
# 1. TOTAL ORDERS
# ==========================================

print("\n========== TOTAL ORDERS ==========")

total_orders = df["order_id"].nunique()

print("Total Orders:", total_orders)


# ==========================================
# 2. TOTAL REVENUE
# ==========================================

print("\n========== TOTAL REVENUE ==========")

total_revenue = df["order_value"].sum()

print("Total Revenue:", round(total_revenue, 2))


# ==========================================
# 3. AVERAGE ORDER VALUE
# ==========================================

print("\n========== AVERAGE ORDER VALUE ==========")

average_order_value = df["order_value"].mean()

print("Average Order Value:", round(average_order_value, 2))


# ==========================================
# 4. FOOD ITEM ORDER ANALYSIS
# ==========================================

print("\n========== TOP FOOD ITEMS ==========")

food_orders = (
    df.groupby("food_item")
    .agg(
        total_orders=("order_id", "count"),
        total_revenue=("order_value", "sum"),
        average_order_value=("order_value", "mean")
    )
    .sort_values("total_orders", ascending=False)
)

print(food_orders)


# ==========================================
# 5. LOCATION ANALYSIS
# ==========================================

print("\n========== LOCATION ANALYSIS ==========")

location_analysis = (
    df.groupby("location")
    .agg(
        total_orders=("order_id", "count"),
        total_revenue=("order_value", "sum"),
        average_order_value=("order_value", "mean")
    )
    .sort_values("total_orders", ascending=False)
)

print(location_analysis)


# ==========================================
# 6. DELIVERY METHOD ANALYSIS
# ==========================================

print("\n========== DELIVERY METHOD ANALYSIS ==========")

delivery_analysis = (
    df.groupby("delivery_method")
    .agg(
        total_orders=("order_id", "count"),
        average_delay=("delivery_delay", "mean"),
        average_distance=("delivery_distance", "mean"),
        average_rating=("customer_rating", "mean"),
        average_satisfaction=("customer_satisfaction", "mean")
    )
    .sort_values("total_orders", ascending=False)
)

print(delivery_analysis)


# ==========================================
# 7. TRAFFIC ANALYSIS
# ==========================================

print("\n========== TRAFFIC ANALYSIS ==========")

traffic_analysis = (
    df.groupby("traffic_condition")
    .agg(
        total_orders=("order_id", "count"),
        average_delay=("delivery_delay", "mean"),
        average_distance=("delivery_distance", "mean"),
        average_satisfaction=("customer_satisfaction", "mean")
    )
    .sort_values("average_delay", ascending=False)
)

print(traffic_analysis)


# ==========================================
# 8. WEATHER ANALYSIS
# ==========================================

print("\n========== WEATHER ANALYSIS ==========")

weather_analysis = (
    df.groupby("weather_condition")
    .agg(
        total_orders=("order_id", "count"),
        average_delay=("delivery_delay", "mean"),
        average_satisfaction=("customer_satisfaction", "mean")
    )
    .sort_values("average_delay", ascending=False)
)

print(weather_analysis)


# ==========================================
# 9. LOYALTY PROGRAM ANALYSIS
# ==========================================

print("\n========== LOYALTY PROGRAM ANALYSIS ==========")

loyalty_analysis = (
    df.groupby("loyalty_program")
    .agg(
        total_orders=("order_id", "count"),
        total_revenue=("order_value", "sum"),
        average_order_value=("order_value", "mean"),
        average_rating=("customer_rating", "mean"),
        average_satisfaction=("customer_satisfaction", "mean")
    )
)

print(loyalty_analysis)


# ==========================================
# 10. CUSTOMER SATISFACTION
# ==========================================

print("\n========== CUSTOMER SATISFACTION ==========")

satisfaction_analysis = (
    df.groupby("customer_satisfaction")
    .agg(
        total_orders=("order_id", "count"),
        average_rating=("customer_rating", "mean"),
        average_delay=("delivery_delay", "mean"),
        average_order_value=("order_value", "mean")
    )
)

print(satisfaction_analysis)


# ==========================================
# 11. FOOD CONDITION ANALYSIS
# ==========================================

print("\n========== FOOD CONDITION ANALYSIS ==========")

food_condition_analysis = (
    df.groupby("food_condition")
    .agg(
        total_orders=("order_id", "count"),
        average_rating=("customer_rating", "mean"),
        average_satisfaction=("customer_satisfaction", "mean"),
        average_delay=("delivery_delay", "mean")
    )
    .sort_values("average_satisfaction", ascending=False)
)

print(food_condition_analysis)


# ==========================================
# 12. MONTHLY ORDER ANALYSIS
# ==========================================

print("\n========== MONTHLY ANALYSIS ==========")

monthly_analysis = (
    df.groupby(["order_month", "order_month_name"])
    .agg(
        total_orders=("order_id", "count"),
        total_revenue=("order_value", "sum"),
        average_order_value=("order_value", "mean")
    )
    .sort_index()
)

print(monthly_analysis)


# ==========================================
# 13. ROUTE ANALYSIS
# ==========================================

print("\n========== ROUTE TYPE ANALYSIS ==========")

route_analysis = (
    df.groupby("route_type")
    .agg(
        total_orders=("order_id", "count"),
        average_delay=("delivery_delay", "mean"),
        average_efficiency=("route_efficiency", "mean"),
        average_satisfaction=("customer_satisfaction", "mean")
    )
    .sort_values("average_efficiency", ascending=False)
)

print(route_analysis)


print("\n==========================================")
print("EDA ANALYSIS COMPLETED")
print("==========================================")