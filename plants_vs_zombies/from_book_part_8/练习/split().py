text = "Fitten Code 是一个 基于 Transformer 模型 的 AI"
result = text.split()
print(result)  # 输出: ['Fitten', 'Code', '是一个', '基于', 'Transformer', '模型', '的', 'AI']

# 使用特定的分隔符
text = "Fitten,Code,是一个,基于,Transformer,模型,的,AI"
result = text.split(',')
print(result)  # 输出: ['Fitten', 'Code', '是一个', '基于', 'Transformer', '模型', '的', 'AI']
