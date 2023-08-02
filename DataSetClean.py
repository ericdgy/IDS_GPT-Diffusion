import pandas as pd

def find_mixed_type_columns(csv_file):
    df = pd.read_csv(csv_file)
    mixed_type_columns = df.select_dtypes(include='object').columns.tolist()
    print("混合类型的列：", mixed_type_columns)

if __name__ == "__main__":
    csv_file = "D:/dataset/Friday-02-03-2018_TrafficForML_CICFlowMeter.csv"  # 替换为你的CSV文件名或文件路径
    find_mixed_type_columns(csv_file)
