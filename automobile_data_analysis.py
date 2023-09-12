import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


car_df =  pd.read_excel('2015 - Dataset(Assessment).xls')
print(car_df.dtypes)

#1. Find the car manufacturer, which contains most quantity of car models.
#df = car_df.groupby('Mfr Name')['Carline'].nunique().plot(kind = 'bar')
#plt.show()

#2. Find the top average fuel economy for the city and highway driving from the given data set.
df2 = car_df.copy()
df2['average FE'] = df2[['City FE', 'Highway FE']].mean(axis=1)
#df2.max()

#3. Find good and bad average fuel economy cars from all transmission types.
max_trans_df = df2.groupby(['Transmission', 'Transmission Description'])['average FE'].max()
print(max_trans_df)
min_trans_df = df2.groupby(['Transmission', 'Transmission Description'])['average FE'].min()
print(min_trans_df)


#4. Find car manufacturers, which have 4WD (4-wheel drive) and 2WD (2-wheel drive) with engine power is more than 3.5.
res_df = df2[(df2["Drive Desc"] == '2-Wheel Drive, Rear') | (df2["Drive Desc"] == '2-Wheel Drive, Front') | (df2["Drive Desc"] == '4-Wheel Drive') & (df2['Engine Displacement'] > 3.5)]
print(res_df['Mfr Name'].unique())

#5. Is there a relationship between Combined FE and Combined CO2
"""
x = df2["Combined FE"]
y = df2["Combined CO2"]

plt.scatter(x, y, label='Data')
plt.xlabel("Combined FE")
plt.ylabel("Combined CO2")

coef = np.polyfit(x, y, 3)
p = np.poly1d(coef)

sorted = np.sort(x)
plt.plot(sorted, p(sorted), color='red', label='Trend line')
plt.legend()
plt.show()
"""

#6. How much CO2 on average is emitted for each car type?
#dfCO2 = car_df.groupby('Carline Class Desc')['Combined CO2'].mean()
#dfCO2.plot(kind='bar')
#plt.show()

#7.How much CO2 on average is emitted for each car manufacturer?
#dfCO2 = car_df.groupby('Mfr Name')['Combined CO2'].mean().plot(kind='bar')
#plt.show()

#8. What's the average rating for each car manufacturer?
#dfCO2 = car_df.groupby('Mfr Name')['Combined FE'].mean().plot(kind='bar')
#plt.show()

#9. How much CO2 is emitted for each aston martin carline?
"""
astondf = car_df[car_df['Mfr Name'] == 'aston martin']
astondf["Mfr Name"]= astondf["Mfr Name"].str.title()
astondf['FullCarline'] = astondf['Mfr Name'] + ' ' + astondf['Carline'] + ' ' + astondf['Transmission']
astondf.groupby(['FullCarline']).sum().plot(kind='pie', y='Combined CO2', autopct="%1.0f%%", title = 'Total Combined CO2 for each Aston Martin Type')
plt.show()
"""

#10. How much CO2 is emitted for each MAZDA carline?
"""
astondf = car_df[car_df['Mfr Name'] == 'MAZDA']
astondf["Mfr Name"]= astondf["Mfr Name"].str.title()
astondf['FullCarline'] = astondf['Mfr Name'] + ' ' + astondf['Carline'] + ' ' + astondf['Transmission']
astondf.groupby(['FullCarline']).sum().plot(kind='pie', y='Combined CO2', autopct="%1.0f%%", title = 'Total Combined CO2 for each Aston Martin Type')
plt.show()
"""


#11. How much CO2 is emitted for each Mitsubishi Motors Co carline?
"""
astondf = car_df[car_df['Mfr Name'] == 'Mitsubishi Motors Co']
astondf["Mfr Name"]= astondf["Mfr Name"].str.title()
astondf['FullCarline'] = astondf['Mfr Name'] + ' ' + astondf['Carline'] + ' ' + astondf['Transmission']
astondf.groupby(['FullCarline']).sum().plot(kind='pie', y='Combined CO2', autopct="%1.0f%%", title = 'Total Combined CO2 for each Aston Martin Type')
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

print(car_df.isnull().sum())
