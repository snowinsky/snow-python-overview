from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import load_boston_house as boston_house

# 加载波士顿房价数据集

X, y = boston_house.data, boston_house.target

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建并训练模型
model = LinearRegression()
model.fit(X_train, y_train)

# 预测
predictions = model.predict(X_test)

# 评估
print("模型得分:", model.score(X_test, y_test))