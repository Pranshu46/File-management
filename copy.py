import os
import shutil

source = input("enter source folder here")

destination = input('enter source folder here')

dest = shutil.copy(source, destination)

print ("after copying file:")

print(os.listdir(path))