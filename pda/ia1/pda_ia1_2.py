# -*- coding: utf-8 -*-
"""pda_ia1_2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1T5SdL8NKNjfr-HwmIwdhjOIfm5ekxx9h
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder,MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,confusion_matrix,classification_report

df=pd.read_csv('https://raw.githubusercontent.com/Deepsphere-AI/LVA-Batch5-Assessment/main/booking.csv')

df.info()

df.head()

df.duplicated().sum()

#no duplicates but for safety if data is updates we are removing duplicates.
df.drop_duplicates(inplace=True)

df.duplicated().sum()

df.isnull().sum()

mode_rt=df['room type'].mode()[0]
mode_rt

x=pd.DataFrame()
x['rt']=df['room type'].isna()

#num values in room type and average price
mode_rt=df['room type'].mode()[0]
df['room type']=df['room type']
median_avg_pr=df['average price'].median()
df['average price']=df['average price'].fillna(median_avg_pr)

df.isnull().sum()

cat_col=[x for x in df.select_dtypes(include=['object']).columns]
for c in cat_col:
  plt.figure(figsize=(10,5))
  df[c].value_counts().plot(kind='bar')
  plt.title(f'bar chart of {c}')
  plt.xlabel(f'{c}')
  plt.ylabel('frequency')
  plt.show()

num_col=[x for x in df.select_dtypes(include=['int64','float64']).columns]
for n in num_col:
  plt.figure(figsize=(10,5))
  sns.histplot(df[n])
  plt.title(f'histogram chart of {n}')
  plt.xlabel(f'{n}')
  plt.ylabel('frequency')
  plt.show()

for i in range(len(num_col)):
  for j in range(i+1,len(num_col)):
    plt.figure(figsize=(10,5))
    sns.scatterplot(data=df,x=num_col[i],y=num_col[j])
    plt.title(f'scatter chart of {i} and {j}')
    plt.xlabel(f'{i}')
    plt.ylabel(j)
    plt.show()

cor_mat=df[num_col].corr()
cor_mat

plt.figure(figsize=(10,5))
sns.heatmap(cor_mat,cmap='coolwarm',annot=True)
plt.title('heat map of corrilation')
plt.show()

#outlier
num_col=[x for x in df.select_dtypes(include=['int64','float64']).columns]
for n in num_col:
  plt.figure(figsize=(10,5))
  sns.boxplot(df[n])
  plt.title(f'box plot of {n}')
  plt.xlabel(f'{n}')
  plt.ylabel('frequency')
  plt.show()

#encoding of cat
le=LabelEncoder()
for i in cat_col:
  df[i]=le.fit_transform(df[i])

df.head()

df.isnull().sum()

#split data
x=df.drop(columns='booking status')
y=df['booking status']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

#scaling
scaler=MinMaxScaler()
x_train=scaler.fit_transform(x_train)
x_test=scaler.transform(x_test)

model=LogisticRegression()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
print(y_pred)

#evaluation accuracy_score,precision_score,recall_score,f1_score,confusion_matrix,classification_report
acc_s=accuracy_score(y_test,y_pred)
print(f'accuracy score {acc_s}')
prec_s=precision_score(y_test,y_pred)
print(f'precision score {prec_s}')
rec_s=recall_score(y_test,y_pred)
print(f'recall score {rec_s}')
f1_s=f1_score(y_test,y_pred)
print(f'f1 score {f1_s}')

c_mat=confusion_matrix(y_test,y_pred)
print(c_mat)

c_report=classification_report(y_test,y_pred)
print(c_report)

