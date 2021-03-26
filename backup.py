import os
import shutil
src= input("enter source folder name : ")
dst= input("enter destination folder name : ")

src=src+'/'
dst=dst+'/'

list_of_files=os.listdir(src)
for file in list_of_files:
    shutil.copy((src+file), dst)