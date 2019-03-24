import os

fp =open("path.txt","w")
for root, dirs, files in os.walk(os.path.abspath("./test_files/")):
    for file in files:
        fp.write(os.path.join(root, file))
        fp.write("\n")
fp.close()