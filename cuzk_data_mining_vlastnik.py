import urllib.request
import os
import csv
#set working directory
wd = os.chdir(r'C:\Users\patmic\Desktop\KODUJU\DATAMINING_KATASTR')
#create new csv file
with open ("jenisov_vlastnici_dopln.csv", "w", encoding="UTF-16") as output:
    # open csv file with cadastral identificator and cadastral parcel label
    ownerswriter = csv.writer(output)
    with open('jenisov_vlastnici.csv') as owners:
        ownersreader = csv.reader(owners, delimiter = ';')
        numline = len(owners.readlines())
        # get back at first row of csv file with seek command
        owners.seek(0)
        i = 0
        for row in ownersreader:
            if i > 0 and i <numline:
                url ="http://vdp.cuzk.cz/vdp/ruian/vlastnici?typ=pa&id="+str(row[0])
                #print(url)
                gethtml = urllib.request.urlopen(url).read().decode('UTF-8')
                ownurl= gethtml.split('</td><td class="right"')
                ownurl1=ownurl[0].split('<td>')
                ownurl2=ownurl1[-1].split(",")
                ownerswriter.writerow(row+[ownurl2[0]])
                print('row '+str(i)+' is ok')
            i+=1


