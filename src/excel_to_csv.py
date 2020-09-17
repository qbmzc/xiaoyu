import pandas as pd
import os

# excel文件的路径
excel_path = '/data/Cong/excel/'
# csv文件保存的位置
csv_path = '/data/Cong/csv/'


# 定义一个转换方法
def excel_to_csv():
    # 获取所有的excel文件
    files = os.listdir(excel_path)
    # 遍历文件，每次获取一个进行操作
    for file in files:
        # 判断是文件而不是文件夹
        if not os.path.isdir(file):
            print('开始转换：' + file)
            # 获取文件名称和后缀名
            (file_name, extension) = os.path.splitext(file)
            # 读取excel,从第一行读取
            data = pd.read_excel(excel_path + file, index_col=0)
            # 写入csv文件，编码为utf-8
            data.to_csv(csv_path + file_name + '.csv', encoding='utf-8')
            pd.re
    print('转换结束')


# 主函数
if __name__ == '__main__':
    excel_to_csv()
