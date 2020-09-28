from numpy import *

# 曼哈顿距离
vector1 = mat([1, 2, 3])
vector2 = mat([4, 5, 6])
print(sum(abs(vector1 - vector2)))

# 欧式距离
vector1 = mat([1, 2, 3])
vector2 = mat([4, 5, 6])
print(sqrt((vector1 - vector2) * (vector1 - vector2).T))

# 闵可夫斯基距离
# 切比雪夫距离
# vector1 = mat([1, 2, 3])
# vector2 = mat([4, 5, 6])
# print(sqrt(abs(vector1 - vector2).max))

# 夹角余弦
# vector1 = mat([1, 2, 3])
# vector2 = mat([4, 5, 6])
# print(dot(vector1, vector2)/(linalg.norm(vector1)*linalg.norm(vector2)))

# 汉明距离
matV = mat([1, 1, 1, 1], [1, 0, 0, 1])
smstr = nonzero(matV[0]-matV[1])
print(smstr)

# 杰卡德相似系数
import scipy.spatial.distance as dist
matV = mat([1, 1, 1, 1], [1, 0, 0, 1])
print(dist.pdist(matV, 'jaccard'))