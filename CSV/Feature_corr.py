import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 读取CSV文件
df = pd.read_csv('F:/dataset/merged_data.csv')

# 删除非数值列
df = df.drop(columns=['Timestamp', 'Label'])

# 计算皮尔逊系数
corr = df.corr()

# 找出高关联的特征对
threshold = 0.8  # 设置阈值，可以根据需要调整
high_corr = []
for i in range(len(corr.columns)):
    for j in range(i):
        if abs(corr.iloc[i, j]) > threshold:
            high_corr.append((corr.columns[i], corr.columns[j], corr.iloc[i, j]))

# 打印高关联的特征对
for item in high_corr:
    print(f"Features: {item[0]} and {item[1]}, Correlation: {item[2]:.2f}")

# 绘制热度图
plt.figure(figsize=(20, 15))
sns.heatmap(corr, cmap='coolwarm', annot=True, fmt=".2f")
plt.title("Feature Correlation Heatmap")
plt.show()