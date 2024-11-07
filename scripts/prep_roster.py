from pathlib import Path
import csv
import random

def prep_roster(shuffle=True):
    accom_file = list(Path('./input').glob('*.csv'))
    if len(accom_file) == 0:
        raise FileNotFoundError("csv File for Accomodations not Found in Input Directory")
    if len(accom_file) > 1:
        raise RuntimeError("Too Many .csv Files Found in Input Directory")
    accom_file = accom_file[0]

    if not Path("input/roster.txt").is_file():
        raise FileNotFoundError("Roster File Not Found.")
                

    # Make Roster File
    with open("input/roster.txt", "r") as in_file:
        with open("roster/roster.csv", "w") as out_file:
            for line in in_file:
                if ord('0') <= ord(line[0]) <= ord('9'):
                    rep = line.replace('\t', ',')
                    new_line = rep[:[i for i,v in enumerate(rep) if v == ','][3]-8]
                    new_line = new_line.replace(', ', ',')
                    out_file.write(new_line+"\n")
                if line[:7] == "Student":
                    new_line = "Student#,Last_Name,First_Name,NetID,Lefty,Questions\n"
                    out_file.write(new_line)

    # Clean Up Accomodation Table
    with open(accom_file, "r") as in_file:
        with open('roster/accom.csv', 'w') as out_file:
            reader = csv.reader(in_file, delimiter=',')
            writer = csv.writer(out_file, delimiter=',')
            writer.writerow(['NetID','Lefty','Questions'])
            for line in reader:
                # print(line[-1][line[-1].find('@'):])
                if line[-1][line[-1].find('@'):] != '@uci.edu':
                    continue
                writer.writerow([line[-1][:line[-1].find('@')], line[0], line[1]])

    #Adding Accomodations to Roster Table
    csv_list = []

    with open("roster/roster.csv", 'r') as i:
        csvreader = csv.reader(i)
        csv_list = [row + ["No", "No"] for row in csvreader][1:]

    for line in csv_list:
        with open('roster/accom.csv', 'r') as in_file:
            accom_reader = csv.reader(in_file, delimiter=',')
            for read_accom_line in accom_reader:
                if read_accom_line[0].lower() == line[3].lower():
                    csv_list[-2], csv_list[-1] = read_accom_line[1:]

    with open("roster/roster.csv", 'w', newline='') as o:
        csvwriter = csv.writer(o, delimiter=',')
        o.write("Student#,Last_Name,First_Name,NetID,Lefty,Questions\n")
        for i in csv_list:
            csvwriter.writerow(i)
    
    with open('roster/roster.csv', 'r+') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        writer = csv.writer(csv_file, delimiter=',')
        for read_roster_line in reader:
            with open('roster/accom.csv', 'r') as in_file:
                accom_reader = csv.reader(csv_file, delimiter=',')
                for read_accom_line in accom_reader:
                    if read_accom_line[0].lower() == read_roster_line[4].lower():
                        read_roster_line += read_accom_line[1:]
                        writer.writerow(read_roster_line)
                    


    csv_list = []

    with open("roster/roster.csv", 'r') as i:
        csvreader = csv.reader(i)
        csv_list = [row for row in csvreader][1:]

    random.shuffle(csv_list)

    with open("roster/roster.csv", 'w', newline='') as o:
        csvwriter = csv.writer(o, delimiter=',')
        o.write("Student#,Last_Name,First_Name,NetID,Lefty,Questions\n")
        for i in csv_list:
            csvwriter.writerow(i)