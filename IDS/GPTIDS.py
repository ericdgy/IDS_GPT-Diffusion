import pandas as pd
from sklearn.model_selection import train_test_split
from transformers import GPT2Tokenizer, GPT2LMHeadModel, TextDataset, DataCollatorForLanguageModeling
from transformers import Trainer, TrainingArguments
from sklearn.metrics import accuracy_score
import torch

# 初始化tokenizer和模型
tokenizer = GPT2Tokenizer.from_pretrained("gpt2-medium")
model = GPT2LMHeadModel.from_pretrained("gpt2-medium")

# 检查GPU支持并设置设备
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# 打印当前使用的设备
if device.type == 'cuda':
    print(f"Using GPU ({torch.cuda.get_device_name(0)}) for training.")
else:
    print("Using CPU for training.")

# 准备数据
train_dataset = TextDataset(tokenizer=tokenizer, file_path="train_textualized_dataset.txt", block_size=128)
test_dataset = TextDataset(tokenizer=tokenizer, file_path="test_textualized_dataset.txt", block_size=128)
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

# 定义训练参数
training_args = TrainingArguments(
    output_dir="./results",
    overwrite_output_dir=True,
    num_train_epochs=3,
    per_device_train_batch_size=8,  # 根据RTX 2080的8GB显存调整
    per_device_eval_batch_size=8,   # 根据RTX 2080的8GB显存调整
    save_steps=10_000,
    save_total_limit=2,
    logging_dir='./logs',
    logging_steps=100,  # 每100步打印一次训练进度和损失
    evaluation_strategy="steps",  # 每logging_steps步评估一次模型
    eval_steps=100,  # 每100步评估一次模型
)


# 创建Trainer实例
trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=train_dataset,
    eval_dataset=test_dataset,
)

# 微调模型
trainer.train()

# 使用微调后的模型生成预测
def generate_prediction(text):
    input_ids = tokenizer.encode(text, return_tensors="pt").to(device)
    output = model.generate(input_ids)
    decoded_output = tokenizer.decode(output[0])
    return decoded_output.split()[-1]  # 返回生成的最后一个词，即预测的标签

# 评估模型
test_data = pd.read_csv('test_textualized_dataset.txt', header=None, names=["Text"])
true_labels = test_data["Text"].str.split().str[-1].tolist()  # 从文本化的数据中提取真实的标签
test_texts = test_data["Text"].str.rsplit(' ', 1).str[0].tolist()  # 移除真实的标签，只保留特征描述
predicted_labels = [generate_prediction(text) for text in test_texts]
accuracy = accuracy_score(true_labels, predicted_labels)
print(f"Accuracy: {accuracy*100:.2f}%")
