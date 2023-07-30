import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('covid_dataset_updated.csv')
print(df.head(20))


print(df[df['Cases']>=10]['Deaths'])
df[df['Cases']==50]['Month'].plot(kind="bar")
plt.savefig('plot.png')