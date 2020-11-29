def txtTocsv(inFile, outFileName ):
    
    outFile = open(outFileName, 'w+')
    outFile.write('"First Name","Count"\n')
    for line in inFile:
        print(line)
        #the orignal file (GirlsName.txt) has some inconsistent formating from line 102 until eof 
        # the following try except handles comma and space separaters.
     
        try:
            words = line.split(",")
            strLine =  words[0].strip() + ','  + words[1].strip() + '\n'
        except:
            words = line.split()+[""]  # adding item to list in case line is corrupted
            
            strLine =  words[0].strip() + ','  + words[1].strip() + '\n'
        outFile.write(strLine)
    inFile.close()
    outFile.close()



if __name__ == "__main__":
    inFile1 = open('2000_BoysNames.txt', 'r')
    txtTocsv(inFile1,"2000_BoysName.csv")

    inFile2 = open('2000_GirlsNames.txt', 'r')
    txtTocsv(inFile2,"2000_GirlsNames.csv")
    