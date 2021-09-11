import numpy as np

# numpy的版本和配置信息
np.__version__
np.show_config()

# 内存大小
n = np.array([1, 2, 3])
n.size
n.itemsize

# 获取某个函数的帮助文档
help(np.mean)
np.info(np.mean)
help(np.mean)



