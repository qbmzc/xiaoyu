#-*- coding:utf-8 -*-

import os
import pandas as pd

# filename 文件名称，file_num 拆分的数量
def file_split(filename,file_num,header=True):
    if header:
        chunksize=1000000
        data1 = pd.read_table(filename, chunksize = chunksize, sep=',', encoding='gbk') 
        num = 0
        for chunk in data1:
            num += len(chunk)
        chunksize = round(num / file_num + 1)

        # 需要存的file
        head, tail = os.path.splitext(filename)
        data2 = pd.read_table(filename, chunksize = chunksize, sep=',', encoding='gbk')
        i = 0 #定文件名
        for chunk in data2:
            chunk.to_csv('{0}_{1}{2}'.format(head, i, tail),header=None,index=False)
            print('保存第{0}个数据'.format(i))
            i += 1
    else:
        # 获得每个文件需要有的行数
        chunksize = 1000000   #先初始化的chunksize是100W
        data1 = pd.read_table(filename, chunksize = chunksize ,header=None, sep=',') 
        num = 0
        for chunk in data1:
            num += len(chunk)
        chunksize = round(num / file_num + 1)

        # 需要存的file
        head, tail = os.path.splitext(filename)
        data2 = pd.read_table(filename, chunksize = chunksize ,header=None, sep=',')
        i = 0 #定文件名
        for chunk in data2:
            chunk.to_csv('{0}_{1}{2}'.format(head, i, tail),header=None,index=False) 
            print('保存第{0}个数据'.format(i))
            i += 1
    
if __name__ == '__main__':
    filename = '/data/Cong/test1.csv' # 这里修改为自己的文件位置
    file_split(filename, 20, header=False)