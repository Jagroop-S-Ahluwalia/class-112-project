import os
import shutil


from_dir=r"C:\Users\jagsm\Downloads\empty"
to_dir=r"C:\Users\jagsm\Downloads\mydocfolder"

listoffiles=os.listdir(from_dir)
# print(listoffiles)


for i in listoffiles:
    # print(i)

    name,extenstion = os.path.splitext(i)

    print(extenstion)

    if(extenstion ==""):
        continue

    if extenstion in [".pptx",".txt",".xlsx",".docx",".exe"]:
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