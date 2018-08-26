import os
import csv
import re

wordsInLine = []
tempWord = []
urlList = []


def count():
    flag = 0
    print("Reading all file names in sorted order")
    print("Boolean value for containing javascript code (1) otherwise (0)")
    for filename in sorted(os.listdir(os.getcwd())):
    #open up the file containing the email
        file=open(filename)
        count1 = 0
        for line in file:
            #create a list that contains is each word in each line
            wordsInLine = line.split(' ')
            #For each word try to split it with :
            for word in wordsInLine:
                
                if re.search('</script>',word,re.I):
                    count1=1

        file.close()
        urlList.append(count1)
        if flag!=0:
            print "File Name = " + filename
            print "Boolean value for email = ",count1
        flag = flag+1

count()
final = urlList[1:]
print "Final Boolean value list"
print final

with open('js.csv', 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    for val in final:
        wr.writerow([val])
print("CSV file generated")