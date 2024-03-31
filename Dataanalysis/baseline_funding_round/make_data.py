import csv

prohibited = ["google","facebook","amazon","instagram"]

with open("BASELINE_apps.csv","r") as filereader:
    reader = csv.reader(filereader)
    next(reader)
    with open("data.csv","w") as filewriter:
        writer = csv.writer(filewriter, delimiter=',')
        writer.writerow(["app_id","domain"])
        for rows in reader:
            if rows[1]!='':
                url = rows[1]
                domain = url.split("://")[1].split("/")[0]
                if any(urls not in domain for urls in prohibited):
                    writer.writerow([rows[0],domain])
                else:
                    print domain
            elif rows[2]!='':
                url = rows[2]
                domain = url.split("://")[1].split("/")[0]
                if any(urls not in domain for urls in prohibited):
                    writer.writerow([rows[0],domain])
                else:
                    print domain
                
                
