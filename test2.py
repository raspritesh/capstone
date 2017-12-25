import time
import MySQLdb as m
import serial
import types
import rfidreader1
db=m.connect("localhost","root","","cap")
import RPi.GPIO as gpio
sql="""CREATE TABLE IF NOT EXISTS d(id varchar(10) primary key,name varchar(20) not null,bookid varchar(10) not null,bookname varchar(30) not null,issuedate varchar(10),returndate varchar(10),status varchar(5))"""
cur=db.cursor()
cur.execute(sql)
while True:
	res=rfidreader1.reading()
	print res
	sql="select id,name,bookname,issuedate,returndate,status from d where bookid='%s';" %res
	cur.execute(sql)
	try:
		
		cur.execute(sql)
		db.commit()
            
        except:
            	print "unable to fetch data"
	
	
                
	time.sleep(1)	

	
