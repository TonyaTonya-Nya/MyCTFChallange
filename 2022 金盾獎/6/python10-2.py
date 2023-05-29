import glob
import os
import zipfile
import time



# 列表推导式


def unzip_files():
    file_lst = glob.glob('./*')
    filename_lst = [os.path.basename(i) for i in file_lst]
    for filename in filename_lst:
        if '.' in filename:
            suffix = filename.split('.')[-1]
            if suffix == 'zip':
                unzip(filename)
                os.remove(filename)

def unzip(filename):
    zip_file = zipfile.ZipFile(filename)
    s=filename.split('.')[0]
    
    
    bb=str(eval(s))
    b=bytes(bb, 'utf-8')
    zip_file.setpassword(b)
    # 类似tar解除打包，建立文件夹存放解压的多个文件

    zip_file.extractall()
    zip_file.close()

while(1):
    unzip_files()