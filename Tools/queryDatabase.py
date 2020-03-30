#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python script used to query the content of a database"""

import sys
import sqlite3

from datetime import datetime
from datetime import timedelta

def queryDatabase(databaseFileName, request="lastDay"):
    """Query the content of a database"""

    # Create database query
    query = ""

    # Get current datetime
    currentDatetime = datetime.now()
    #print("currentDatetime={}".format(currentDatetime))

    if request == "lastDay":
        yeasterday = currentDatetime - timedelta(days=1)
        yeasterday = yeasterday.date()
        #print("yeasterday={}".format(yeasterday))
        query = "SELECT * FROM bme280 WHERE (date >= '{}')".format(yeasterday)
    elif request == "lastWeek":
        lastWeek = currentDatetime - timedelta(days=7)
        lastWeek = lastWeek.date()
        #print("lastWeek={}".format(lastWeek))
        query = "SELECT * FROM bme280 WHERE (date >= '{}')".format(lastWeek)
    elif request == "lastMonth":
        lastMonth = currentDatetime - timedelta(days=31)
        lastMonth = lastMonth.date()
        #print("lastMonth={}".format(lastMonth))
        query = "SELECT * FROM bme280 WHERE (date >= '{}')".format(lastMonth)
    elif request == "lastYear":
        lastYear = currentDatetime - timedelta(days=365)
        lastYear = lastYear.date()
        #print("lastYear={}".format(lastYear))
        query = "SELECT * FROM bme280 WHERE (date >= '{}')".format(lastYear)
    elif request == "all":
        query = "SELECT * FROM bme280"
    elif request == "lastEntry":
        query = "SELECT * FROM bme280 ORDER BY date DESC LIMIT 1"
    else:
        print("Invalid request, options are: lastDay, lastWeek, lastMonth, lastYear.")
        return []
    #print("query={}".format(query))

    # Open database file
    conn = None
    try:
        conn = sqlite3.connect(databaseFileName)
    except:
        print("Failed to open database from file: {}".format(databaseFileName))
        return []
    cursor = conn.cursor()

    data = []
    cursor.execute(query)
    for row in cursor:
        line = [elem for elem in row]
        data.append(line)
        #print(line)

    # Close database file
    conn.close()

    return data

if __name__ == "__main__":
    databaseFileName = "envData.db"
    if len(sys.argv) > 1:
        databaseFileName = sys.argv[1]
    #print("databaseFileName={}".format(databaseFileName))
    # Options: "lastDay", "lastWeek", "lastMonth", "lastYear", "all", "lastEntry"
    request = "lastEntry"
    data = queryDatabase(databaseFileName, request)
    print(data)