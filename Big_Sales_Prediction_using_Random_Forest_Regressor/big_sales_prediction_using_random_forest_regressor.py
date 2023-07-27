# -*- coding: utf-8 -*-
"""Big Sales Prediction using Random Forest Regressor.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Rf4DYST3anlqsbouE9BJKHhOMLiUbbca

# **Big Sales Prediction using Random Forest Regressor**

# **Get Understand about Dataset**

**There are 12 variables in dataset.**

1. Item Identifier
2. Item Weight
3. Item Fat Content
4. Item Visibility
5. Item Type
6. Item MRP
7. Outlet Identifier
8. Outlet Establishment Year
10. Outlet Location Type
11. Outlet Type
12. Item Outlet Sales

# **Import Library**
"""

import pandas as pd
import numpy as np

"""# **Import CSV as Dataset**"""

df=pd.read_csv('https://github.com/YBIFoundation/Dataset/raw/main/Big%20Sales%20Data.csv')

"""# **Get the first 5 rows from Dataframe**"""

df.head()

"""# **Get Information of Dataframe**"""

df.info()

"""# **Get Summary Statistics**"""

df.describe()

import seaborn as sb
sb.pairplot(df)

"""# **Get Column Names**"""

df.columns

"""# **Get Categries and Counts of Categorical Values**"""

df[['Item_Identifier']].value_counts()

df[['Item_Fat_Content']].value_counts()

df.replace({'Item_Fat_Content':{'LF':'Low Fat','reg':'Regular','low fat':'Low Fat'}},inplace=True)

df[['Item_Fat_Content']].value_counts()

df.replace({'Item_Fat_Content':{'Low Fat':0,'Regular':1}},inplace=True)

df[['Item_Type']].value_counts()

df.replace({'Item_Type':{'Fruits and Vegetables':0,'Snack Foods':0,'Household':1,'Frozen Foods':0,
                         'Dairy':0,'Baking Goods':0,'Canned':0,'Health and Hygiene':1,'Meat':0,
                         'Soft Drinks':0,'Breads':0,'Hard Drinks':0,'Others':2,'Starchy Foods':0,
                         'Breakfast':0,'Seafood':0 }},inplace=True)

df[['Item_Type']].value_counts()

df[['Outlet_Identifier']].value_counts()

df.replace({'Outlet_Identifier':{'OUT027':0,
'OUT013':1,
'OUT035':2,
'OUT046':3,
'OUT049':4,
'OUT045':5,
'OUT018':6,
'OUT017':7,
'OUT010':8,
'OUT019':9 }},inplace=True)

df[['Outlet_Identifier']].value_counts()

df[['Outlet_Size']].value_counts()

df.replace({'Outlet_Size':{'Medium':0,'Small':1,'High':2}},inplace=True)

df[['Outlet_Size']].value_counts()

df[['Outlet_Location_Type']].value_counts()

df.replace({'Outlet_Location_Type':{'Tier 1':0,'Tier 2':1,'Tier 3':2}},inplace=True)

df[['Outlet_Location_Type']].value_counts()

df[['Outlet_Type']].value_counts()

df.replace({'Outlet_Type':{'Supermarket Type1':0,'Grocery Store':1,'Supermarket Type3':2,'Supermarket Type2':3}},inplace=True)

df[['Outlet_Type']].value_counts()

df.head()

df.info()

df.shape

"""# **Define y and x**"""

y=df['Item_Outlet_Sales']

y.shape

y

df.columns

x=df[['Item_Weight', 'Item_Fat_Content', 'Item_Visibility',
       'Item_Type', 'Item_MRP', 'Outlet_Identifier',
       'Outlet_Establishment_Year', 'Outlet_Size', 'Outlet_Location_Type',
       'Outlet_Type']]

x.shape

x

"""# **Get x Variables Stantardized**"""

from sklearn.preprocessing import StandardScaler

ss=StandardScaler()

x_std=df[['Item_Weight','Item_Visibility','Item_MRP','Outlet_Establishment_Year']]

x_std=ss.fit_transform(x_std)

x_std

x[['Item_Weight','Item_Visibility','Item_MRP','Outlet_Establishment_Year']]=pd.DataFrame(x_std,columns=[['Item_Weight','Item_Visibility','Item_MRP','Outlet_Establishment_Year']])

x

"""# **Get Train Test Split**"""

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.7,random_state=2529)

x_train.shape,x_test.shape,y_train.shape,y_test.shape

"""# **Get Model Train**"""

from sklearn.ensemble import RandomForestRegressor

rfr=RandomForestRegressor(random_state=2529)

rfr.fit(x_train,y_train)

"""# **Get Model Prediction**"""

y_pred=rfr.predict(x_test)

y_pred

"""# **Get model Evaluation**"""

from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score

mean_squared_error(y_test,y_pred)

mean_absolute_error(y_test,y_pred)

r2_score(y_test,y_pred)

"""# **Get Visualization of Actual Vs Predicted Result**"""

import matplotlib.pyplot as plt
plt.scatter(y_test,y_pred)
plt.xlabel('Actual Prices')
plt.ylabel('Predicted prices')
plt.title('Actual Vs Predicted Price')
plt.show()
