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
print('Describe:\n',WT_df.describe())
print('Null Values:\n',WT_df.isnull().sum())
print('Info:\n',WT_df.info())


Real_data = WT_df['LV ActivePower (kW)']                #make a list
Teorical_data = WT_df['Theoretical_Power_Curve (KWh)']  #make a list
plt.figure(figsize=(25,10))
sns.scatterplot(data=WT_df,x='Wind Speed (m/s)',y='LV ActivePower (kW)',s=1,label='Real (KW)',color='purple') 
sns.scatterplot(data=WT_df,x='Wind Speed (m/s)',y='Theoretical_Power_Curve (KWh)',s=1,label='Theorical (kwh)',color='green') 
plt.xlabel('wind speed (m/s)', size=10)
plt.ylabel('Power Production (kw)', size=10)
plt.title('Wind Turbine Power Production vs Theorical Production')
plt.legend(fontsize=8)
plt.show()
