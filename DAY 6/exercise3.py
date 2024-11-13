import os
import shutil

if not os.path.exists("job"):
    os.mkdir("job")
else:
    print("job folder already exists")

os.chdir("job")
with open("file1.txt", "w") as file:
    file.write("hello world\n")
os.chdir("..")

if not os.path.exists("job2"):
    os.rename("job", "job2")
else:
    print("job2 folder already exists")

shutil.rmtree("job2")
