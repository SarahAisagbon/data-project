import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


car_df =  pd.read_csv('Dataset.csv')

"""
#1. The number of car models in each year
df = car_df.groupby(['Model Year'])['Division'].nunique().plot()
plt.show()
"""

"""
#2. Combined CO2 over time for each Car Manafucter
yearan = car_df.groupby(['Model Year', 'Mfr Name'])['Combined CO2'].mean().unstack('Mfr Name').plot()
plt.show()
"""

"""
#3. Find the car manufacturer, which contains most quantity of car models.
astondf = car_df[car_df['Mfr Name'] == 'Aston Martin']
astondf.groupby(['Model Year'])['Carline'].nunique().plot()
plt.show()
"""

fiftdf = car_df[car_df['Model Year'] == '2015']
print(fiftdf.head())
#fiftdf.groupby('Mfr Name')['Carline'].nunique().plot(kind ='bar')
twendf = car_df[car_df['Model Year'] == '2024']
#twendf.groupby('Mfr Name')['Carline'].nunique().plot(kind ='bar')
print(twendf.head())

