from transformers import GPT2Config, GPT2LMHeadModel
# import torch

# 创建一个极小的GPT-2配置
mini_config = GPT2Config(
    vocab_size=1000,  # 很小的词汇表
    n_positions=64,   # 很短的序列长度
    n_embed=64,       # 很小的嵌入维度
    n_layer=2,        # 只有2层
    n_head=2,         # 2个注意力头
    n_inner=128,      # 很小的前馈网络维度
    activation_function="gelu",
    resid_pdrop=0.1,  # dropout
    embd_pdrop=0.1,
    attn_pdrop=0.1,
)

print("模型配置:")
print(mini_config)

# 从配置创建模型（不下载预训练权重）
model = GPT2LMHeadModel(mini_config)

print("\n模型结构:")
print(model)
print(f"\n总参数量: {sum(p.numel() for p in model.parameters())};")