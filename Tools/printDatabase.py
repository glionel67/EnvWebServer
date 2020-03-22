#!/usr/bin/env python3
"""Python script used to print the content of a database"""

import sqlite3
import sys

# Open database file
conn = sqlite3.connect('envData.db')
cursor = conn.cursor()

# Print database content
print("\tDatabase contents")

print("- BME280:")
for row in cursor.execute("SELECT * FROM bme280"):
    print (row)

print("- DHT22:")
for row in cursor.execute("SELECT * FROM dht22"):
    print(row)

# Close database file
conn.close()
