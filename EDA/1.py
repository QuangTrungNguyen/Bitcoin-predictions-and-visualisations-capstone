import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv("bitcoin_train.csv")
#print(df)
#df.info()
#print(df.describe())
corr=df.corr(method="pearson")
sns.heatmap(corr,
            xticklabels=True,
            yticklabels=True,
            cmap="YlGnBu")#,annot=True)
plt.show()
