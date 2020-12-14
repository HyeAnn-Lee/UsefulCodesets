with open('FileName.txt', 'w') as filehandle:
    for list_1D in list_2D:
        for item in list_1D:
            filehandle.write('%s\t' % item)
        filehandle.write("\n")
