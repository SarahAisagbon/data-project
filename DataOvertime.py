import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

car_df =  pd.read_csv('Dataset.csv')

#1. The number of car models in each year
df = car_df.groupby(['Model Year'])['Division'].nunique().plot()
plt.xlabel("Year")
plt.ylabel("# Car Models")
plt.title("Number of Car Models per year")
plt.show()

carlbs = ['Subaru', 'Fca Us Llc', 'Pagani Automobili S', 'Roush',
 'Quantum Fuel System', 'Mobility Ventures L', 
 'Koenigsegg', 'Ruf', 'Subaru Tecnica Inte']

#2a. Find the quantity of car models for Aston Martin each year.
astondf = car_df[car_df['Mfr Name'] == 'Aston Martin']
astondf.groupby(['Model Year'])['Carline'].nunique().plot()

#2b. Find the quantity of car models for BMW each year.
bmwdf = car_df[car_df['Mfr Name'] == 'BMW']
bmwdf.groupby(['Model Year'])['Carline'].nunique().plot()

#2c. Find the quantity of car models for Audi each year.
audidf = car_df[car_df['Division'] == 'Audi']
audidf.groupby(['Model Year'])['Carline'].nunique().plot()

#2d. Find the quantity of car models for Lamborghini each year.
lamdf = car_df[car_df['Division'] == 'Lamborghini']
lamdf.groupby(['Model Year'])['Carline'].nunique().plot()

#2e. Find the quantity of car models for Acura each year.
lamdf = car_df[car_df['Division'] == 'Acura']
lamdf.groupby(['Model Year'])['Carline'].nunique().plot()
plt.xlabel("Year")
plt.ylabel("# Car Models")
plt.title("Quantity of Models each year")
plt.legend(['Aston Martin', 'BMW', 'Audi', 'Lamborghini', 'Acura'])
plt.show()


#3a. Find the FE rating for Bugatti each year.
lamdf = car_df[car_df['Division'] == 'Bugatti']
lamdf.groupby(['Model Year'])['Carline'].nunique().plot()

#3b. Find the FE rating for Hyundai Motor Company each year.
lamdf = car_df[car_df['Division'] == 'Hyundai Motor Company']
lamdf.groupby(['Model Year'])['Carline'].nunique().plot()

#3c. Find the FE rating for Mercedes-Benz each year.
lamdf = car_df[car_df['Division'] == 'Mercedes-Benz']
lamdf.groupby(['Model Year'])['Carline'].nunique().plot()

#3d. Find the FE rating for Toyota each year.
lamdf = car_df[car_df['Division'] == 'Toyota']
lamdf.groupby(['Model Year'])['Carline'].nunique().plot()

#3e. Find the FE rating for Ferrari North America, Inc. each year.
lamdf = car_df[car_df['Division'] == 'Ferrari North America, Inc.']
lamdf.groupby(['Model Year'])['Carline'].nunique().plot()
plt.xlabel("Year")
plt.ylabel("Average FE Rating")
plt.title("FE rating each year")
plt.legend(['Bugatti', 'Hyundai Motor Company', 'Mercedes-Benz', 'Toyota', 'Ferrari North America, Inc.'])
plt.show()

#4. Find the car models with the best and worst FE ratings each year.
years = car_df['Model Year'].unique()
best_FE = {}
for year in years:
    yeardf = car_df[car_df['Model Year'] == year]
    topFE = yeardf['Combined FE'].max()
    lowFE = yeardf['Combined FE'].min()
    topname=yeardf[yeardf['Combined FE'] == topFE]['Division'].values[0]
    lowname=yeardf[yeardf['Combined FE'] == lowFE]['Division'].values[0]
    best_FE[year] = {"Best FE": (topname, topFE), "Worst FE": (lowname, lowFE)}
print(best_FE)


"""
#2. Combined CO2 over time for each Car Manafucter
yearan = car_df.groupby(['Model Year', 'Mfr Name'])['Combined CO2'].mean().unstack('Mfr Name').plot()
number_of_plots=32
colormap = plt.cm.nipy_spectral #I suggest to use nipy_spectral, Set1,Paired
yearan.set_color_cycle([colormap(i) for i in np.linspace(0, 1,number_of_plots)])
plt.xlabel("Year")
plt.ylabel("Combined CO2")
plt.title("CO2 per Car Manufacturer")
plt.show()
"""