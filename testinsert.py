#!/usr/bin/python
import time
import random
import sqlite3

#01-------------------------------
mydb1 = '/home/pi/myiot/myiot01.db'
cn1 = sqlite3.connect(mydb1)

print "\nSQLite == 1.Test read tables fron python."
print "Database file:", mydb1
print "-----------------------------------"

#1--staglist
staglist = ['T1','T2','H1','H2','KW1','KW2']
sql1 = '''select distinct STAG from TSETTING'''
cur1 = cn1.execute(sql1)
staglist = cur1.fetchall()

#2--sql3
#--insert into TMEASURE (STAG,SVALUE) values ('T1', 25.0);
print "\n",time.asctime( time.localtime(time.time()) )
print "\nSQLite == 2.Test insert record into table from python."

xcount = 10000
sql30 = '''insert into TMEASURE (STAG,SVALUE) values ('T1', 25);'''
sql3fmt = '''insert into TMEASURE (STAG,SVALUE) values ('%s', %.1f);'''

tstart = time.asctime( time.localtime(time.time()) )

try:
	for xi in range(1,xcount):
		xc = '%s' % (random.choice(staglist))
		xv = random.random()*100
		sql3 = sql3fmt % (xc,xv)
		cn1.execute(sql3)
	cn1.commit()
	xmsg = '\n\nSQL OK:'
except:
	cn1.rollback()
	xmsg = '\n\nSQL ERROR:'

print "\n",time.asctime( time.localtime(time.time()) )


tdone = time.asctime( time.localtime(time.time()) )

print xmsg, sql3
print "record count= %i" % (xcount)
print "timestart:", tstart
print "timedone: ", tdone

#2a---
sql1 = '''select * from TMEASURE '''
cursor1 = cn1.execute(sql1)	
tb01 = cursor1.fetchall()
print "\n========================================="
print "Query:",sql1
print  "  no.of rows = %i\n" % (len(tb01))
i=0


#99---done
cn1.close()
