import pandas as pd
import os

# 文件夹路径，包含所有CSV文件
folder_path = 'F:/dataset'

# 创建一个空的列表，用于存储每个文件的数据
data_frames = []

# 遍历文件夹中的每个文件
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)

        # 读取CSV文件
        data = pd.read_csv(file_path)

        # 将数据添加到列表中
        data_frames.append(data)

# 使用pd.concat合并所有数据
merged_data = pd.concat(data_frames, ignore_index=True)

# 将时间列转换为datetime对象，以便排序
merged_data["Timestamp"] = pd.to_datetime(merged_data["Timestamp"], dayfirst=True)

# 按时间列排序
merged_data = merged_data.sort_values(by="Timestamp")

# 保存合并后的数据到新的CSV文件
merged_data.to_csv('merged_data.csv', index=False)
