import pandas as pd
import sqlite3
import os
from GPT_utils_SQL import get_summary

# Configuration
csv_file = "sample_data.csv"  # Change filename if needed
output_folder = "outputs"
os.makedirs(output_folder, exist_ok=True)

# Load Data
try:
    df = pd.read_csv(csv_file)
except FileNotFoundError:
    print(f"❌ File '{csv_file}' not found.")
    exit()

print("✅ CSV Loaded:\n", df.head())

# SQLite In-Memory Database
conn = sqlite3.connect(":memory:")
df.to_sql("SalesData", conn, index=False, if_exists="replace")
print("\n✅ Data Loaded into SQL Table 'SalesData'\n")

# Predefined Queries
quick_queries = {
    "1": "SELECT * FROM SalesData;",
    "2": "SELECT City, SUM(Sales) AS TotalSales FROM SalesData GROUP BY City;",
    "3": "SELECT Name, Sales FROM SalesData WHERE Sales > 7000;"
}

# Menu Loop
while True:
    print("\n📊 Choose an option:\n")
    print("1  Show full table")
    print("2  Sales by city summary")
    print("3  Show high sales (>7000)")
    print("4  Custom SQL query")
    print("5  Exit")

    choice = input("Enter option number: ").strip()

    if choice == "5":
        print("👋 Goodbye!")
        break

    # Determine Query
    if choice in quick_queries:
        query = quick_queries[choice]
        print(f"\n▶ Running:\n{query}\n")
    elif choice == "4":
        query = input("Enter your custom SQL query:\n")
    else:
        print("⚠️ Invalid choice. Please try again.")
        continue

    # Execute Query
    try:
        result = pd.read_sql_query(query, conn)
        print("\n📊 Result:\n", result)

        # AI Summary
        data_text = result.to_string(index=False)
        summary = get_summary(data_text)
        print("\n🤖 AI Summary:\n", summary)

        # Save Output
        result_file = os.path.join(output_folder, f"result_{choice}.csv")
        result.to_csv(result_file, index=False)
        print(f"✅ Result saved to {result_file}")

    except Exception as e:
        print(f"⚠️ SQL Error: {e}")

print(df.head())

# SQLite Database in memory
conn = sqlite3.connect(":memory:")
df.to_sql("SalesData", conn, index=False, if_exists="replace")

print("\n✅ Data Loaded into SQL Table 'SalesData'\n")

# Quick Queries Menu
quick_queries = {
    "1": "SELECT * FROM SalesData;",
    "2": "SELECT City, SUM(Sales) as TotalSales FROM SalesData GROUP BY City;",
    "3": "SELECT Name, Sales FROM SalesData WHERE Sales > 7000;",
}

# Ensure output folder exists
os.makedirs("Outputs", exist_ok=True)

# Interactive Menu Loop
while True:
    print("\n📊 Choose an option:\n")
    print("1  Show full table")
    print("2  Sales by city summary")
    print("3  Show high sales (>7000)")
    print("4  Custom SQL query")
    print("5  Exit")

    choice = input("Enter option number: ")

    if choice == "5":
        print("👋 Goodbye!")
        break

    if choice in quick_queries:
        query = quick_queries[choice]
        print(f"\n▶ Running:\n{query}\n")
    elif choice == "4":
        query = input("Enter your custom SQL query:\n")
    else:
        print("⚠️ Invalid choice. Please try again.")
        continue

    try:
        result = pd.read_sql_query(query, conn)
        print("\n📊 Result:\n", result)
        data_text = result.to_string(index=False)
        summary = get_summary(data_text)
        print("\n AI summary:\n", summary)

        # Save results
        result_file = f"outputs/result_{choice}.csv"
        result.to_csv(result_file, index=False)
        print(f"✅ Result saved to {result_file}")

    except Exception as e:
        print("⚠️ SQL Error:", e)
