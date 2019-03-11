# -*- coding: UTF-8 -*-
# 检查素材中命名不规范的序列（不从img_0000开始）
import os
# 表情素材路径
ExpressionPath = "E:/Projects/Student's Platform/material/Expression-MNIST/disgust/"
# 获取该目录下所有文件，存入列表中
ExpressionFile = os.listdir(ExpressionPath)

for EachFile in ExpressionFile:
    SingleExpressionPath = ExpressionPath + EachFile + "/"
    SinglePictureFile = os.listdir(SingleExpressionPath)
    if SinglePictureFile[0] != "img_0000.jpg":
        print(EachFile)

