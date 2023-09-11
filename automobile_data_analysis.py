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
print(res_df)

x = df2["Combined FE"]
y = df2["Combined CO2"]

coef_2 = np.polyfit(x, y, 2)
#df2.plot(x="Combined FE", y="Combined CO2",style ='x')
plt.scatter(x, y, label='Data')
plt.plot(x, np.poly1d(coef_2)(x), color='red', label='Trend line')
plt.legend()
plt.show()