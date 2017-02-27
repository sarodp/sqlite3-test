#!usr/bin/bash
echo "create myiot.db"
sqlite3 myiot.db < createtables.sql
sqlite3 myiot.db < insertrows.sql
echo "myiot.db created."
ls -l *.db
