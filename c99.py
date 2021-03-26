import os
import shutil
path = input("enter the name of directories to be sorted out:")
list_of_files= os.listdir(path)
for file in list_of_files:
    name, ext = os.path.splitext(file)
 
    ext=ext[1:]
    print(name+''+ext)
    if ext =='':
        continue
    if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)
    else:
        os.mkdir(path+'/'+ext)
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)