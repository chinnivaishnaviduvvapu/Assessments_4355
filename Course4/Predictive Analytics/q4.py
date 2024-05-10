# -*- coding: utf-8 -*-
"""Q4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ukNw4q3lTvzt06wJNNZv9rK7vtZl8SiI
"""

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
import time
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix,r2_score,mean_squared_error,precision_score, recall_score, f1_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt
from sklearn.metrics import silhouette_score
from numpy import loadtxt
from xgboost import XGBClassifier
from sklearn.linear_model import LogisticRegression,LinearRegression
from sklearn.svm import SVC
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
import seaborn as sn
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import silhouette_score
import seaborn as sns
from sklearn.ensemble import IsolationForest
from statsmodels.stats.outliers_influence import variance_inflation_factor

df=pd.read_csv('/content/sample_data/anomaly_train.csv')
df.head()

df.shape

df.info()

df.dtypes

df.isna().sum()

for column in df.select_dtypes(include=['float64', 'int64']).columns:
    plt.figure(figsize=(10, 5))
    sns.histplot(df[column])
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()

# Plot bar charts for categorical columns
for column in df.select_dtypes(include=['object']).columns:
    plt.figure(figsize=(10, 5))
    df[column].value_counts().plot(kind='bar')
    plt.title(f'Bar Chart of {column}')
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.show()

numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns
for i in range(len(numerical_columns)):
    for j in range(i + 1, len(numerical_columns)):
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=df, x=numerical_columns[i], y=numerical_columns[j])
        plt.title(f'Scatter Plot between {numerical_columns[i]} and {numerical_columns[j]}')
        plt.show()

df.describe()

df.duplicated().sum()

#outliers detection
for column in df.select_dtypes(include=['float64', 'int64']).columns:
    plt.figure(figsize=(10, 6))  # Set the figure size for better readability
    sns.boxplot(x=df[column])
    plt.title(f'Box Plot of {column}')
    plt.xlabel(column)
    plt.show()

numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns
# Compute the correlation matrix for numerical variables
correlation_matrix = df[numerical_columns].corr()
print("Correlation matrix:\n", correlation_matrix)

#heatmap
# Plot the correlation matrix as a heatmap
plt.figure(figsize=(20, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm')
plt.title('Heatmap of Correlation Matrix')
plt.show()

df.columns

df=pd.get_dummies(df,columns=["Type"],dtype=int)

df=pd.get_dummies(df,columns=["Location"],dtype=int)

df.head()

model = IsolationForest(n_estimators=100, contamination=0.1)
model.fit(df)
#model.fit(features)
k=df
y_pred = model.predict(k)

#add another column in df as anomaly
df['anomaly_score']=model.decision_function(k)

df.head()

anomalies = df.loc[df["anomaly_score"] < 0]
not_anomalies=df.loc[df["anomaly_score"] > 0]

anomalies

not_anomalies

df.columns

x=df[['Amount', 'Time', 'User', 'Type_Online Purchase',
       'Type_Retail Purchase', 'Location_City Center', 'Location_Online',
       'Location_Suburbs', 'anomaly_score']]
df_values=x.values
result=[]
for i in df_values:
  z=model.predict([i])
  if z==[1]:
    result.append('no')
  elif z==[-1]:
    result.append('yes')

df['Anomaly']=result

df.head()

plt.scatter(not_anomalies["Amount"], not_anomalies["anomaly_score"], label="Normal")
plt.scatter(anomalies["Amount"], anomalies["anomaly_score"],color="green", label="Anomaly")
plt.xlabel("Amount")
plt.ylabel("anomaly_score")
plt.legend()
plt.show()