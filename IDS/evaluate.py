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
    output = model.generate(input_ids, attention_mask=attention_mask, pad_token_id=tokenizer.eos_token_id,
                            max_new_tokens=50)
    decoded_output = tokenizer.decode(output[0])
    filtered_output = filter_output(decoded_output)  # 过滤输出

    # 检查filtered_output是否为空
    if not filtered_output.strip():
        return "."  # 如果为空，则只返回一个点
    return filtered_output.split()[-1] + "."  # 在生成的最后一个词后添加“.”

# 评估模型
test_data = pd.read_csv('test_textualized_dataset2.txt', header=None, names=["Text"])

# 选择测试数据的一个子集
sample_size = 1000  # 你可以根据需要调整这个数字
test_data_sample = test_data.sample(n=sample_size, random_state=42)

# 使用子集提取test_texts和true_labels
true_labels = test_data_sample["Text"].str.split().str[-1].tolist()
test_texts = test_data_sample["Text"].str.rsplit(n=1).str[0].tolist()

predicted_labels = []
for text in tqdm(test_texts, desc="Evaluating"):  # 使用tqdm显示进度
    predicted_labels.append(generate_prediction(text))
accuracy = accuracy_score(true_labels, predicted_labels)
print(f"Accuracy: {accuracy*100:.2f}%")