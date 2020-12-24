import os
import datetime
import subprocess

from matplotlib.pyplot import xlabel, ylabel
import pandas as pd
import numpy as np

import streamlit as st

import plotly.express as px

@st.cache
def load_data(path):
    df = pd.read_csv(path,index_col=0)
    return df

def check_csv(location):
    today = datetime.date.today()
    path = f"/work/data/{today}_{location}.csv"
    if os.path.exists(path):
        return path
    else:
        cmd = f"python /work/src/suumo_scraper.py --location {location}"
        subprocess.call(cmd.split())
        if os.path.exists(path):
            return path
        else:
            raise AttributeError("wrong location")


"""
# Kusomusi Apartment Agent
"""
locations = ["shinjuku", "shibuya"]
target_location = st.selectbox('select location', locations)
f"location: {target_location}"

path = check_csv(target_location)
df = load_data(path)
df_scatter = df.copy()

"""
## Raw Data
"""
targets = list(df.columns)
selected_targets = st.multiselect('select targets', targets, default=targets)
df = df[selected_targets]
st.dataframe(df)

"""
## Plot Scatters
"""
target_x = st.selectbox('select target x', targets)
target_y = st.selectbox('select target y', targets)


st.write(
    px.scatter(df_scatter,x=target_x, y=target_y, title='Scatters')
)


"""
## Filter by area and age
"""
area_value = st.slider('select area',min_value=0, max_value=50, step=1, value=20)
f"area: {area_value}"
age_value = st.slider('select age',min_value=1, max_value=60, step=1, value=20)
f"age: {age_value}"

screened_df = df_scatter.query(f"area > {area_value} and apartment_age < {age_value}")
st.dataframe(screened_df)

names = screened_df['apartment_name'].values
links = screened_df['URL'].values
"""
## Links
"""
for i, j in zip(names,links):
    i
    j
    "-------------------------"