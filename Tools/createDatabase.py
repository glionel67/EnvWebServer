#!/usr/bin/env python3
"""Python script used to create a new database for storing environmental data"""

import sqlite3 as sq
import sys

conn = sq.connect('envData.db')
with conn:
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS bme280")
    cursor.execute("CREATE TABLE bme280 (date DATETIME, temperature FLOAT, humidity FLOAT, pressure FLOAT)")

    #cursor.execute("DROP TABLE IF EXISTS ccs811")
    #cursor.execute("CREATE TABLE ccs811 (date DATETIME, eco2 FLOAT, tvoc FLOAT, temperature FLOAT)")

    #cursor.execute("DROP TABLE IF EXISTS dht22")
    #cursor.execute("CREATE TABLE dht22 (date DATETIME, temperature FLOAT, humidity FLOAT)")
conn.close()