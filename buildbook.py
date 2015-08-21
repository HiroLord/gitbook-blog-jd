import os, datetime

for (dirpath, dirnames, filenames) in os.walk("source"):
    for fname in filenames:

        filein = dirpath+"/"+fname
        outpath = dirpath.replace("source/","")
        fileout = "output/"+outpath+"/"+fname

        f = open(filein,'r')
        filedata = []
        filedata.append(f.readline())
        f.close()

        modified = "###### Last modified: " + str(datetime.datetime.fromtimestamp(os.path.getmtime(dirpath+"/"+fname)))

        f = open(fileout,'w')
        for linenum in range(len(filedata)):
            if linenum == 0:
                f.write(modified+"\n")
                continue
        f.write(filedata[linenum])
        f.close()
