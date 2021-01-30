# !/bin/python3
#  这是一个图片批量压缩工具，
# 使用方法为： 
# python3 image.py -i 输入路径 -o 输出路径
# 如：
#  python3 image.py -i ~/Desktop/cat/ -o ~/Desktop/cat_dist/


from PIL import Image
import os
import shutil
import sys
import getopt

# pip install pillow


# 
def compressImage(srcPath, dstPath):
    for filename in os.listdir(srcPath):
        # 如果不存在目的目录则创建一个，保持层级结构
        if not os.path.exists(dstPath):
            os.makedirs(dstPath)

        # 拼接完整的文件或文件夹路径
        srcFile = os.path.join(srcPath, filename)
        dstFile = os.path.join(dstPath, filename)

        # 如果是文件就处理
        if os.path.isfile(srcFile):
            try:
                # 打开原图片缩小后保存，可以用if srcFile.endswith(".jpg")或者split，splitext等函数等针对特定文件压缩
                sImg = Image.open(srcFile)
                w, h = sImg.size
                # 设置压缩尺寸和选项，注意尺寸要用括号
                dImg = sImg.resize((int(w/2), int(h/2)), Image.ANTIALIAS)
                # 也可以用srcFile原路径保存,或者更改后缀保存，save这个函数后面可以加压缩编码选项JPEG之类的
                dImg.save(dstFile)
                print(dstFile+" 成功！")
            except Exception:
                print(dstFile+"失败！")

        # 如果是文件夹就递归
        if os.path.isdir(srcFile):
            compressImage(srcFile, dstFile)


if __name__ == '__main__':
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print('image.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    print('输入的文件为：', inputfile)
    print('输出的文件为：', outputfile)

    # 遍历压缩图片
    compressImage(inputfile, outputfile)
