f = open('/data/Cong/text1.txt','r') #打开文件
i = 0 #设置计数器
while i<12345 : #这里12345表示文件行数，如果不知道行数可用每行长度等其他条件来判断
    with open('newfile'+str(i),'w') as f1:
        for j in range(0,100) : #这里设置每个子文件的大小
            if i < 12345 : #这里判断是否已结束，否则最后可能报错
                f1.writelines(f.readline())
                i = i+1
            else:
                break