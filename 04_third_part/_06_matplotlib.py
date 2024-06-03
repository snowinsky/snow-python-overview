import matplotlib.pyplot as plt

# 准备数据
x = [1, 2, 3, 4]
y = [10, 15, 7, 10]

# 创建图表
plt.plot(x, y, marker='o')
plt.title('Simple Line Chart')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()