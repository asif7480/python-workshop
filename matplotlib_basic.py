import pandas as pd
import matplotlib.pyplot as plt

sample_data = {
    'months': [1,2,3,4,5,6,7,8,9,10],
    'cases': [45, 62, 55, 32, 45, 61, 20, 15, 42, 21],
    'ages': [21, 18, 17, 24, 30 ,36, 31, 42, 28, 22]
}
print(sample_data)

df = pd.DataFrame(sample_data)
print(df)

# generating graph of a data set
df.plot(kind='bar')
plt.savefig('plot.png')

df[ df['ages']>= 20]['cases'].plot()
plt.savefig('plot')

# df[ df['ages']>= 20]['cases'].plot()
# df[ df['months']==6][['cases','ages']].plot(kind='bar')
df[ df['months']>=6][['cases','ages']].plot(kind='line')
plt.savefig('plot')

# df[ df['months']<= 20][['cases', "ages"]].plot(kind='bar')
df[ df['months']<= 20][['cases', "ages"]].plot(kind='hist')
plt.savefig('plot')

# df[ df['months']<= 20][['cases', "ages"]].plot(kind='area')
df[ df['months']<= 20][['cases', "ages"]].plot(kind='area', stacked=False)
plt.savefig('plot')

df[ df['months']<=6][['cases','ages']].plot(kind="line")
plt.suptitle('Example Data')
plt.xlabel('ages')
plt.ylabel('cases')
plt.savefig('plot')
