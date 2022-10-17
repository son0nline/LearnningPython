import sqlite3

db = sqlite3.connect("Section11\contact.db")
# db.execute("insert into contacts (Name,Phone,Email)  values ('robin','0987654321','robin@batman.com')")
# db.execute("insert into contacts values ('batman','0987654322','iambatman@batman.com')")
# db.commit()

for Name,Phone,Email in db.execute("select * from contacts"):
    print(Name,Phone,Email)
    print("*"*80)


Name = input("input Name: ")
Phone = input("input Phone: ")
Email = input("input Email: ")


## sql injection ##
# updateSql = f"update contacts set Phone='{Phone}', Email='{Email}' where Name='{Name}'"
# print(updateSql)
# updateCmd = db.cursor()
# updateCmd.executescript(updateSql)
# # or
# updateCmd.execute(updateSql)


## alternative ##
updateSql = f"update contacts set Phone=?, Email=? where Name=?"
updateCmd = db.cursor()
updateCmd.execute(updateSql,(Phone, Email, Name))

print(f"{updateCmd.rowcount} rows effect.")
db.commit()
updateCmd.close()

db.close()
