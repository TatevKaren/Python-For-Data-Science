import pandas as pd
import sqlite3

# Loading CSV file with header
data_csv = pd.read_csv("percent_bachelors_degrees_women_usa.csv")
print(data_csv)

# Loading TXT file with header and seperator comma
data_txt = pd.read_csv("StudentSchools.txt", header = 0, sep = ',')
print(data_txt)

# Loading Excel file and specifally spreadsheet with name "Sheet1"
data_excel = pd.read_excel("file_name.xlsx", sheet_name = "Sheet1")

# Loading JSON
data_json = pd.read_json("file_name.json")
# Loading SQL Table with table name "table_name"
## making connection with SQL database named database_name.db
connection_db = sqlite3.connect("database_name.db")
## 1st query to select 1 feature with name col_1 from table with "table_name"
query_1 = 'SELECT col_1 FROM table_name'
## 2nd query to select all features with from table with "table_name"
query_2 = 'SELECT * FROM table_name'
## loading a table with query_2 from SQL database
data_sql = pd.read_sql(query_2, connection_db)
