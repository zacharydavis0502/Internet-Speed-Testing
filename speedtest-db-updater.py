import sys
import csv
import pyspeedtest
import mysql.connector
from datetime import datetime

mydb = mysql.connector.connect(host = "####", user = "####", password = "####", database = "####")

mycursor = mydb.cursor()

def dbTableSizeCheck():
    sqlcount =  "SELECT COUNT(*) FROM dataTable"
    mycursor.execute(sqlcount)
    result = mycursor.fetchone()
    strresult = str(result)

    only_nums = "".join([c for c in strresult if c.isdigit()])
    only_nums = int(only_nums)
    
    if(only_nums >= 100):
        print("true")
        return True
    else:
        return False

def insertData():
    
    timews = datetime.now()
    time = str(timews.strftime("%m-%d-%Y %H:%M:%S"))
    st = pyspeedtest.SpeedTest()
    ping = round(st.ping(), 2)
    download = round(st.download()/1000000, 2)
    upload = round(st.upload()/1000000, 2)
    host = st.host
    
    sql = "INSERT INTO dataTable (TIME, PING, DOWN, UP, HOST) VALUES (%s, %s, %s, %s, %s)"
    val = (time, ping, download, upload, host)

    mycursor.execute(sql, val)
    mydb.commit()

def tableToCsv():
    query = "SELECT * FROM dataTable"
    mycursor.execute(query)
    result = mycursor.fetchall()
    timews = datetime.now()
    fileTime = timews.strftime("%m-%d-%Y")
    c = csv.writer(open('/var/www/ftpFiles/Internet Speed Data/dataTableDump_' + fileTime + '.csv', 'w'))
    #header = "DATE,PING,DOWNLOAD,UPLOAD,HOST"
    #c.write(header)
    for x in result:
        c.writerow(x)

    print("DB DATA WRITTEN TO CSV")

def wipeDb():
    wipe = "DELETE FROM dataTable"
    mycursor.execute(wipe)
    print("DB WIPED!!")

if (dbTableSizeCheck() == True):
    tableToCsv()
    wipeDb()
    insertData()
else:
    insertData()



