import sqlite3

db = sqlite3.connect("Section11\contact.db")
db.execute("CREATE TABLE IF NOT EXISTS contacts ('Name'	TEXT,	'Phone'	TEXT,    'Email'	TEXT)")

db.execute("insert into contacts (Name,Phone,Email)  values ('robin','0987654321','robin@batman.com')")
db.execute("insert into contacts values ('batman','0987654322','iambatman@batman.com')")
#remember that
db.commit()

cursor = db.cursor()
cursor.execute("select * from contacts")
#print(cursor.fetchall())
print(cursor.fetchone())
for Name,Phone,Email in cursor:
    print(Name,Phone,Email)
    print("*"*80)

cursor.close()


# db.execute("insert into Users values ('robin','0987654321')")
# db.execute("insert into Users values ('batman','0987654322')")
# #remember that
# db.commit()

db.close()