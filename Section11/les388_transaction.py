import sqlite3

db = sqlite3.connect("Section11\contact.db")

for Name,Phone,Email in db.execute("select * from contacts"):
    print(Name,Phone,Email)
    print("*"*80)


Name = input("what do you want to delete?: ")
## alternative ##
updateSql = f"delete from contacts where Name=?"
updateCmd = db.cursor()
updateCmd.execute(updateSql,(Name,))

print(f"{updateCmd.rowcount} rows effect.")
for Name,Phone,Email in db.execute("select * from contacts"):
    print(Name,Phone,Email)
    print("*"*80)

db.rollback()
print("*"*80)
for Name,Phone,Email in db.execute("select * from contacts"):
    print(Name,Phone,Email)
    print("*"*80)

updateCmd.close()
db.close()
