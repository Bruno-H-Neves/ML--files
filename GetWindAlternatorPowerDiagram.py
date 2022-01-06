import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import warnings
warnings.filterwarnings("ignore")
import numpy as np


WindTurbine=pd.read_csv(r"C:\Datasets-base\Datasets\Scada\T1.csv")
#print(WindTurbine.head(10))
WT_df=WindTurbine.copy()
#print(WT_df.head(10))
#print('Describe:\n',WT_df.describe())
#print('Null Values:\n',WT_df.isnull().sum())
#print('Info:\n',WT_df.info())

def plot_1(df):
    plt.figure(figsize=(15,10))
    sns.scatterplot(data=df,x='Wind Speed (m/s)',y='LV ActivePower (kW)',s=1,label='Real (KW)',color='purple') 
    sns.scatterplot(data=df,x='Wind Speed (m/s)',y='Theoretical_Power_Curve (KWh)',s=1,label='Theorical (kwh)',color='green') 
    plt.xlabel('wind speed (m/s)', size=10)
    plt.ylabel('Power Production (kw)', size=10)
    plt.title('Wind Turbine Power Production vs Theorical Production')
    plt.legend(fontsize=8)
    plt.show()

def plot_2(df, show_real=False):
    plt.figure(figsize=(15,10))
    sns.scatterplot(data=df,x='Wind Speed (m/s)',y='Theoretical_Power_Curve (KWh)',s=1,label='Theorical (kwh)',color='green') 
    sns.scatterplot(data=df,x='Wind Speed (m/s)',y='Theo_P_Max',s=1,label='Max power accept (KW)',color='red') 
    sns.scatterplot(data=df,x='Wind Speed (m/s)',y='Theo_P_Min',s=1,label='Min power accept (KW)',color='blue') 
    if show_real:
        sns.scatterplot(data=df,x='Wind Speed (m/s)',y='LV ActivePower (kW)',s=1,label='Real (KW)',color='orange')        

    plt.xlabel('wind speed (m/s)', size=10)
    plt.ylabel('KWh', size=10)
    plt.title('Wind Turbine Theorical Production and limits')
    plt.legend(fontsize=8)
    plt.show()


plot_1(WT_df)

#make a histerisys
Real_data = WT_df['LV ActivePower (kW)']                #make a list
Teorical_data = WT_df['Theoretical_Power_Curve (KWh)']  #make a list
Theo_P_Max=[]
Theo_P_Min=[]
limits=(0.97,1.03)
for power in Teorical_data:
    Theo_P_Max.append(power*limits[1])
    Theo_P_Min.append(power*limits[0])

WT_df['Theo_P_Max']=Theo_P_Max
WT_df['Theo_P_Min']=Theo_P_Min
plot_2(WT_df,True)

#make data for machine learning

def data_ML(df):
    
    y = df['Theoretical_Power_Curve (KWh)'].values
    X = df['Wind Speed (m/s)'].values
    return X, y

X,y=data_ML(WT_df)
#print('Feature:\n',type(X[0]))
#print('Target:\n',type(y[0]))

from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesRegressor
from sklearn import metrics

def show_results(x_te,y_te,x_tr,y_tr,y_pr):
    Mabs=metrics.mean_absolute_error(y_te, y_pr)
    MSq=metrics.mean_absolute_error(y_te, y_pr)
    RMSquared  = np.sqrt(metrics.mean_squared_error(y_te, y_pr))
    Acc_Tr=model.score(x_tr,y_tr)
    Acc_test= model.score(x_te,y_te)
    Error={'MAbs:':Mabs,
           'MSq:': MSq,
           'RMSquared:':RMSquared,
           'Acc on Traning:': Acc_Tr,
           'Acc on Testing:': Acc_test}
    for idx, error in enumerate(Error):
        print(f'{error} -> {Error[error]}')

def plot_3(df):
    plt.figure(figsize=(15,10))
    sns.scatterplot(data=df,x='wind',y= 'y_test',s=1,label='Real Curve',color='green') 
    sns.scatterplot(data=df,x='wind',y= 'y_pred',s=1,label='Machine Learning Curve',color='red') 
    plt.xlabel('wind speed (m/s)', size=10)
    plt.ylabel('KWh', size=10)
    plt.title('Real vs Predict Turbine Curve')
    plt.legend(fontsize=8)
    plt.show()


X_train, X_test, y_train, y_test = train_test_split(X.reshape(-1,1), y, test_size = 0.70, random_state = 42)

model=ExtraTreesRegressor()
#print(X_train.shape)
#print(y_train.shape)
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
show_results(X_test,y_test,X_train,y_train,y_pred)

#print(X_test)
#print(y_test.shape)
#print(y_pred.shape)
X_test1=[]
for test in X_test:
    X_test1.append(test[0])

columns=['wind','y_test','y_pred']
df_test=pd.DataFrame(columns=columns)
df_test['wind']=X_test1
df_test['y_test']=y_test
df_test['y_pred']=y_pred
#print(df_test)
plot_3(df_test)

import joblib


filename = 'Kaggle_Wind_Turbine_Turkey.sav'
joblib.dump(model, filename)                    # Save model current folder 

load_model = joblib.load(filename)              # load file 
nb = input('Introduce a Wind Speed (m/s):')
data=[[nb]]
test23=load_model.predict(data)
print(f'Theoric Active Power: {test23[0]} KW')