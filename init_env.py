# init_env.py

# 安装必要库（清华镜像）
!pip install -q d2l==0.17 torch matplotlib pandas numpy -i https://pypi.tuna.tsinghua.edu.cn/simple

# 导入库
import torch
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import d2l

print("✅ 环境已准备好")