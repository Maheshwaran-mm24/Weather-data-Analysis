import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('weather.csv')
# Monthly average temperature
df.groupby('weather')['temp_max'].mean().plot(kind='line')
plt.show()