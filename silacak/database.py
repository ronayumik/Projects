import pyodbc
# from sqlalchemy import *

connectstring = 'mssql+pyodbc://sa:ar4rfv.@10.199.14.30/pelacakan'
connectstring2 = 'DRIVER={ODBC Driver 13 for SQL Server};SERVER=10.199.14.30;DATABASE=pelacakan;UID=sa;PWD=ar4rfv.'
cnxn = pyodbc.connect(connectstring2)
cursor = cnxn.cursor()

# SET NOCOUNT ON should be added to prevent errors thrown by cursor

sql = """select pub_judul from publikasi_dosen limit 10"""

result = cursor.execute(sql)
print result

# print result.fetchall()

# result.nextset()
# print result.fetchall()
# result.nextset()
# print result.fetchall()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      