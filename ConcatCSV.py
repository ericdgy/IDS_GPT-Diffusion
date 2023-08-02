import os
import pandas as pd

def merge_csv_files_by_time(folder_path):
    try:
        # 获取文件夹中所有文件的列表
        file_list = os.listdir(folder_path)

        # 用于存储所有CSV文件的DataFrame列表
        dfs = []

        # 遍历文件夹中的所有文件
        for filename in file_list:
            # 确保文件是CSV文件
            if filename.endswith(".csv"):
                # 构建CSV文件的完整路径
                file_path = os.path.join(folder_path, filename)

                # 读取CSV文件，并将"Timestamp"列解析为日期时间类型
                df = pd.read_csv(file_path, parse_dates=["Timestamp"], dayfirst=True)

                # 将DataFrame添加到列表中
                dfs.append(df)

        # 合并DataFrame列表为一个新的DataFrame，按照"Timestamp"列排序
        merged_df = pd.concat(dfs).sort_values(by="Timestamp")

        # 打印合并后的DataFrame
        print("合并后的DataFrame:")
        print(merged_df)

        # 保存合并后的DataFrame为新的CSV文件
        merged_df.to_csv("merged_data.csv", index=False)
        print("合并后的数据保存成功！")

    except FileNotFoundError:
        print("Error: 文件夹未找到。")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    folder_path = "D:/dataset"  # 替换为你的文件夹路径
    merge_csv_files_by_time(folder_path)
