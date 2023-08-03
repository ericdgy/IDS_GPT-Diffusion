import os
import pandas as pd

def get_unique_labels_in_csv_file(csv_file):
    try:
        # 读取CSV文件
        df = pd.read_csv(csv_file)

        # 获取CSV文件的标签列（假设标签列名为'Label'，根据实际情况修改）
        labels = df['Label'].unique()

        return labels

    except FileNotFoundError:
        print(f"Error: 文件未找到 - {csv_file}")
    except Exception as e:
        print(f"Error: {e}")

def count_unique_labels_in_csv_folder(folder_path):
    try:
        # 获取文件夹中所有文件的列表
        file_list = os.listdir(folder_path)

        # 创建一个字典来保存每个文件的标签数量和标签名称列表
        file_labels_dict = {}

        # 遍历文件夹中的所有文件
        for filename in file_list:
            # 确保文件是CSV文件
            if filename.endswith(".csv"):
                # 构建CSV文件的完整路径
                file_path = os.path.join(folder_path, filename)

                # 获取CSV文件中不同标签的数量
                label_counts = get_unique_labels_in_csv_file(file_path)

                # 将标签数量和标签名称列表添加到字典中，以文件名为键
                file_labels_dict[filename] = {
                    "count": len(label_counts),
                    "labels": label_counts.tolist()
                }

        # 打印每个文件的标签数量和标签名称列表
        print("每个CSV文件中不同标签的数量和标签名称列表：")
        for filename, label_info in file_labels_dict.items():
            label_count = label_info["count"]
            labels = label_info["labels"]
            print(f"{filename}: 标签数量 = {label_count}, 标签名称 = {labels}")

    except FileNotFoundError:
        print("Error: 文件夹未找到。")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    folder_path = "D:/dataset"  # 替换为你的文件夹路径
    count_unique_labels_in_csv_folder(folder_path)
