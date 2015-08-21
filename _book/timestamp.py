import os, datetime

for (dirpath, dirnames, filenames) in os.walk("august"):
    for fname in filenames:

        filein = dirpath+"/"+fname

        f = open(filein,'r')
        filedata = []
        filedata.append(f.readline())
        f.close()

        modified = "###### Last modified: " + str(datetime.datetime.fromtimestamp(os.path.getmtime(dirpath+"/"+fname)))

        #newdata = filedata.replace("{datetime}", modified)

        f = open(filein,'w')
        for linenum in range(len(filedata)):
            if linenum == 0:
                f.write(modified)
            else:
                f.write(filedata[linenum])
            f.write("\n")
        f.close()
