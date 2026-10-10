import pandas as pd
import sqlite3


def excel_to_sqlite(excel_file, sqlite_file, table_name):
    # Read Excel file into pandas DataFrame
    df = pd.read_excel(excel_file)

    # Connect to SQLite database
    conn = sqlite3.connect(sqlite_file)

    # Write DataFrame to SQLite database
    df.to_sql(table_name, conn, index=False, if_exists='replace')
    print(df)

    # Close database connection
    conn.commit()

# Specify the paths and names
excel_file = 'Cars.xlsx'
sqlite_file = 'searchbotf23.db'
table_name = 'animesearchbot'

# Convert Excel to SQLite
excel_to_sqlite(excel_file, sqlite_file, table_name) #there is only one problem connected with how data is saved(instead of ' ' put '_'

print("Conversion complete!")
