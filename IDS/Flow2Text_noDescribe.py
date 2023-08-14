import pandas as pd
from sklearn.model_selection import train_test_split
# 读取数据
data = pd.read_csv('F:/dataset/Friday-02-03-2018_TrafficForML_CICFlowMeter.csv')

# 分割数据为训练集和测试集
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

# 将每一行转换为只包含数值的文本
def row_to_text(row):
    features = ' '.join([str(row[col]) for col in data.columns if col != 'Label'])
    return f"{features} {row['Label']}."

# 将每一行应用上述函数并保存为文本文件
def save_to_textualized_file(data, filename):
    textualized_data = data.apply(row_to_text, axis=1)
    with open(filename, 'w') as f:
        for item in textualized_data:
            f.write("%s\n" % item)

# 转换并保存训练集和测试集
save_to_textualized_file(train_data, 'train_textualized_dataset2.txt')
save_to_textualized_file(test_data, 'test_textualized_dataset2.txt')
