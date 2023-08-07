import pandas as pd
from sklearn.model_selection import train_test_split

# 读取数据
data = pd.read_csv('D:/dataset/Friday-02-03-2018_TrafficForML_CICFlowMeter.csv')

# 分割数据为训练集和测试集
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)


# 将数据转化为描述性的文本格式
def row_to_text(row):
    features = row[:-1]  # 所有特征，除了最后的标签
    label = row[-1]  # 最后的标签

    # 为每个特征创建一个描述性的句子
    sentences = [f"{col} is {value}" for col, value in zip(data.columns[:-1], features)]

    # 将所有句子组合成一个段落，并添加标签描述
    text = ', '.join(sentences) + f". The type of this flow is {label}."

    return text


# 将训练集和测试集转化为描述性的文本
train_text = train_data.apply(row_to_text, axis=1)
test_text = test_data.apply(row_to_text, axis=1)

# 保存文本数据到新的文件
train_text.to_csv('train_textualized_dataset.txt', index=False, header=None)
test_text.to_csv('test_textualized_dataset.txt', index=False, header=None)