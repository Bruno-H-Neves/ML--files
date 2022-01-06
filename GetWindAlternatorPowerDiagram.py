import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import warnings
warnings.filterwarnings("ignore")


WindTurbine=pd.read_csv(r"C:\Datasets-base\Datasets\Scada\T1.csv")
#print(WindTurbine.head(10))
WT_df=WindTurbine.copy()
#print(WT_df.head(10))
#print('Describe:\n',WT_df.describe())
#print('Null Values:\n',WT_df.isnull().sum())
#print('Info:\n',WT_df.info())

def plot_1(df):
    plt.figure(figsize=(25,10))
    sns.scatterplot(data=df,x='Wind Speed (m/s)',y='LV ActivePower (kW)',s=1,label='Real (KW)',color='purple') 
    sns.scatterplot(data=df,x='Wind Speed (m/s)',y='Theoretical_Power_Curve (KWh)',s=1,label='Theorical (kwh)',color='green') 
    plt.xlabel('wind speed (m/s)', size=10)
    plt.ylabel('Power Production (kw)', size=10)
    plt.title('Wind Turbine Power Production vs Theorical Production')
    plt.legend(fontsize=8)
    plt.show()

def plot_2(df, show_real=False):
    plt.figure(figsize=(25,10))
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


#plot_1(WT_df)

Real_data = WT_df['LV ActivePower (kW)']                #make a list
Teorical_data = WT_df['Theoretical_Power_Curve (KWh)']  #make a list
Theo_P_Max=[]
Theo_P_Min=[]
limits=(0.95,1.05)
for power in Teorical_data:
    Theo_P_Max.append(power*limits[1])
    Theo_P_Min.append(power*limits[0])

WT_df['Theo_P_Max']=Theo_P_Max
WT_df['Theo_P_Min']=Theo_P_Min
plot_2(WT_df,True)


#make a histerisys 