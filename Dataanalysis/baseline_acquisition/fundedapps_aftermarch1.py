import csv
import datetime


check_date = datetime.datetime.strptime("2019-03-05", '%Y-%m-%d')

mydict = {}
with open("data.csv","r") as filereader:
    reader = csv.reader(filereader)
    next(reader)
    for rows in reader:
        if rows[1][:4] == "www.":
            mydict[rows[1][4:]]=rows[0]
        else:
            mydict[rows[1]]=rows[0]
    filereader.close()

urls = mydict.keys()
mydict2 = {}

id_or = {}
with open("organizations.csv", "r") as filereader:
    reader = csv.reader(filereader)
    arow = next(reader)
    for rows in reader:
        for url in urls:
            if  rows[10] != '' and rows[10] == url:    
                mydict2[rows[0]]=rows[10]
                id_or[rows[0]]=mydict[url]

    filereader.close()

mydict3=[]

#print mydict2
keys = mydict2.keys()

with open("acquisitions.csv","r") as filereader:
    reader = csv.reader(filereader)
    arow = next(reader)
    print arow[23],arow[8]
    with open("acquisitions_aftermarch1.csv","w") as filewriter:
        writer = csv.writer(filewriter, delimiter=',')
        writer.writerow(["app_id"] + arow)
        for rows in reader:
            if rows[23] != '':
                date = datetime.datetime.strptime(rows[23], '%Y-%m-%d')
                if date > check_date and rows[8] in keys:
                    mydict3.append(rows[8])      
                    writer.writerow([id_or[rows[8]]] + rows)
    filereader.close()


with open("organizations.csv", "r") as filereader:
    reader = csv.reader(filereader)
    with open("org_detail_of_acquisitions_aftermarch1.csv","w") as filewriter:
        writer = csv.writer(filewriter, delimiter=',')
        writer.writerow(["app_id"] + next(reader))
        for rows in reader:
            if rows[0] in mydict3:
                writer.writerow([id_or[rows[0]]] + rows)
                
    filereader.close()
    filewriter.close()

