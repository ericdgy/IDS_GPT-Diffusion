import pandas as pd
from transformers import GPT2Tokenizer, GPT2LMHeadModel
from sklearn.metrics import accuracy_score
import torch
from tqdm import tqdm
import re

# 加载保存的tokenizer和模型
tokenizer = GPT2Tokenizer.from_pretrained("./saved_model/")
model = GPT2LMHeadModel.from_pretrained("./saved_model/")

# 检查GPU支持并设置设备
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

def filter_output(output):
    """确保输出只包含字母和空格"""
    return re.sub(r'[^a-zA-Z\s]', '', output)

# 使用微调后的模型生成预测
def generate_prediction(text):
    input_ids = tokenizer.encode(text, return_tensors="pt", truncation=True, max_length=512).to(device)
    attention_mask = torch.ones(input_ids.shape, device=device)  # 创建全1的attention_mask
    output = model.generate(input_ids, attention_mask=attention_mask, pad_token_id=tokenizer.eos_token_id, max_new_tokens=50)
    decoded_output = tokenizer.decode(output[0])
    filtered_output = filter_output(decoded_output)  # 过滤输出
    return filtered_output.split()[-1]  # 返回生成的最后一个词，即预测的标签

# 评估模型
test_data = pd.read_csv('test_textualized_dataset2.txt', header=None, names=["Text"])

# 仅提取第一个文本和其对应的标签
first_text = test_data["Text"].iloc[90]
true_label = first_text.split()[-1]
test_text = " ".join(first_text.split()[:-1])

# 显示输入
print("Input Text:", test_text)

# 生成预测
predicted_label = generate_prediction(test_text) + "."

# 显示输出
print("Predicted Label:", predicted_label)
print("True Label:", true_label)

# 如果你想比较预测标签和真实标签，可以这样做：
if predicted_label == true_label:
    print("Prediction is correct!")
else:
    print("Prediction is incorrect.")
