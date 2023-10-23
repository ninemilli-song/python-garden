from pycrawlers import huggingface

urls = ['https://huggingface.co/albert-base-v2/tree/main',
        'https://huggingface.co/dmis-lab/biosyn-sapbert-bc5cdr-disease/tree/main']

paths = ['./model_1/albert-base-v2', './model_2/']
# 实例化类
# 使用默认 base_url (https://huggingface.co)

hg = huggingface()
# 自定义 base_uel
# hg = huggingface('https://huggingface.co')
# 输入 huggingface 的 token，下载需要权限的模型或数据集
# token = "xxxxxyyyyywwwwwccccc"
# hg = huggingface(token=token)

# 1. 单个获取
# 1.1 使用默认保存位置（'./'）
hg.get_data(urls[0])

# 1.2 自定义保存地址
# hg.get_data(urls[0], paths[0])

# 2.批量获取
# 2.1 使用默认保存位置（'./'）
hg.get_batch_data(urls)

# 2.2 自定义保存地址
# hg.get_batch_data(urls, paths)