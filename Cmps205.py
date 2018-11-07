import pyodbc
server = 'alexasql.database.windows.net'
database = 'AdventureWorks2016'
username = 'cmps253'
password = 'Cmps205!'
driver= '{SQL Server}'

cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+password)

file = open("cmps205.html","w")
file = open("cmps205.html","w") 
 
file.write("<html>")
file.write("<head>")
file.write("<style>")
file.write("table, th, td { border: 1px solid black; }")
file.write("</style>")
file.write("</head>")

file.write("<table>")
 


cursor = cnxn.cursor()
cursor.execute("SELECT top 10 * from Person.Person")
row = cursor.fetchone()
while row:
   file.write("<tr><td>" + row[4] + "</td><td>" + row[6] + "</tr>")
   row = cursor.fetchone()
file.write("</table>")  
file.write("</html>") 
file.close()