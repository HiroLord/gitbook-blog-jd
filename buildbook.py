import os, datetime, shutil

if os.path.exists("output"):
    shutil.rmtree("output")
os.makedirs("output")


for (dirpath, dirnames, filenames) in os.walk("source"):

    if dirpath == "source":
        continue

    for fname in filenames:
        if fname[-3:] != ".md":
            continue

        filein = dirpath+"/"+fname
        outpath = "output/"+dirpath.replace("source/","")
        fileout = outpath+"/"+fname

        if not os.path.exists(outpath):
            os.makedirs(outpath)

        f = open(filein,'r')
        filedata = f.readlines()
        f.close()

        modified = "###### Last modified on " + datetime.datetime.fromtimestamp(os.path.getmtime(dirpath+"/"+fname)).strftime("%b %d, %Y at %I:%M %p")

        f = open(fileout,'w')
        for linenum in range(len(filedata)):
            if linenum == 0:
                f.write(modified+"\n")
                continue
            f.write(filedata[linenum])
        f.close()
