import hashlib
import base64

text = "{'1': 'computer', '2': 'monitor', '3': ['1', '2', '3', '4']}"
original_hash = hashlib.sha256(text.encode("utf8"))
print(f"sha256: {original_hash.hexdigest()}" )

encoded = base64.b64encode(text.encode("utf8"))
print(f"base64: {encoded}" )

encoded = base64.b64encode(b'something unknowable')
print(f"base64: {encoded}" )
