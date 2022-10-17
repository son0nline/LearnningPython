import sqlite3

db = sqlite3.connect("Section11\contact.db")
UserName = input("Search user: ")

for UserName, Pass in db.execute("select * from users where UserName like ? ",('%'+UserName+'%',)):
    print(UserName, Pass)
    print("*"*80)

db.close()
