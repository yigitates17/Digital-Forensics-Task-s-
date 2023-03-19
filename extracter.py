import sqlite3
from datetime import datetime, timedelta
from tabulate import tabulate

# Choose your database directory
cookies_location = "C:/Users/yigit/AppData/Local/Google/Chrome/User Data/Default/Network/Cookies.db"

# Creating cursor and connection to the database
connection = sqlite3.connect(cookies_location)
cursor = connection.cursor()

# Entering the necessary query and fetching
cursor.execute("SELECT name, host_key, path, creation_utc, expires_utc, source_port, value FROM Cookies")
data = cursor.fetchall()

# To clean the data, some adjustments
converted_data = []
headers = ["name", "host_key", "path", "creation_time", "expiration_time", "source_port", "value"]

for row in data:

    # From microseconds to readable dates
    creation_utc = datetime(1601, 1, 1) + timedelta(microseconds=row[3])
    expires_utc = datetime(1601, 1, 1) + timedelta(microseconds=row[4])
    creation_str = creation_utc.strftime('%d-%m-%Y')
    expires_str = expires_utc.strftime('%d-%m-%Y')

    # Adding the readable dates and character limits for clarity.
    converted_row = (row[0][:30], row[1][:30], row[2][:30], creation_str, expires_str, row[5], row[6])
    converted_data.append(converted_row)

# Printing the result
print(tabulate(converted_data, headers=headers))

# Closing the connection
connection.close()
