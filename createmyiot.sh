#!/bin/sh
rm myiot.db
echo "\\>create myiot.db"
sqlite3 myiot.db < createtables.sql
sqlite3 myiot.db < insertrows.sql
echo "\\>ls -l *.db"
ls -l *.db
