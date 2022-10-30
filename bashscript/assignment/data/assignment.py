#!/usr/bin/env python3

import os
with open('oldFiles.txt', "r") as myfile:
    for line in myfile:
        data = line.replace("\n", "")
        base = os.path.basename(data)
        baseNew = base.replace("jane", "jdoe")
        os.chdir('/home/student-04-6b8ffd89e02c/data')
        os.rename(base, baseNew)
myfile.close()
