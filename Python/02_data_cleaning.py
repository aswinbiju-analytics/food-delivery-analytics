import pandas as pd
import os

# ==========================================
# FOOD DELIVERY ANALYSIS
# DATA CLEANING
# ==========================================

# Load raw dataset
df = pd.read_csv("data/raw/food_delivery_dataset.csv")

print("Original Shape:", df.shape)


# ==========================================
# 1. REMOVE EXTRA SPACES FROM TEXT COLUMNS
# ==========================================

text_columns = df.select_dtypes(include=["object", "string"]).columns

for column in text_columns:
    df[column] = df[column].str.strip()


# ==========================================
# 2. CONVERT DATE COLUMNS
# ==========================================

df["order_time"] = pd.to_datetime(
    df["order_time"],
    errors="coerce"
)

df["delivery_time"] = pd.to_datetime(
    df["delivery_time"],
    errors="coerce"
)


# ==========================================
# 3. CHECK INVALID DATES
# ==========================================

print("\n========== INVALID DATES ==========")

print(
    "Invalid order dates:",
    df["order_time"].isna().sum()
)

print(
    "Invalid delivery dates:",
    df["delivery_time"].isna().sum()
)


# ==========================================
# 4. CREATE DATE FEATURES
# ==========================================

df["order_year"] = df["order_time"].dt.year

df["order_month"] = df["order_time"].dt.month

df["order_month_name"] = df["order_time"].dt.month_name()

df["order_day"] = df["order_time"].dt.day

df["order_day_name"] = df["order_time"].dt.day_name()


# ==========================================
# 5. CREATE DELIVERY DELAY CATEGORY
# ==========================================

def classify_delay(delay):

    if delay < 0:
        return "Early"

    elif delay == 0:
        return "On Time"

    else:
        return "Delayed"


df["delivery_status"] = df["delivery_delay"].apply(
    classify_delay
)


# ==========================================
# 6. CHECK DATA AFTER CLEANING
# ==========================================

print("\n========== CLEANED DATA ==========")

print("Rows:", df.shape[0])

print("Columns:", df.shape[1])


print("\n========== MISSING VALUES ==========")

print(df.isnull().sum())


print("\n========== DUPLICATES ==========")

print(df.duplicated().sum())


print("\n========== DELIVERY STATUS ==========")

print(df["delivery_status"].value_counts())


# ==========================================
# 7. CREATE CLEANED FOLDER
# ==========================================

os.makedirs("data/cleaned", exist_ok=True)


# ==========================================
# 8. SAVE CLEANED DATASET
# ==========================================

output_file = "data/cleaned/food_delivery_cleaned.csv"

df.to_csv(
    output_file,
    index=False
)


print("\n==========================================")
print("CLEANING COMPLETED SUCCESSFULLY")
print("==========================================")

print("Cleaned file saved at:")

print(output_file)

print("\nFinal Shape:", df.shape)
