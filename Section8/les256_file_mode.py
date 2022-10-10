"""
//https://docs.python.org/3/library/functions.html#open
'r' open for reading (default)

'w' open for writing, truncating the file first

'x' open for exclusive creation, failing if the file already exists

'a' open for writing, appending to the end of file if it exists

'b' binary mode

't' text mode (default)

'+' open for updating (reading and writing)
"""

with open('Section8\\testexport.txt','w+') as mFile:
    lines = [ str(key) for key in range(100) ]
    mFile.writelines( "\n".join(lines) )
    print(lines)