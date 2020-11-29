import csv
import os, sys



if __name__ == "__main__":
   
      
    fileName = input('Enter file name : ')
          
          
    file = open(fileName, 'r')
    reader = csv.reader(file)

    #next(reader, None)

    #row is a list of all elements in the csv line
    for row in reader:
       
        print(", ".join(row))
