from pathlib import Path
import csv
import random

if not Path("./roster/roster.txt").is_file():
    raise FileNotFoundError("Roster File Not Found.")

if not Path("./roster/lefties.csv").is_file():
    raise FileNotFoundError("Lefties File Not Found.")

lefties = set()

with open('./roster/lefties.csv', "r") as i:
    for line in i:
        if ord('0') <= ord(line[0]) <= ord('9'):
            lefties.add(line[:line.index(',')])

with open("./roster/roster.txt", "r") as i:
    with open("./roster/roster.csv", "w") as o:
        for line in i:
            if ord('0') <= ord(line[0]) <= ord('9'):
                rep = line.replace('\t', ',')
                new_line = rep[:[i for i,v in enumerate(rep) if v == ','][3]-8]
                if (rep[:rep.index(',')] in lefties):
                    new_line += ",YES"
                else:
                    new_line += ",NO"
                new_line = new_line.replace(', ', ',')
                o.write(new_line+"\n")
            if line[:7] == "Student":
                new_line = "Student#,Last_Name,First_Name,NetID,Lefty\n"
                o.write(new_line)

csv_list = []

with open("./roster/roster.csv", 'r') as i:
    csvreader = csv.reader(i)
    csv_list = [row for row in csvreader]

random.shuffle(csv_list)

with open("./roster/roster.csv", 'w', newline='') as o:
    csvwriter = csv.writer(o, delimiter=',')
    o.write("Student#,Last_Name,First_Name,NetID,Lefty\n")
    for i in csv_list:
        csvwriter.writerow(i)