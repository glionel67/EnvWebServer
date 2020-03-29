#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python script used to plot the content of a database using plotly library"""

import sqlite3
import sys

from datetime import datetime
from datetime import timedelta

import plotly.io as pio
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plotly.offline import plot

def plotDatabase(data):
    """Plot the content of the database using plotly and return the html code"""
    x = []
    yt = []
    yh = []
    yp = []
    for i in range(len(data)):
        x.append(data[i][0])
        yt.append(data[i][1])
        yh.append(data[i][2])
        yp.append(data[i][3])

    #fig = go.Figure(data=[go.Scatter(x=x, y=yt)])
        
    fig = make_subplots(rows=3, cols=1, shared_xaxes=True, vertical_spacing=0.02)
    fig.add_trace(go.Scatter(x=x, y=yt, name="Tem", \
                             line=dict(color='red', width=2)), row=1, col=1)
    fig.add_trace(go.Scatter(x=x, y=yh, name="Hum", \
                             line=dict(color='green', width=2)), row=2, col=1)
    fig.add_trace(go.Scatter(x=x, y=yp, name="Pre", \
                             line=dict(color='blue', width=2)), row=3, col=1)

    fig.update_yaxes(title_text="Tem [°C]", row=1, col=1)
    fig.update_yaxes(title_text="Hum [%]", row=2, col=1)
    fig.update_yaxes(title_text="Pre [Pa]", row=3, col=1)
    fig.update_layout(
        autosize=False,
        width=1360,
        height=768,
        title="Temperature/humidity/pressure",
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="#7f7f7f"
        )
    )
    #fig.show(renderer="browser")

    div = plot(fig, auto_open=False, output_type='div', \
        show_link=False, link_text="", \
        include_plotlyjs=False)

    return div, fig

if __name__ == "__main__":
    # Open database file
    databaseFileName = 'envData.db'
    if len(sys.argv) > 1:
        databaseFileName = sys.argv[1]
    conn = sqlite3.connect(databaseFileName)
    cursor = conn.cursor()

    # Print database content
    #print("Database contents:\n")

    data = []
    cursor.execute("SELECT * FROM bme280")
    for row in cursor:
        line = [elem for elem in row]
        data.append(line)
        #print(line)

    # Close database file
    conn.close()

    div, fig = plotDatabase(data)
    print(div)
    fig.show(renderer="browser")