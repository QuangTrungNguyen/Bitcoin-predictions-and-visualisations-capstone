import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv("bitcoin_train.csv")
df1=df.drop(df.columns[5:39],axis=1)#.info()
#sns.pairplot(df1)
#sns.regplot(x="close",y="low",data=df1)
plt.scatter(x=df1["close"],y=df1["low"])
plt.show()
