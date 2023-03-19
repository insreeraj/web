import numpy as np
import pandas as pd
import os
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

from imblearn.over_sampling import SMOTE
from imblearn.pipeline import make_pipeline
from pylab import rcParams
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score, recall_score, confusion_matrix
from sklearn.metrics import f1_score, roc_auc_score, roc_curve
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
import xgboost as xgb
import pickle
from sklearn.model_selection import train_test_split

df1 =pd.read_csv("main_project-bank-full.csv")


df1['default'] = df1['default'].map( 
                   {'yes':1 ,'no':0}) 
df1['loan'] = np.where(df1['loan'] =='yes', 1, 0)
df1['housing'] = np.where(df1['housing'] =='yes', 1, 0)
df1['marital'] = np.where(df1['marital'] =='married', 0,np.where(df1['marital'] =='single', 1,np.where(df1['marital'] =='divorced', 2, -1)))
df1['job'] = df1['job'].replace({'management' :1, 'technician' :2, 'entrepreneur':3,
                             'blue-collar' :4, 'retired' :5, 'admin.':6,
                             'services' :7, 'self-employed' :8, 'unemployed' :9,
                             'housemaid':10, 'student':11, 'unknown':-1
                             })
df1['education'] = df1['education'].replace({'tertiary' :1, 'secondary' :2, 'primary':3,
                       'unknown':-1})
df1['contact'] = df1['contact'].replace({'cellular' :1, 'telephone' :2,
                       'unknown':-1})
df1['month'] = df1['month'].replace({'jan' :1, 'feb' :2, 'mar':3,
                             'apr' :4, 'may' :5, 'jun':6,
                             'jul' :7, 'aug' :8, 'sep' :9,
                             'oct':10, 'nov':11, 'dec':12
                             })
df1['poutcome'] = df1['poutcome'].replace({'failure' :1, 'other' :2,'success' :3,
                       'unknown':-1})
df1['Target'] = np.where(df1['Target'] =='yes', 1, 0)
df1=df1.fillna(method='pad')
sm = SMOTE()

X = df1.drop(['Target'], axis=1)
y = df1['Target']
X_sm, y_sm = sm.fit_resample(X, y)
X_train1, X_test1, y_train1, y_test1 = train_test_split(X_sm, y_sm, test_size = 0.3, random_state = 0)

model = xgb.XGBClassifier()
model.fit(X_train1, y_train1)

pickle.dump(model,open('model.pkl','wb'))