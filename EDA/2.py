import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv("bitcoin_train.csv")
#df.hist()
sns.distplot(df['volume'])
plt.show()