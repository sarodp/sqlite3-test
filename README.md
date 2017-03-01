# sqlite3-test
หัดใช้และทดสอบเบื้องต้น sqlite3 บน raspery pi 3<br>
<br>
ตัวอย่าง วิธีติดตั้งและทดสอบ ดูที่ไฟล์ Testlog.txt<br>
<br>
<br>
ไฟล์ต่างๆ เพื่อทดสอบการติดตั้งและหัดใช้งานเบื้องต้นของโปรแกรม sqlite3<br>
========================================================<br>
sqlite3_cheatsheet.txt<br>
--ตัวอย่างการใช้คำสั่งในโปรแกรม sqlite3<br>
<br>
.sqliterc<br>
--ไฟล์กำหนดค่าคัวแปรควบคุมต่างๆ ของโปรแกรม sqlite3<br>
--ให้ก็อปปี้ไฟล์เซ็ตติ้งไว้ที่น่ี /home/pi/.sqliterc<br>  
<br>
createmyiot.sh<br>
--สคริปท์ไฟล์สร้างไฟล์ฐานข้อมูล myiot.db  <br>
--$chmod +x createmyiot.sh  <br>
<br>
createtables.sql<br> 
--สคริปท์ SQL สร้างตาราง TMEASURE กับ TSETTING<br>
<br>
insertrows.sql<br>
--สคริปท์ SQL เพิ่มเรคคอร์ดให้กับตาราง TMEASURE กับ TSETTING<br>
<br>
myiot.db  
--ไฟล์ฐานข้อมูล SQLite ที่ใช้ทดสอบ สามารถสร้างขึ้นโดยรันเชลล์สคริปท์ createmyiot.sh  
<br>
testselect1.py    
--โปรแกรมไพทอนทดสอบการอ่าน Table จากไฟล์ฐานข้อมูล myiot.db  
<br>
testinsert1.py  
--โปรแกรมไพทอนทดสอบการเขียนข้อมูลลงตาราง TMEASURE ของไฟล์ฐานข้อมูล myiot.db  
<br>
<br>
ลิงค์แนะนำ:  
=======================================  
วิธีติดตั้งบน raspberry pi  
http://raspberrywebserver.com/sql-databases/set-up-an-sqlite-database-on-a-raspberry-pi.html  
http://raspberrywebserver.com/sql-databases/accessing-an-sqlite-database-with-python.html  
<br><br>
หัดใช้ sqlite3  
part 1  
https://www.youtube.com/watch?v=QjICgmk31js&feature=youtu.be  
http://www.newthinktank.com/2013/05/sqlite3-tutorial/  
part 2  
https://www.youtube.com/watch?v=dBnOn17pI7c  
http://www.newthinktank.com/2013/06/sqlite3-tutorial-2/  
<br>
http://www.newthinktank.com/2013/05/sqlite3-tutorial/  
http://www.w3ii.com/en-US/sqlite/default.html  
<br><br>
คู่มืออ้างอิง sqlite3  
https://sqlite.org/docs.html  
https://www.sqlite.org/doclist.html  
https://sqlite.org/cli.html  
https://sqlite.org/lang_corefunc.html  
<br>
