import os
import shutil


path = input("enter the name of directory to be sorted:-")

list_of_files = os.listdir(path)

for file in list_of_files:
    name, ext = os.path.splitext(file)

    ext = ext[1:]


    if ext == '':
        continue


    if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)

        else:
            os.mikedirs(paths+'/'+ext)
            shutil.move(path+'/'+filr, path+'/'+ext+'/'+file)