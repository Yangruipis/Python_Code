import pymysql
f = open(r'D:\Data\SZ000839.csv')# Load the csv
header = True
conn = pymysql.connect('localhost','root','password','database')
cur = conn.cursor()

for line in f:
    if header:
        header = False # Skip the header
    else:
        data = line.replace('\"','').replace('\n','').split(',')
        cur.execute("INSERT INTO SZ000839(symbol,_date,_open,high,low,_close,volume) VALUES ('%s','%s','%s','%s','%s','%s','%s')" % tuple(data))

conn.commit()# Commit the transaction
f.close() # Don't forget to close all of these
cur.close()
conn.close()
print('finished!')