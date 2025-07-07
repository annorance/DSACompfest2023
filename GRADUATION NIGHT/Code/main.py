#import important libraries
import pandas as pd
import matplotlib.pyplot as plt

#import data
data = pd.read_csv('raw_air_pollution_data_2023.csv')
data.head()

#remove duplicates and unwanted observations
data = data.drop_duplicates(ignore_index = True)
data = data.drop(['um100', 'pm1', 'um010', 'pm10', 'um003', 'um050', 'um005', 'pressure',
                  'locationId', 'latitude', 'longitude', 'country'], axis = 1)
data.head()

#handling missing data
data.isnull()
data = data.dropna(axis=0, how="any", subset=None, inplace=True)
data.head()

#changing data type
##check information, shape, and data type
data.info()

#managing outliers
#apakah perlu? cek dari grafik ###--> ini rafly aja
fig, ax = plt.subplots(figsize = (12,6))
ax.plot(data['location'], data['pm25'])
ax.set_xlabel('lokasi')
ax.set_ylabel('partikel pm2.5 (mikrogram/m^3')
plt.show()
