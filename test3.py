import time
from datetime import date
import MySQLdb as m
import serial
import types
import rfidreader1
def fine(d1,m1,y1,d2,m2,y2):
    d=date(y1,m1,d1)
    e=date(y2,m2,d2)
    delta=e-d
    a=delta.days
    return (a-14)*1
db=m.connect("localhost","root","","cap")
import RPi.GPIO as gpio
sql="""CREATE TABLE IF NOT EXISTS d(id varchar(10) primary key,name varchar(20) not null,bookid varchar(10) not null,bookname varchar(30) not null,issuedate varchar(10),returndate varchar(10),status varchar(5))"""
cur=db.cursor()
cur.execute(sql)
while True:
	res=rfidreader1.reading()
	print res
	sql="select id,name,bookname,issuedate,returndate from d where bookid='%s';" %res
	cur.execute(sql)
	result=cur.fetchall()
	for row in result:
                Id=row[0]
                name=row[1]
                bookname=row[2]
                issuedate=row[3]
                returndate=row[4]
        print "ID='%s'"%Id
        print "name='%s'"%name
        print "bookname='%s'"%bookname
        l=issuedate.split('/')
        k=returndate.split('/')
        p=map(int,l)
        o=map(int,k)
        print p[2]
        g=fine(p[0],p[1],p[2],o[0],o[1],o[2])
        print g
		
        if result is None and res!=None:
                inp1=raw_input("Enter ID").strip('\n')
                inp2=raw_input("Enter name").strip('\n')
                inp3=raw_input("Enter bookname").strip('\n')
                inp4=raw_input("Enter issuedate").strip('\n')
                inp5=raw_input("Enter return date").strip('\n')
                inp6=raw_input("Enter status").strip('\n')
                sql="insert into d(id,name,bookid,bookname,issuedate,returndate,status) values('%s','%s','%s','%s','%s','%s','%s');"%(inp1,inp2,res,inp3,inp4,inp5,inp6)
                try:
                	
                        cur.execute(sql)
                        db.commit()
			
		except Exception as e:
                	print "Some error occured:",e
                        db.rollback()
	
                
	time.sleep(1)


	
