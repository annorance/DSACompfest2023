#!/usr/bin/env python
# coding: utf-8

# ## import important libraries

# In[41]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import statsmodels.api as sm
import math
from scipy.stats import norm
from sklearn.model_selection import train_test_split
from sklearn.model_selection import RandomizedSearchCV
from sklearn.tree import DecisionTreeClassifier, export_graphviz
import graphviz
from sklearn.metrics import accuracy_score
from sklearn import tree
from numpy.lib.function_base import percentile
from sklearn.metrics import mean_squared_error


# ## import dataset

# In[42]:


data = pd.read_csv('ev_sum.csv')
data.head()


# ## preprocessing

# In[43]:


#drop duplicate rows
data = data.drop_duplicates(ignore_index = True)
data


# In[6]:


#data information
data.info()


# In[18]:


#missing data
data.isnull()


# ### Manage Outliers

# In[38]:


#IQR HARGA
Q1_harga = np.percentile(data['Harga(Rp)'], 25, method='midpoint')
Q3_harga = np.percentile(data['Harga(Rp)'], 75, method='midpoint')
IQR_harga = (Q3_harga - Q1_harga)
print('IQR_harga:', IQR_harga)
#IQR KAPASITAS BATERAI
Q1_baterai = np.percentile(data['Kapasitas Baterai (kWh)'], 25, method='midpoint')
Q3_baterai = np.percentile(data['Kapasitas Baterai (kWh)'], 75, method='midpoint')
IQR_baterai = (Q3_baterai - Q1_baterai)
print('IQR_baterai:', IQR_baterai)
#IQR EFISIENSI
Q1_efisiensi = np.percentile(data['Efisiensi (Wh/km)'], 25, method='midpoint')
Q3_efisiensi = np.percentile(data['Efisiensi (Wh/km)'], 75, method='midpoint')
IQR_efisiensi = Q3_efisiensi - Q1_efisiensi
print('IQR_efisiensi:', IQR_efisiensi)


# In[39]:


#Outlier atas
#UPPER HARGA
upper_harga= Q3_harga + 1.5*IQR_harga
upper_harga_array=np.array(data['Harga(Rp)']>=upper_harga)
print("Upper harga: ", upper_harga)
print("Outlier above upper bound: ", upper_harga_array.sum())
#UPPER BATERAI
upper_baterai= Q3_baterai + 1.5*IQR_baterai
upper_baterai_array=np.array(data['Kapasitas Baterai (kWh)']>=upper_baterai)
print("Upper baterai: ", upper_baterai)
print("Outlier above upper bound: ", upper_baterai_array.sum())
#UPPER EFISIENSI
upper_efisiensi= Q3_efisiensi + 1.5*IQR_efisiensi
upper_efisiensi_array=np.array(data['Efisiensi (Wh/km)']>=upper_efisiensi)
print("Upper efisiensi: ", upper_efisiensi)
print("Outlier above upper bound: ", upper_efisiensi_array.sum())

#Outlier bawah
#LOWER HARGA
lower_harga= Q1_harga - 1.5*IQR_harga
lower_harga_array=np.array(data['Harga(Rp)']<=lower_harga)
print("Lower harga: ", lower_harga)
print("Outlier below lower bound: ", lower_harga_array.sum())
#LOWER BATERAI
lower_baterai= Q1_baterai - 1.5*IQR_baterai
lower_baterai_array=np.array(data['Kapasitas Baterai (kWh)']<=lower_baterai)
print("Lower baterai: ", lower_baterai)
print("Outlier below lower bound: ", lower_baterai_array.sum())
#LOWER EFISIENSI
lower_efisiensi= Q1_efisiensi - 1.5*IQR_efisiensi
lower_efisiensi_array=np.array(data['Efisiensi (Wh/km)']<=lower_efisiensi)
print("Lower efisiensi: ", lower_efisiensi)
print("Outlier below lower bound: ", lower_efisiensi_array.sum())


# ### Boolean value indicating the outlier rows

# In[40]:


#UPPER
upper_harga_array = np.where(data['Harga(Rp)']>=upper_harga)[0]
print(upper_harga_array)
upper_baterai_array = np.where(data['Kapasitas Baterai (kWh)']>=upper_baterai)[0]
print(upper_baterai_array)
upper_efisiensi_array = np.where(data['Efisiensi (Wh/km)']>=upper_efisiensi)[0]
print(upper_efisiensi_array)
#LOWER
lower_harga_array = np.where(data['Harga(Rp)']<=lower_harga)[0]
print(lower_harga_array)
lower_baterai_array = np.where(data['Kapasitas Baterai (kWh)']<=lower_baterai)[0]
print(lower_baterai_array)
lower_efisiensi_array = np.where(data['Efisiensi (Wh/km)']<=lower_efisiensi)[0]
print(lower_efisiensi_array)


# ### REMOVE OUTLIERS 

# In[ ]:


#DICANCEL
##karena  walaupun berada di bawah batas bawah/di atas bawah atas, nilainya masih normal dan faktanya terdapat beberapa 
##mobil yang efisiensinya sedikit lebih besar


# ### Statistik Dasar

# In[7]:


df = pd.DataFrame(data)
df.head()


# In[52]:


#Data Aggregation
#DROP NON NUMERIC COLUMN
df_without_brand = df.drop(['Brand'], axis=1)

