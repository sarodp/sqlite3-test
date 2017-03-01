# sqlite3-test
หัดใช้และทดสอบเบื้องต้น sqlite3 บน raspery pi 3

***** วิธีติดตั้งและทดสอบ ดูที่ไฟล์ Testlog.txt  *****

รายละเอียดของไฟล์ต่างๆ เพื่อทดสอบการติดตั้งและหัดใช้งานเบื้องต้นของโปรแกรม sqlite3<br>
<br>
sqlite3_cheatsheet.txt<br>
--ตัวอย่างการใช้คำสั่งในโปรแกรม sqlite3<br>
<br>
.sqliterc<br>
--ไฟล์กำหนดค่าคัวแปรควบคุมต่างๆ ของโปรแกรม sqlite3 <br>
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
myiot.db <br>
--ไฟล์ฐานข้อมูล SQLite ที่ใช้ทดสอบ สามารถสร้างขึ้นโดยรันเชลล์สคริปท์ createmyiot.sh<br>
<br>
testselect1.py<br>  
--โปรแกรมไพทอนทดสอบการอ่าน Table จากไฟล์ฐานข้อมูล myiot.db <br>
testinsert1.py  <br>
--โปรแกรมไพทอนทดสอบการเขียนข้อมูล ลงในตาราง TMEASURE ของไฟล์ฐานข้อมูล myiot.db<br>
<br>
<br>
ลิงค์แนะนำ:<br>
=======================================<br>
วิธีติดตั้งบน raspberry pi<br>
http://raspberrywebserver.com/sql-databases/set-up-an-sqlite-database-on-a-raspberry-pi.html <brt>
http://raspberrywebserver.com/sql-databases/accessing-an-sqlite-database-with-python.html<br>
<br>
หัดใช้ sqlite3<br>
https://www.youtube.com/watch?v=QjICgmk31js&feature=youtu.be <br>
http://www.newthinktank.com/2013/05/sqlite3-tutorial/<br>
http://www.w3ii.com/en-US/sqlite/default.html<br>

คู่มืออ้างอิง sqlite3<br>
https://sqlite.org/docs.html<br>
https://www.sqlite.org/doclist.html <br>
https://sqlite.org/cli.html<br>
https://sqlite.org/lang_corefunc.html<br>
