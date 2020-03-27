#!/usr/bin/env python3
"""Python script used to collect data from environmental sensors and store them in a database"""

import sys
import time

import sqlite3 as sq

import numpy as np

# Adafruit
import board
import busio
import digitalio
import adafruit_ccs811
import adafruit_bme280
import adafruit_dht

####################
### Init sensors ###
####################

### Init BME280 ###
i2c = busio.I2C(board.SCL, board.SDA)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
#spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
#bme_cs = digitalio.DigitalInOut(board.D10)
#bme280 = adafruit_bme280.Adafruit_BME280_SPI(spi, bme_cs)
bme280.sea_level_pressure = 1013.25
bme280.mode = adafruit_bme280.MODE_NORMAL
bme280.standby_period = adafruit_bme280.STANDBY_TC_500
bme280.iir_filter = adafruit_bme280.IIR_FILTER_DISABLE
bme280.overscan_pressure = adafruit_bme280.OVERSCAN_X16
bme280.overscan_humidity = adafruit_bme280.OVERSCAN_X1
bme280.overscan_temperature = adafruit_bme280.OVERSCAN_X1

### Init CCS811 ###
#i2c = busio.I2C(board.SCL, board.SDA)
#ccs811 = adafruit_ccs811.CCS811(i2c)
# Wait for the sensor to be ready and calibrate the thermistor
#while not ccs811.data_ready:
#    pass
#temp = ccs811.temperature
#ccs811.temp_offset = temp - 25.0

### Init DHT22 ###
#dhtDevice = adafruit_dht.DHT22(board.D23)

### Init database ###
database = "envData.db"
tableBme280 = "bme280"
tableCcs811 = "ccs811"
tableDht22 = "dht22"

### Get sensors data and save into database
nSamples = 5
while True:
    # Get sensors data
    samples = np.zeros((5, nSamples))
    nSuccess = 0
    for i in range(nSamples):
        samples[0,i] = bme280.temperature
        samples[1,i] = bme280.humidity
        samples[2,i] = bme280.pressure

        #try:
        #    samples[3,i] = dhtDevice.temperature
        #    samples[4,i] = dhtDevice.humidity
        #    nSuccess += 1
        #except:
        #    samples[3,i] = 0.0
        #    samples[4,i] = 0.0

        #print("BME280: {}".format(samples[:3,i].T))
        #print("DHT22: {}".format(samples[3:].T))

        time.sleep(1)

    samples.sort(axis=1)
    med = np.median(samples, axis=1)
    #print("med={}".format(med.T))
    temp, hum, pres = med[0], med[1], med[2]
    #print("BME280: T={} C, H={} %, P={} Pa".format(temp, hum, pres))

    #tempDht, humDht = med[3], med[4]
    #print("DHT22: T={}, H={} %".format(tempDht, humDht))

    #eco2, tvoc, temp2 = ccs811.eco2, ccs811.tvoc, ccs811.temperature
    #print("CCS811: CO2: {} PPM, TVOC: {} PPM, Temp: {} C".format(\
    #  ccs811.eco2, ccs811.tvoc, ccs811.temperature))

    # Open database
    #print("Writing to database...")
    conn = sq.connect(database)

    with conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO bme280 VALUES(datetime('now'), (?), (?), (?))", (temp, hum, pres))
        #cursor.execute("INSERT INTO ccs811 VALUES(datetime('now'), (?), (?), (?))", (eco2, tvoc, temp2))
        #if nSuccess >= 3:
        #    cursor.execute("INSERT INTO dht22 VALUES(datetime('now'), (?), (?))", (tempDht, humDht))
        conn.commit()
        cursor.close()

    conn.close()
    #print("... done!")

    time.sleep(1200) # 60s * 20 = 1200s = 20 min