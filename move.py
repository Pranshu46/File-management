import shutil
import os

source = input("enter Source folder here:")
destination = input('enter destination folder here:')

source = source + '/'
destination = destination +'/'



list_of_files = os.listdir(source)
for file in list_of_files:
    shutil.move((source+file), destination)