# filetxt = open('Section8\demo.txt','r')

# for line in filetxt:
#     print(line,end='')

# filetxt.close()

# like using in C#
# with open('Section8\demo.txt','r') as filetxt:
#     for line in filetxt:
#         print(line.rstrip())


with open('Section8\demo.txt','r') as filetxt:
    lines = filetxt.readlines() # đọc xong là nó close luôn :|
    #allText = filetxt.read()

with open('Section8\demo.txt','r') as filetxt:    
    allText = filetxt.read()

print('allText',"*"*40)
print(allText)

print("*"*40)
print("".join(lines))
print("*"*40)
print( "".join(reversed(lines)))
