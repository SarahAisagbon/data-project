import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


car_df =  pd.read_csv('Dataset.csv')

"""
#1. The number of car models in each year
df = car_df.groupby(['Model Year'])['Division'].nunique().plot()
plt.xlabel("Year")
plt.ylabel("# Car Models")
plt.title("Number of Car Models per year")
plt.show()
"""

"""
#2. Combined CO2 over time for each Car Manafucter
yearan = car_df.groupby(['Model Year', 'Mfr Name'])['Combined CO2'].mean().unstack('Mfr Name').plot()
plt.xlabel("Year")
plt.ylabel("Combined CO2")
plt.title("CO2 per Car Manufacturer")
plt.show()
"""

"""
#3. Find the quantity of car models for Aston Martin each year.
astondf = car_df[car_df['Mfr Name'] == 'Aston Martin']
astondf.groupby(['Model Year'])['Carline'].nunique().plot()
plt.show()
"""

"""
#5. Find the quantity of car models for BMW each year.
bmwdf = car_df[car_df['Mfr Name'] == 'BMW']
bmwdf.groupby(['Model Year'])['Carline'].nunique().plot()
plt.show()
"""

"""
#6. Find the quantity of car models for Audi each year.
audidf = car_df[car_df['Division'] == 'Audi']
audidf.groupby(['Model Year'])['Carline'].nunique().plot()
plt.show()
"""

"""
#7. Find the quantity of car models for Lamborghini each year.
lamdf = car_df[car_df['Division'] == 'Lamborghini']
lamdf.groupby(['Model Year'])['Carline'].nunique().plot()
plt.show()
"""

"""
#8. Find the car models with the best and worst FE ratings each year.
years = car_df['Model Year'].unique()
best_FE = {}
worst_FE = {}
for year in years:
    yeardf = car_df[car_df['Model Year'] == year]
    topFE = yeardf['Combined FE'].max()
    lowFE = yeardf['Combined FE'].min()
    topname=yeardf[yeardf['Combined FE'] == topFE]['Division'].values[0]
    lowname=yeardf[yeardf['Combined FE'] == lowFE]['Division'].values[0]
    best_FE[year] = {"Manufacturer": topname, "Best FE rating": topFE}
    worst_FE[year] = {"Manufacturer": lowname, "Worst FE rating": lowFE}
"""