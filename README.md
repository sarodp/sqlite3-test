# sqlite3-test
หัดใช้และทดสอบเบื้องต้น sqlite3 บน raspery pi 3  

## วิธีติดตั้งและทดสอบ
ตัวอย่าง การติดตั้งและทดสอบด้วย command line   
แสดงไว้ด้วยไฟล์ Testlog.txt  
  https://github.com/sarodp/sqlite3-test/blob/master/testlog.txt  
<br><br>
## รายละเอียดไฟล์ต่างๆ  
* sqlite3_cheatsheet.txt  
--ตัวอย่างการใช้คำสั่งในโปรแกรม sqlite3   
<br>
* .sqliterc  
--ไฟล์กำหนดค่าคัวแปรควบคุมต่างๆ ของโปรแกรม sqlite3  
--ให้ก็อปปี้ไฟล์เซ็ตติ้งไว้ที่น่ี /home/pi/.sqliterc  
<br>
* createmyiot.sh  
--สคริปท์ไฟล์สร้างไฟล์ฐานข้อมูล myiot.db  
--$chmod +x createmyiot.sh  
<br>
* createtables.sql    
--สคริปท์ SQL สร้างตาราง TMEASURE กับ TSETTING  
<br>
* insertrows.sql  
--สคริปท์ SQL เพิ่มเรคคอร์ดให้กับตาราง TMEASURE กับ TSETTING  
<br>
* myiot.db  
--ไฟล์ฐานข้อมูล SQLite ที่ใช้ทดสอบ สามารถสร้างขึ้นโดยรันเชลล์สคริปท์ createmyiot.sh  
<br>
* testselect1.py  
--โปรแกรมไพทอนทดสอบการอ่าน Table จากไฟล์ฐานข้อมูล myiot.db  
<br>
* testinsert1.py  
--โปรแกรมไพทอนทดสอบการเขียนข้อมูลลงตาราง TMEASURE ของไฟล์ฐานข้อมูล myiot.db  
<br><br>

## ลิงค์แนะนำ:     
* วิธีติดตั้งบน raspberry pi  
http://raspberrywebserver.com/sql-databases/set-up-an-sqlite-database-on-a-raspberry-pi.html  
http://raspberrywebserver.com/sql-databases/accessing-an-sqlite-database-with-python.html  
<br><br>
* หัดใช้ sqlite3  
part 1  
https://www.youtube.com/watch?v=QjICgmk31js&feature=youtu.be  
http://www.newthinktank.com/2013/05/sqlite3-tutorial/  
part 2  
https://www.youtube.com/watch?v=dBnOn17pI7c  
http://www.newthinktank.com/2013/06/sqlite3-tutorial-2/  
<br><br>
* หัดใช้ SQL  
http://www.w3ii.com/sql/default.html  
สรุปย่อประโยคคำสั่ง SQL  
http://www.w3ii.com/sql/sql_quickref.html  
<br><br>
* คู่มืออ้างอิง sqlite3  
https://sqlite.org/docs.html  
https://www.sqlite.org/doclist.html  
https://sqlite.org/cli.html  
https://sqlite.org/lang_corefunc.html  

<br><br>
