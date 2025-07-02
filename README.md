# AI-Powered SQL Query Tool for CSV Data

This Python tool loads CSV data into an in-memory SQLite database, allowing quick SQL queries along with AI-generated summaries for business-friendly insights. Ideal for analysts, business users, or anyone working with structured data.

---

## ⚡ Features
✅ Loads CSV data into SQLite automatically  
✅ Run predefined or custom SQL queries interactively  
✅ AI-generated summaries using GPT-3.5 for easy interpretation of results  
✅ Saves query outputs as CSV files for reporting  
✅ No database installation required — uses in-memory SQLite  

---

## 🛠️ Requirements
- Python 3.x  
- `pandas`, `sqlite3`, `os`  
- `GPT_utils_SQL.py` with AI integration (requires OpenAI API key)  

---

## 🚀 How to Use
1. Place your CSV file in the project folder (default: `sample_data.csv`)  
2. Ensure your OpenAI API key is configured inside `GPT_utils_SQL.py`  
3. Run the tool:  
   ```bash
   python query_tool.py
Choose from the interactive menu:

1 Show full table

2 Sales by city summary

3 High sales over 7000

4 Custom SQL query

5 Exit

The tool will:
✅ Display query results
✅ Generate AI summary of the output
✅ Save results to the outputs folder

📄 Example Output
text
Copy
Edit
📊 Result:
City    Sales
NYC     8500
LA      7800
...

🤖 AI Summary:
Total sales are concentrated in NYC and LA with high-performing sales figures exceeding $7,000.
Output file saved to:

bash
Copy
Edit
outputs/result_2.csv
🤖 AI Integration
Model: GPT-3.5-Turbo

Summarizes raw query output in plain language

Helps transform technical results into client-friendly insights

💼 Ideal Use Cases
✔ Quick SQL queries on CSV data without full database setup
✔ Analysts or finance teams needing AI-powered summaries
✔ Automating reports with clear business insights
✔ Data exploration with minimal coding