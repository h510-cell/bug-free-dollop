import csv
import pandas as pd
import plotly.express as px

with open("data.csv") as f:
    df = csv.DictReader(f)
    fig = px.scatter(df, x:"date"
                       , y:"cases",Color="country")

fig.show()