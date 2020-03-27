#!/usr/bin/env python3
"""Python script used to collect measurement data from the BME280 sensor"""

import sys
import time

import sqlite3 as sq

import numpy as np

# Check if we are using a Raspberry Pi
try:
    import board
    import busio
    import digitalio
    import adafruit_bme280
except:
    pass

def getDataBme280(databaseFileName):
    """Get the data from the sensors and update the database"""

    ### Init BME280 ###
    i2c = busio.I2C(board.SCL, board.SDA)
    bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
    bme280.sea_level_pressure = 1013.25
    bme280.mode = adafruit_bme280.MODE_NORMAL
    bme280.standby_period = adafruit_bme280.STANDBY_TC_500
    bme280.iir_filter = adafruit_bme280.IIR_FILTER_DISABLE
    bme280.overscan_pressure = adafruit_bme280.OVERSCAN_X16
    bme280.overscan_humidity = adafruit_bme280.OVERSCAN_X1
    bme280.overscan_temperature = adafruit_bme280.OVERSCAN_X1

    ### Get sensors data and save into database ###
    nSamples = 5

    # Get sensors data
    samples = np.zeros((3, nSamples))
    #nSuccess = 0
    for i in range(nSamples):
        samples[0,i] = bme280.temperature
        samples[1,i] = bme280.humidity
        samples[2,i] = bme280.pressure
        #print("BME280: {}".format(samples[:3,i].T))
        time.sleep(1)

    samples.sort(axis=1)
    med = np.median(samples, axis=1)
    #print("med={}".format(med.T))
    temp, hum, pres = med[0], med[1], med[2]
    #print("BME280: T={} C, H={} %, P={} Pa".format(temp, hum, pres))

    return temp, hum, pres

if __name__ == "__main__":
    databaseFileName = "envData.db"
    temp, hum, pres = getDataBme280(databaseFileName)
    s = "T = {} °C, H = {} %, P = {} Pa".format(temp, hum, pres)
    print(s)