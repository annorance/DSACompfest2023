##GRAFIK
###2017
import pandas as pd
df=pd.read_excel(r'D:\PROJECTS\DSA COMPFEST\TUGAS 1\referensi\tingkat banjir-tingkat pendidikan per kecamatan, kelurahan.xlsx', sheet_name='Sheet1')

import matplotlib.pyplot as plt
fig, ax1 = plt.subplots(figsize=(12,6))
ax1.bar(df['kecamatan, kelurahan'], df['Total hari mengalami banjir'], color='lightblue')
ax1.set_yticklabels(['{:,}'.format(int(x)) for x in ax1.get_yticks().tolist()])
ax2 = ax1.twinx()
ax2.plot(df['kecamatan, kelurahan'], df['tingkat pendidikan'])
ax1.set_title('Tingkat Pendidikan vs Tingkat Banjir per [Kecamatan, Kelurahan] 2017')
ax1.set_xlabel('[Kecamatan, Kelurahan]')
ax1.set_ylabel('Total Hari Mengalami Banjir')
ax2.set_ylabel('Tingkat Pendidikan')
#plt.savefig('Tingkat Pendidikan vs Tingkat Banjir per [Kecamatan, Kelurahan] 2017')
plt.show()


###2018
import pandas as pd
df = pd.read_excel(r'D:\PROJECTS\DSA COMPFEST\TUGAS 1\referensi\tingkat banjir-tingkat pendidikan per kecamatan, kelurahan.xlsx', sheet_name='Sheet2')

import matplotlib.pyplot as plt
fig, ax1= plt.subplots(figsize=(12,6))
ax1.bar(df['kecamatan, kelurahan'], df['Total hari mengalami banjir'], color='lightblue')
ax1.set_yticklabels(['{:,}'.format(int(x)) for x in ax1.get_yticks().tolist()])
ax2 = ax1.twinx()
ax2.plot(df['kecamatan, kelurahan'], df['tingkat pendidikan'])
ax1.set_title('Tingkat Pendidikan vs Tingkat Banjir per [Kecamatan, Kelurahan] 2018')
ax1.set_xlabel('[Kecamatan, Kelurahan]')
ax1.set_ylabel('Total Hari Mengalami Banjir')
ax2.set_ylabel('Tingkat Pendidikan')
#plt.savefig('Tingkat Pendidikan vs Tingkat Banjir per [Kecamatan, Kelurahan] 2018')
plt.show()


###2019
import pandas as pd
df = pd.read_excel(r'D:\PROJECTS\DSA COMPFEST\TUGAS 1\referensi\tingkat banjir-tingkat pendidikan per kecamatan, kelurahan.xlsx', sheet_name='Sheet3')

import matplotlib.pyplot as plt
fig, ax1= plt.subplots(figsize=(12,6))
ax1.bar(df['kecamatan, kelurahan'], df['Total hari mengalami banjir'], color='lightblue')
ax1.set_yticklabels(['{:,}'.format(int(x)) for x in ax1.get_yticks().tolist()])
ax2 = ax1.twinx()
ax2.plot(df['kecamatan, kelurahan'], df['tingkat pendidikan'])
ax1.set_title('Tingkat Pendidikan vs Tingkat Banjir per [Kecamatan, Kelurahan] 2019')
ax1.set_xlabel('[Kecamatan, Kelurahan]')
ax1.set_ylabel('Total Hari Mengalami Banjir')
ax2.set_ylabel('Tingkat Pendidikan')
#plt.savefig('Tingkat Pendidikan vs Tingkat Banjir per [Kecamatan, Kelurahan] 2019')
plt.show()


###2020
import pandas as pd
df = pd.read_excel(r'D:\PROJECTS\DSA COMPFEST\TUGAS 1\referensi\tingkat banjir-tingkat pendidikan per kecamatan, kelurahan.xlsx', sheet_name='Sheet4')

import matplotlib.pyplot as plt
fig, ax1= plt.subplots(figsize=(12,6))
ax1.bar(df['kecamatan, kelurahan'], df['Total hari mengalami banjir'], color='lightblue')
ax1.set_yticklabels(['{:,}'.format(int(x)) for x in ax1.get_yticks().tolist()])
ax2 = ax1.twinx()
ax2.plot(df['kecamatan, kelurahan'], df['tingkat pendidikan'])
ax1.set_title('Tingkat Pendidikan vs Tingkat Banjir per [Kecamatan, Kelurahan] 2020')
ax1.set_xlabel('[Kecamatan, Kelurahan]')
ax1.set_ylabel('Total Hari Mengalami Banjir')
ax2.set_ylabel('Tingkat Pendidikan')
#plt.savefig('Tingkat Pendidikan vs Tingkat Banjir per [Kecamatan, Kelurahan] 2020')
plt.show()



##ANALISIS MENDALAM --> hanya 2017 sebagai contoh
###1. Loading the Data
df = pd.read_excel(r'D:\PROJECTS\DSA COMPFEST\TUGAS 1\referensi\tingkat banjir-tingkat pendidikan per kecamatan, kelurahan.xlsx',
                   sheet_name='Sheet1')


###2. Understanding the Dataset
df.info() ####--> tipe data "object" masih "object"


###3. Data Preprocessing
####Convert Object Types to Category Types
df['kecamatan, kelurahan'] = df['kecamatan, kelurahan'].astype('category') ####--> tipe data "object" menjadi "category"
df.info()


###4. Data Visualization
import pandas as pd
df=pd.read_excel(r'D:\PROJECTS\DSA COMPFEST\TUGAS 1\referensi\tingkat banjir-tingkat pendidikan per kecamatan, kelurahan.xlsx', sheet_name='Sheet1')

import matplotlib.pyplot as plt
fig, ax1 = plt.subplots(figsize=(12,6))
ax1.bar(df['kecamatan, kelurahan'], df['Total hari mengalami banjir'], color='lightblue')
ax1.set_yticklabels(['{:,}'.format(int(x)) for x in ax1.get_yticks().tolist()])
ax2 = ax1.twinx()
ax2.plot(df['kecamatan, kelurahan'], df['tingkat pendidikan'])
ax1.set_title('Tingkat Pendidikan vs Tingkat Banjir per [Kecamatan, Kelurahan] 2017')
ax1.set_xlabel('[Kecamatan, Kelurahan]')
ax1.set_ylabel('Total Hari Mengalami Banjir')
ax2.set_ylabel('Tingkat Pendidikan')
plt.show()

####One-Hot Encoding
df = pd.get_dummies(df)

###5. Building a Regression Model
####Menentukan Variabel Input/Feature (var. Independen [x]) dan Variabel Output/Target (Var. Dependen[y])
y = df["Total hari mengalami banjir"]
x = df.drop("Total hari mengalami banjir", axis=1)

####Bagi Dataset Menjadi Data Training dan Data Testing
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(
    x,y,
    train_size = 0.8, ####--> 80% training dan 20% testing
    random_state = 1)

####Build Model Menggunakan Data Training
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(x_train,y_train)

###6. Model Evaluation
####Menggunakan Mean Squared Error (MSE) ####--> semakin kecil nilainya, semakin dekat nilai-nilainya dengan rata-rata dan semakin bagus modelnya. berlaku sebaliknya
y_pred=lr.predict(x_test)
from sklearn.metrics import mean_squared_error

import math
c = math.sqrt(mean_squared_error(y_test, y_pred))
print(c)


###7. Model Prediction
data_new = x_train[:1] ####--> first row of the training data

d = lr.predict(data_new)
print(d)

e = y_train[:1]
print(e)