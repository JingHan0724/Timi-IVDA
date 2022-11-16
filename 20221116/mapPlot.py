# -*- coding: utf-8 -*-
"""map.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19p8MXrJcE4BRYb07jSo2McYAVXqxJMaV
"""

!pip install geopandas
!pip install geoplot
!pip install dash

!pip uninstall shapely
!pip install shapely --no-binary shapely

# Commented out IPython magic to ensure Python compatibility.
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import geoplot as gplt
import re
import geoplot.crs as gcrs
from shapely.geometry import Point
# %matplotlib inline

df = pd.read_csv('500_Cities_CDC.csv')
df = df[['StateAbbr','PlaceName','PlaceFIPS','Population2010','ACCESS2_AdjPrev','ARTHRITIS_AdjPrev','BINGE_AdjPrev','BPHIGH_AdjPrev','BPMED_AdjPrev','CANCER_AdjPrev','CASTHMA_AdjPrev','CHD_AdjPrev','CHECKUP_AdjPrev','CHOLSCREEN_AdjPrev','COLON_SCREEN_AdjPrev','COPD_AdjPrev','COREM_AdjPrev','COREW_AdjPrev','CSMOKING_AdjPrev','DENTAL_AdjPrev','DIABETES_AdjPrev','HIGHCHOL_AdjPrev','KIDNEY_AdjPrev','LPA_AdjPrev','MAMMOUSE_AdjPrev','MHLTH_AdjPrev','OBESITY_AdjPrev','PAPTEST_AdjPrev','PHLTH_AdjPrev','SLEEP_AdjPrev','STROKE_AdjPrev','TEETHLOST_AdjPrev','Geolocation']]
df.head()

latitude = []
longitude = []
for line in df['Geolocation']:
  m = re.findall(r'-*\d+\.\d+', line)
  latitude.append(float(m[0]))
  longitude.append(float(m[1]))
df["geometry"] = list(zip(longitude, latitude))
df["geometry"] = df["geometry"].apply(Point)
df.head()

df.head()

df_state = df[['StateAbbr','ACCESS2_AdjPrev','ARTHRITIS_AdjPrev','BINGE_AdjPrev','BPHIGH_AdjPrev','BPMED_AdjPrev','CANCER_AdjPrev','CASTHMA_AdjPrev','CHD_AdjPrev','CHECKUP_AdjPrev','CHOLSCREEN_AdjPrev','COLON_SCREEN_AdjPrev','COPD_AdjPrev','COREM_AdjPrev','COREW_AdjPrev','CSMOKING_AdjPrev','DENTAL_AdjPrev','DIABETES_AdjPrev','HIGHCHOL_AdjPrev','KIDNEY_AdjPrev','LPA_AdjPrev','MAMMOUSE_AdjPrev','MHLTH_AdjPrev','OBESITY_AdjPrev','PAPTEST_AdjPrev','PHLTH_AdjPrev','SLEEP_AdjPrev','STROKE_AdjPrev','TEETHLOST_AdjPrev']]
df_state = df_state.groupby(['StateAbbr']).sum().reset_index()
df_state

import plotly.express as px
fig = px.choropleth(df_state,
locations='StateAbbr',
color='ACCESS2_AdjPrev',
color_continuous_scale='spectral_r',
locationmode='USA-states',
labels={'ACCESS2_AdjPrev':'ACCESS2_AdjPrev'},
scope='usa')

# Add state labels
fig.add_scattergeo(
    locations=df['StateAbbr'],
    locationmode='USA-states',
    text=df['StateAbbr'],
    mode='text')

# Add map title
fig.update_layout(
    title={'text':'Health Condition by State',
           'xanchor':'center',
           'yanchor':'top',
           'x':0.5})


fig.show()
