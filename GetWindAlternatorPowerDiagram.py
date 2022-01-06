import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure


WindTurbine=pd.read_csv(r"C:\Datasets-base\Datasets\Scada\T1.csv")
print(WindTurbine.head(10))
WT_df=WindTurbine.copy()
print(WT_df.head(10))