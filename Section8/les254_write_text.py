
available_parts = {"1": "computer",
                   "2": "monitor",
                   "3": "keyboard",
                   "4": "mouse",
                   "5": "hdmi cable",
                   "6": "dvd drive",
                   }

# with open('Section8\\testexport.txt','w+') as mFile:
#     lines = [ available_parts.get(key) for key in available_parts ]
#     mFile.writelines( "\n".join(lines) )
#     print(lines)

# print value to file    
with open('Section8\\testexport.txt','w') as mFile2:
    for key in available_parts:
        value = available_parts[key]
        print(value, file=mFile2)

