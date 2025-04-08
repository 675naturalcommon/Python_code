fp=open('note.txt','w')#open-->打开文件 w-->write
print('北京欢迎你',file=fp)#将"北京欢迎你"输出(写入)到note.txt文件
fp.close()#关闭文件