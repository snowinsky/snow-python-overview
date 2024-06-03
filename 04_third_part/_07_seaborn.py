import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# 假设有一个数据集
data = pd.DataFrame([[1, 2], [2, 3]], columns=['A', 'B'], index=['X', 'Y'])
sns.heatmap(data, annot=True, cmap='coolwarm')
plt.show()