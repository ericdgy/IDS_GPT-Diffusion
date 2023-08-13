import pandas as pd
from sklearn.model_selection import train_test_split
from transformers import GPT2Tokenizer, GPT2LMHeadModel, TextDataset, DataCollatorForLanguageModeling
from transformers import Trainer, TrainingArguments
from sklearn.metrics import accuracy_score
import torch

# 初始化tokenizer和模型
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# 检查GPU支持并设置设备
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# 打印当前使用的设备
if device.type == 'cuda':
    print(f"Using GPU ({torch.cuda.get_device_name(0)}) for training.")
else:
    print("Using CPU for training.")

# 准备数据
train_dataset = TextDataset(tokenizer=tokenizer, file_path="train_textualized_dataset2.txt", block_size=128)
test_dataset = TextDataset(tokenizer=tokenizer, file_path="test_textualized_dataset2.txt", block_size=128)
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

# 定义训练参数
training_args = TrainingArguments(
    output_dir="./results",
    overwrite_output_dir=True,
    num_train_epochs=3,
    per_device_train_batch_size=64,
    per_device_eval_batch_size=64,
    save_steps=10_000,
    save_total_limit=2,
    logging_dir='./logs',
    logging_steps=100,
    evaluation_strategy="epoch",
    # eval_steps=100,
    fp16=True,  # 使用半精度训练
    # gradient_accumulation_steps=2,  # 使用梯度累积
    # gradient_checkpointing=True,  # 如果需要，可以激活梯度检查点
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

# 保存模型权重和tokenizer
model.save_pretrained("./saved_model/")
tokenizer.save_pretrained("./saved_model/")
