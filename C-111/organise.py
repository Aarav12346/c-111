import os
import shutil

from_dir = "C:/Users/Rohan Kapoor/Downloads"
to_dir = "C:/WhitehatJR/Class/download.images"

list_of_files = os.listdir(from_dir)
#print(list_of_files)

#move all img files from downloads folder to another folder
for file_name in list_of_files:
 name,extension = os.path.splitext(file_name)
 #print ( name)
 #print(extension)
 if extension == ' ':
  continue
 if extension in ['.pdf']:
  path1 = from_dir + '/' + file_name
  path2 = to_dir + '/' + "Image_Files"
  path3 = to_dir + '/' + "Image_Files" + '/' + file_name

  if os.path.exists(path2) :
   print("moving" + file_name + ".....")
   #moving from path one to path three
   shutil.move(path1, path3)
  else:
   os.mkdir(path2)
   print("moving" + file_name + ".....") 
   shutil.move(path1, path3)
