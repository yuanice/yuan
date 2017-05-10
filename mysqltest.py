#mysqldb    
import time, MySQLdb      
conn=MySQLdb.connect(host="localhost",user="root",passwd="root",db="qq",charset="utf8")  
cursor = conn.cursor()       
print('连接成功')      
