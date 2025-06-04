# init_env.py - 放在 GitHub 上，在 Colab 中通过 %run 加载
# 功能：自动安装依赖 + 导入库 + 准备好环境，使用清华镜像

import sys
import subprocess
import importlib

def install(package):
    subprocess.check_call([
        sys.executable, "-m", "pip", "install", "-q",
        package,
        "-i", "https://pypi.tuna.tsinghua.edu.cn/simple"
    ])

# 自动安装必要库（如果未安装）
try:
    import torch
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np
    import d2l
except ImportError:
    print("⏳ 缺少依赖，正在使用清华镜像安装...")
    install("torch")
    install("matplotlib")
    install("pandas")
    install("numpy")
    install("d2l==0.17")
    print("✅ 依赖已通过清华镜像安装完成")

# 导入库
import torch
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import d2l

print("🎉 环境已准备好，可以直接开始学习/训练！")
