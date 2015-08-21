import os, datetime, shutil

if os.path.exists("output"):
    shutil.rmtree('output')
os.makedirs("output")

for (dirpath, dirnames, filenames) in os.walk("source"):
    if dirpath == "source":
        continue
    pathed = dirpath.replace("source/","")
    if not os.path.exists("output/"+pathed):
        os.makedirs("output/"+pathed);
    for fname in filenames:
        if fname[-3:] != ".md":
            continue

        filein = dirpath+"/"+fname
        fileout = "output/"+pathed+"/"+fname

        f = open(filein,'r')
        filedata = f.readlines()
        f.close()

        modified = "###### Last modified: " + str(datetime.datetime.fromtimestamp(os.path.getmtime(dirpath+"/"+fname)))

        f = open(fileout,'w')
        for linenum in range(len(filedata)):
            if linenum == 0:
                f.write(modified+"\n")
                continue
            f.write(filedata[linenum])
        f.close()
