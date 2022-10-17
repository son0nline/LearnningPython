import sqlite3

db = sqlite3.connect("Section11\contact.db")

db.execute("insert into contacts (Name,Phone,Email)  values ('robin','0987654321','robin@batman.com')")
db.execute("insert into contacts values ('batman','0987654322','iambatman@batman.com')")
db.commit()

for Name,Phone,Email in db.execute("select * from contacts"):
    print(Name,Phone,Email)
    print("*"*80)

updatesql = "update contacts set phone = '9999' where name = 'robin'"
updateCmd = db.cursor()
updateCmd.execute(updatesql)

print(f"{updateCmd.rowcount} rows effect")
updateCmd.connection.commit()
# the same with 
#db.commit()
print(updateCmd.connection == db)

updateCmd.close()

for Name,Phone,Email in db.execute("select * from contacts"):
    print(Name,Phone,Email)
    print("*"*80)

db.execute("delete from contacts")
db.commit()

db.close()