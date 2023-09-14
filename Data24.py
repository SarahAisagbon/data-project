import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

car_df =  pd.read_csv('2024 - Dataset.csv')

#1. Find the car manufacturer, which contains most quantity of car models.
car_df.groupby('Mfr Name')['Carline'].nunique().plot(kind ='bar')
plt.title("The quantity of car models for each car manufacturer")
plt.ylabel("Car Manufacturer")
plt.ylabel("# Car Models")
plt.show()

#2. Find the top average fuel economy for the city and highway driving from the given data set.
df2 = car_df.copy()
df2['average FE'] = df2[['City FE', 'Highway FE']].mean(axis=1)
max =df2['average FE'].max()
df2['fullline'] = df2['Division'] + ' ' + df2['Carline'].str.title()
name = df2['fullline'][df2['average FE'] == max].values[0]
topFEdict = {'2024': {'Car Model': name, 'Average Fuel Economy': max}}
print(topFEdict)

#3. Find good and bad average fuel economy cars from all transmission types.
df2['Transmission Description'] = df2['Transmission Description'].str.split('(', expand=True)[0]
df2.boxplot(column=['average FE'], by =['Transmission Description'], rot= 90, fontsize=6)
plt.show()

#4. Find car manufacturers, which have 4WD (4-wheel drive) and 2WD (2-wheel drive) with engine power is more than 3.5.
res_df = df2[(df2["Drive Desc"] == '2-Wheel Drive, Rear') | (df2["Drive Desc"] == '2-Wheel Drive, Front') | (df2["Drive Desc"] == '4-Wheel Drive') & (df2['Engine Displacement'] > 3.5)]
grouped =res_df.groupby('Mfr Name')
grouped['Carline'].nunique().plot(kind ='bar')
plt.title("4-wheel drive and 2-wheel drive cars with engine power more than 3.5 (2015)")
plt.xlabel("Manufacturers")
plt.ylabel("# Car Models")
plt.show()

#5. Is there a relationship between Combined FE and Combined CO2
"""
x = df2["Combined FE"]
y = df2["Combined CO2"]

plt.scatter(x, y, label='Data')
plt.title("Relationship between Combined FE and Combined CO2 (2024)")
plt.xlabel("Combined FE")
plt.ylabel("Combined CO2")

coef = np.polyfit(x, y, 3)
p = np.poly1d(coef)

sorted = np.sort(x)
plt.plot(sorted, p(sorted), color='red', label='Trend line')
plt.legend()
plt.show()
"""

"""
#6. How much CO2 on average is emitted for each car type?
dfCO2 = car_df.groupby('Carline Class Desc')['Combined CO2'].mean()
dfCO2.plot(kind='bar')
plt.xlabel("Car Type")
plt.ylabel("CO2 Emission")
plt.title("CO2 Emission per Car Type (2015)")
plt.show()
"""

"""
#7.How much CO2 on average is emitted for each car manufacturer?
dfCO2 = car_df.groupby('Mfr Name')['Combined CO2'].mean().plot(kind='bar')
plt.xlabel("Car Manufacturer")
plt.ylabel("CO2 Emission")
plt.title("CO2 Emission per Car Manufacturer (2015)")
plt.show()
"""

"""
#8. What's the average rating for each car manufacturer?
dfCO2 = car_df.groupby('Mfr Name')['Combined FE'].mean().plot(kind='bar')
plt.xlabel("Car Manufacturer")
plt.ylabel("Average FE Rating")
plt.title("Average FE Rating for each Car Manufacturer (2015)")
plt.show()
"""

#9. How much CO2 is emitted for each aston martin carline?
"""
astondf = car_df[car_df['Mfr Name'] == 'Aston Martin']
astondf["Mfr Name"] = astondf["Mfr Name"].str.title()
astondf['FullCarline'] = astondf['Mfr Name'] + ' ' + astondf['Carline'] + ' ' + astondf['Transmission']
astondf.groupby(['FullCarline']).sum().plot(kind='pie', y='Combined CO2', autopct="%1.0f%%", title = 'Total Combined CO2 for each Aston Martin Type')
plt.show()
"""

#10. How much CO2 is emitted for each MAZDA carline?
"""
mzdf = car_df[car_df['Mfr Name'] == 'MAZDA']
mzdf["Mfr Name"]= mzdf["Mfr Name"].str.title()
mzdf['FullCarline'] = mzdf['Mfr Name'] + ' ' + mzdf['Carline'] + ' ' + mzdf['Transmission']
mzdf.groupby(['FullCarline']).sum().plot(kind='pie', y='Combined CO2', autopct="%1.0f%%", title = 'Total Combined CO2 for each Mazda Type')
plt.show()
"""

#11. How much CO2 is emitted for each Mitsubishi Motors Co carline?
"""
mmcdf = car_df[car_df['Mfr Name'] == 'Mitsubishi Motors Co']
mmcdf["Mfr Name"]= mmcdf["Mfr Name"].str.title()
mmcdf['FullCarline'] = mmcdf['Mfr Name'] + ' ' + mmcdf['Carline'] + ' ' + mmcdf['Transmission']
mmcdf.groupby(['FullCarline']).sum().plot(kind='pie', y='Combined CO2', autopct="%1.0f%%", title = 'Total Combined CO2 for each Mitsubishi Motors Co Type')
plt.show()
"""

#12. Is there a relationship between Engine Power and FE rating
"""
x = df2["Engine Displacement"]
y = df2["Combined FE"]

plt.scatter(x, y, label='Data')
plt.xlabel("Engine Power")
plt.ylabel("Combined FE")

coef = np.polyfit(x, y, 1)
p = np.poly1d(coef)

sorted = np.sort(x)
plt.plot(sorted, p(sorted), color='red', label='Trend line')
plt.legend()
plt.show()
"""

#13. Is there a relationship between # Cylinders and FE rating
"""
x = df2["# Cylinders"]
y = df2["Combined FE"]

plt.scatter(x, y, label='Data')
plt.xlabel("# Cylinders")
plt.ylabel("Combined FE")

coef = np.polyfit(x, y, 1)
p = np.poly1d(coef)

sorted = np.sort(x)
plt.plot(sorted, p(sorted), color='red', label='Trend line')
plt.legend()
plt.show()
"""

#14. Is there a relationship between Engine Power and # Gears
"""
x = df2["Engine Displacement"]
y = df2["# Cylinders"]

plt.scatter(x, y, label='Data')
plt.xlabel("Engine Displacement")
plt.ylabel("# Cylinders")

coef = np.polyfit(x, y, 1)
p = np.poly1d(coef)

sorted = np.sort(x)
plt.plot(sorted, p(sorted), color='red', label='Trend line')
plt.legend()
plt.show()
"""

#15. Is there a relationship between Engine Power and # Gears
"""
x = df2["Engine Displacement"]
y = df2["# Gears"]

plt.scatter(x, y, label='Data')
plt.xlabel("Engine Displacement")
plt.ylabel("# Gears")

coef = np.polyfit(x, y, 1)
p = np.poly1d(coef)

sorted = np.sort(x)
plt.plot(sorted, p(sorted), color='red', label='Trend line')
plt.legend()
plt.show()
"""
