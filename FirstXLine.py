import pandas as pd

def display_and_export_csv(input_file, output_file, num_rows):
    try:
        # 读取CSV文件
        df = pd.read_csv(input_file)

        # 选择前5行数据
        df_head = df.head(num_rows)

        # 打印前5行数据
        print("前5行数据：")
        print(df_head)

        # 导出前5行数据到新的CSV文件
        df_head.to_csv(output_file, index=False)
        print("导出成功！")

    except FileNotFoundError:
        print("Error: 文件未找到。")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    input_filename = "D:/dataset/Friday-02-03-2018_TrafficForML_CICFlowMeter.csv"  # 替换为你的输入CSV文件名
    output_filename = "Formal5Line.csv"  # 替换为你的输出CSV文件名
    display_and_export_csv(input_filename, output_filename, num_rows=5)
