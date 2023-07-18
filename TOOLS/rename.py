# 先重命名再进行数据标注
# 图片存放的路径
# 如果图片里本来就有以 1.jpg这样命名的文件，则需要把num = 1改成 其他的 如 num = 333 把名字改掉 再重新搞成 num = 1
import os
path = r"F:\DEEPLEARNING\仪表数据集\数字仪表数据集"

# 遍历更改文件名
num = 1
for file in os.listdir(path):

    os.rename(os.path.join(path, file), os.path.join(path, str(num)) + ".jpg")
    num = num + 1