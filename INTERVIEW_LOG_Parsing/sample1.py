




import re
import csv
from collections import Counter

def reader(filename):
    with open(filename) as f:
        log=f.read()
        #print(log)

        regex = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

        ipslist = re.findall(regex, log)

        return ipslist

def count(ipslist):
    return Counter(ipslist)

def write_csv(counter):
    with open("IP-outut.csv", "w") as csvfile:
        writer = csv.writer(csvfile)

        header = ["IP", "Frequency"]

        writer.writerow(header)

        for i in counter:
            writer.writerow((i, counter[i]))




if __name__ == "__main__":
   
   write_csv(count(reader('mediumlog.txt')))