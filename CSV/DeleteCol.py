import pandas as pd

# 源文件名
file_name = 'Thuesday-20-02-2018_TrafficForML_CICFlowMeter.csv'

# 读取CSV文件
data = pd.read_csv('F:/dataset/Thuesday-20-02-2018_TrafficForML_CICFlowMeter.csv')

# 删除名为"Label"的列
data = data.drop(columns=['Flow ID','Src IP','Src Port','Dst IP'])

# 将结果保存回原始CSV文件，从而覆盖源文件
data.to_csv(file_name, index=False)
