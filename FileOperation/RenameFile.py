import os
path = "E:/Projects/Student's Platform/material/Expression-MNIST/anger/take0116/"

# 获取要修改子目录名称的文件夹，存入列表中
FilePath = os.listdir(path)

n = 0
for EachPicture in FilePath:
    #设置旧文件名（就是路径+文件名）
    oldname = path + FilePath[n]
    # 设置新文件名
    newname = path + "img_" + str('%04d' % n) + ".jpg"
    # 用os模块中的rename方法对文件改名
    os.rename(oldname, newname)
    print(oldname, '======>', newname)
    n += 1
