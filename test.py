from os import *
import os

test = os.system("curl --upload-file ./test.txt https://transfer.sh/hello.txt")
print(test)
#https://transfer.sh/N5sySl/hello.txt