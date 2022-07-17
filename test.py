import glob
import os
os.chdir("./xqc")
files = glob.glob("./*")

for file in files:
    if(os.path.basename(file).isascii()):
        print(":}")
    else:
        print(os.path.basename(file))

print("okay funding secured")