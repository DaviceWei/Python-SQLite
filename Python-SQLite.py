from datetime import datetime
import sqlite3
import configparser
import os

dbname = "main-db.db" #定义数据库名字，测试使用main-db.db
m=""
logfile = open(datetime.now().strftime('%Y-%m-%d')+".log","a")#初始化日志系统


def ntime(): #函数，输出日期，格式[2022-07-14 21:49:56]
    return "["+datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"] "

def mprint(m):#自定义mprint，输出并记录日志
    logfile.write(ntime()+m+"\n")
    print(ntime()+m+"\n")
    
def mkdb():#新建数据库并插入表
    mkdb = sqlite3.connect(dbname)
    mkdb.execute("""CREATE TABLE INFO_DATABASE(IP_ADDRESS TEXT, CLI_MSG TEXT,TIME TEXT)""")

mprint("系统已运行。")

if os.path.isfile(dbname):#判断数据库是否存在，若不存在则创建
    mprint("已找到数据库 \""+dbname+"\"")
else:
    mprint("数据库不存在，系统尝试创建！")
    mkdb()
    


#连接数据库#
conndb = sqlite3.connect(dbname)
if conndb:
    mprint("成功连接至数据库 \""+dbname+"\"")
else:
    mprint("错误：数据库 \""+dbname+"\" 连接失败。")
# #

while True:
    awa=input(ntime()+"输入测试数据：")

                 
    #mprint("数据库：")
    if awa !="exit":
        get_info = "insert into info_database (IP_ADDRESS, CLI_MSG, TIME) values ('"+ip+"', '"+msg+"', '"+datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"')"
        conndb.execute(get_info)
    else:
        break

conndb.commit()
conndb.close()
mprint("系统退出。")
logfile.close()