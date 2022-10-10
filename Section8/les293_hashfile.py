import hashlib

fileName = "Section8\\temperature_anomaly.json"
original_hashed256 = "57C91A4CB18C8247289698BC1E9B9154E11FACCE8ACA8DA23389E4D4280A2616"

with open(fileName,'rb') as bFile:
    contents = bFile.read()

checked_hash = hashlib.sha256(contents).hexdigest()
print(checked_hash)
if original_hashed256.casefold() == checked_hash:
    print("this file is original")
else:
    print("file has been modified!")