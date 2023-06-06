import glob, os

# 数据集的位置
imgs_dir = 'images'   #图片文件夹的‘相对路径’
print(imgs_dir)

#用作 test 的图片数据的比例
percentage_test = 20;     #数据集比例划分*/100

#创建训练数据集和测试数据集：train.txt 和 test.txt
file_train = open('train.txt', 'w')    #创建train。txt
file_test = open('val.txt', 'w')        #创建val。txt
counter = 1
index_test = round(100 / percentage_test)
for pathAndFilename in glob.iglob(os.path.join(imgs_dir, "*.jpg")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))

    if counter == index_test:
        counter = 1
        file_test.write('data/images' + "/" + title + '.jpg' + "\n")   #在linux下根据你的yolo文件夹和你数据文件夹的关系去写
    else:
        file_train.write('data/images' + "/" + title + '.jpg' + "\n")
        counter = counter + 1



