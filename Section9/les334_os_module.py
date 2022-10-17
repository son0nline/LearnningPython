import os

strPath = "D:\\"
print(os.path.exists(strPath))

objectWalk = os.walk(".") # '.' mean current folder

with open("Section9\\walk.txt","w",encoding="utf-8") as swriter:
    for i in objectWalk:# struct {"path", [list folders], [list files]}
        print(i,file=swriter)


def list_directories(s: str):
    def dir_list(d):
        dirs = os.listdir(d)         
        lsFiles = []
        lsFolders = []

        for f in dirs:
            path = os.path.join(d,f)
            if os.path.isdir(path):
               lsFolders.append(f)
            elif os.path.isfile(path):
                lsFiles.append(f)

            print("folder" if os.path.isdir(path) else "file",f)
        print("*"*80)
        print(lsFiles)
    
    if os.path.exists(strPath):
        print(f"Directory listing of {s}")
        dir_list(s)
        
    else:
        print(f"Directory {s} is not exist!")

list_directories(strPath)
        

