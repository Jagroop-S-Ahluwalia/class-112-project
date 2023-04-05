import os
import shutil

from_dir=r"C:\Users\jagsm\Downloads\empty"
to_dir=r"C:\Users\jagsm\Downloads\myimagefolder"


listoffiles = os.listdir(from_dir)

# print(listoffiles)

for i in listoffiles:
    # print(i)

    name,extention = os.path.splitext(i)
    # print(extention)

    if(extention ==""):
        continue

    if extention in [".jpg",".png",".gif",".jpeg",".exe"]:
        path1 = from_dir+"/"+i
        path2 = to_dir+"/"+"imageflies"
        path3 = to_dir+"/"+"imageflies"+"/"+i

        if os.path.exists(path2):
            print("moving")
            shutil.move(path1,path3)

        else:
            os.makedirs(path2)
            print("moving")
            shutil.move(path1,path3)

    