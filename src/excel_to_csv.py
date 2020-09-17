import pandas as pd
import os

excel_path = '/data/Cong/excel/'
csv_path = '/data/Cong/csv/'


def excel_to_csv():
    files = os.listdir(excel_path)
    for file in files:
        if not os.path.isdir(file):
            print('开始转换：' + file)
            (file_name, extension) = os.path.splitext(file)
            data = pd.read_excel(excel_path + file, index_col=0)
            data.to_csv(csv_path + file_name+'.csv', encoding='utf-8')

    print('转换结束')


if __name__ == '__main__':
    excel_to_csv()