#DATA AGGREGATION
min_values = df.min()
print("NILAI MINIMUM = \n", min_values)
max_values = df.max()
print("NILAI MAKSIMUM = \n", max_values)
mean_values = df_without_brand.mean()
print("RATA-RATA = \n", mean_values)
std_values = df_without_brand.std()
print("STANDARD DEVIATION = \n", std_values)
correlation_matrix = df_without_brand.corr()
print("MATRIKS KORELASI = \n", correlation_matrix)


# In[9]:


#Model Regresi
X = sm.add_constant(df[['Kapasitas Baterai (kWh)', 'Efisiensi (Wh/km)']])
y = df['Harga(Rp)']

model = sm.OLS(y, X).fit()
print(model.summary())
## y = -1,575x10^-9 + 2.726*10^7 X1 + 4.488*10^6 X2


# In[10]:


#Harga Prediksi
predicted_values = model.predict(X)
df['Predicted_Harga'] = predicted_values
print(df)


# ### DATA NORMALIZATION

# In[ ]:


#Dicancel karena distribusi datanya sudah cukup baik


# ### EDA 

# In[63]:


#DATA VISUALIZATION
#SCATTER PLOT
##Harga vs Efisiensi
sns.scatterplot(data=data, x='Efisiensi (Wh/km)', y='Harga(Rp)')
plt.show()
##Harga vs Kapasitas Baterai
sns.scatterplot(data=data, x='Kapasitas Baterai (kWh)', y='Harga(Rp)')
plt.show()
###dari sini dapat terlihat bahwa harga tinggi didapat ketika efisiensi rendah dan kapasitas baterai tinggi

#SCATTERPLOT EFISIENSI X KAPASITAS BATERAI
sns.scatterplot(data=data, x='Efisiensi (Wh/km)', y='Kapasitas Baterai (kWh)')
plt.show()
###dari sini dapat dilihat bahwa kapasitas baterai yang tinggi diperoleh ketika efisiensi berada di sekitar 0.4-0.6

#HEATMAP
sns.set(font_scale=0.45)
print(df_without_brand.corr())
# plotting correlation heatmap
dataplot = sns.heatmap(df_without_brand.corr(), cmap="YlGnBu", annot=True)
# displaying heatmap
plt.show()
##kesimpulan: Harga lebih dipengaruhi oleh kapasitas baterainya daripada efisiensi,  kaitan antara efisiensi dan kapasitas baterai gak begitu erat (di scatter plot juga sudah tergambar)

#BOXPLOT
#boxplot kapasitas baterai
plt.boxplot(data["Kapasitas Baterai (kWh)"])
plt.show()
#boxplot efisiensi
plt.boxplot(data["Efisiensi (Wh/km)"])
plt.show() 
###di gambar tertera hanya ada 2 outliers padahal seharusnya 3. hal ini dikarenakan terdapat dua data dengan nilai efisiensi yaitu 290 sehingga gambar menjadi tumpang tindih 
#boxplot harga
plt.boxplot(data["Harga(Rp)"])
plt.show()


# ### Membuat Machine Learning 

# In[47]:


#Menambahkan Harga Maksimum
df['rekomendasi'] = df['Harga(Rp)'] <= df['Predicted_Harga']
print(df.to_string())


# In[48]:


#Separating the target variable
X = df.values[:, 1:5]
Y = df.values[:,5]
Y = Y.astype('int')

#Splitting dataset into test and train
X_train, X_test, y_train, y_test = train_test_split(X,Y,test_size = 0.2, random_state = 100)


# In[49]:


#Hyperparameter Tuning
clf_entropy.tree_.max_depth


# In[50]:


clf_entropy.score(X_train, y_train)


# In[52]:


#FIRST TRIAL
#Function to perform training with Entropy
clf_entropy = DecisionTreeClassifier(criterion = "entropy", random_state=100, max_depth=3, min_samples_leaf=5)
clf_entropy.fit(X_train, y_train)

#Function to make prediction
y_pred_en = clf_entropy.predict(X_test)
print(y_pred_en)

#Checking accuracy
print("Accuracy is ", accuracy_score(y_test,y_pred_en)*100)

#SECOND TRIAL
#Function to perform training with Entropy
clf_entropy = DecisionTreeClassifier(criterion = "entropy", random_state=100, max_depth=8, min_samples_leaf=8)
clf_entropy.fit(X_train, y_train)

#Function to make prediction
y_pred_en = clf_entropy.predict(X_test)
print(y_pred_en)

#Checking accuracy
print("Accuracy is ", accuracy_score(y_test,y_pred_en)*100)

#THIRD TRIAL
#Function to perform training with Entropy
clf_entropy = DecisionTreeClassifier(criterion = "entropy", random_state=100, max_depth=10, min_samples_leaf=10)
clf_entropy.fit(X_train, y_train)

#Function to make prediction
y_pred_en = clf_entropy.predict(X_test)
print(y_pred_en)

#Checking accuracy
print("Accuracy is ", accuracy_score(y_test,y_pred_en)*100)


# ### EVALUATION

# In[25]:


y_pred = clf_entropy.predict(X_test)
math.sqrt(mean_squared_error(y_test, y_pred))
###semakin kecil nilai MSE maka semakin baik kualitas model


# In[ ]:




