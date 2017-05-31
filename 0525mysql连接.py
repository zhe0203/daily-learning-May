# -*- coding=utf-8 -*-
 
 

 
import os
import MySQLdb
import logging
 
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
logging.basicConfig(filename=log_file, level=logging.DEBUG)
 
def main():

    #传入用户名和密码
    dbuser =""
    dbpass =""
    dbhost=""
    dbname=""
 

    arr_tags = []
    db = MySQLdb.connect( dbhost, dbuser ,dbpass,dbname,charset="UTF8")
    cursor = db.cursor()
   
    sql = "select id, content from cx limit 10";
	


    print sql

    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()

        for row in results:
            id = row[0]
          
            content = row[1]
           
            #print tmp_row
            print id, content

         

    except Exception as e:
        print "Error: unable to fecth data"
        print e

    db.close()
    print "done"
    csvfile.close()


if __name__ == "__main__":
     main()
     #下面是测试
     #print get_tags('基金3号产品和基金21号')
