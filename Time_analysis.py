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
#3. Find the quantity of car models for Aston Martin each year.
astondf = car_df[car_df['Mfr Name'] == 'Aston Martin']
astondf.groupby(['Model Year'])['Carline'].nunique().plot()
plt.show()
"""

"""
#4. Find the car manufacturer, which contains most quantity of car models.
"""
car_df.groupby(['Model Year', 'Mfr Name'])['Carline'].nunique().plot()
plt.show()

