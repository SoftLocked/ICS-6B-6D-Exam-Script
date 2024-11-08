from pathlib import Path
import csv
import random


accom_file = list(Path('./input').glob('*.csv'))
if len(accom_file) == 0:
    raise FileNotFoundError("csv File for Accomodations not Found in Input Directory")
if len(accom_file) > 1:
    raise RuntimeError("Too Many .csv Files Found in Input Directory")
accom_file = accom_file[0]

if not Path("input/roster.txt").is_file():
    raise FileNotFoundError("Roster File Not Found.")


def make_roster_file():
    '''
    Makes Roster File
    '''
    with open("input/roster.txt", "r") as in_file:
        with open("internal_data/roster.csv", "w", newline='') as out_file:
            for line in in_file:
                if ord('0') <= ord(line[0]) <= ord('9') or line[0] == '*':
                    rep = line.replace('\t', ',')
                    rep = rep.replace('*', '')
                    new_line = rep[:[i for i,v in enumerate(rep) if v == ','][3]-8]
                    new_line = new_line.replace(', ', ',')
                    out_file.write(new_line+"\n")
                if line[:7] == "Student":
                    new_line = "Student#,Last_Name,First_Name,NetID,Lefty,Questions\n"
                    out_file.write(new_line)

def clean_accom_table(prior_left, prior_aisle):
    '''
    Cleans Up the User-Supplied Accomodation Table
    '''
    global accom_file
    with open(accom_file, "r") as in_file:
        with open('internal_data/accom.csv', 'w', newline='') as out_file:
            reader = csv.reader(in_file, delimiter=',')
            writer = csv.writer(out_file, delimiter=',')
            writer.writerow(['NetID','Lefty','Questions'])
            for line in reader:
                if len(line) > 3:
                    line = line[-3:]
                if not (line[0] and line[1] and line[2]):
                    continue
                if line[-1][line[-1].find('@'):] != '@uci.edu':
                    continue
                if not prior_left:
                    line[0] = 'n'
                if not prior_aisle:
                    line[1] = 'n'
                writer.writerow([line[-1][:line[-1].find('@')], 1 if line[0][0].lower() == 'y' else 0, 1 if line[1][0].lower() == 'y' else 0])


def add_accoms():
    #Adding Accomodations to Roster Table
    csv_list = []

    with open("internal_data/roster.csv", 'r') as i:
        csvreader = csv.reader(i)
        csv_list = [row + ["0", "0", "N/A"] for row in csvreader][1:]

    for i in range(len(csv_list)):
        if type(csv_list[i]) != list:
            continue
        with open('internal_data/accom.csv', 'r') as in_file:
            accom_reader = csv.reader(in_file, delimiter=',')
            for read_accom_line in accom_reader:
                if read_accom_line[0].lower() == csv_list[i][3].lower():
                    csv_list[i][4] = "1" if read_accom_line[1:][0] == '1' else "0"
                    csv_list[i][5] = "1" if read_accom_line[1:][1] == '1' else "0"

    with open("internal_data/roster.csv", 'w', newline='') as o:
        csvwriter = csv.writer(o, delimiter=',')
        o.write("Student#,Last_Name,First_Name,NetID,Lefty,Questions,Seat\n")
        for i in csv_list:
            csvwriter.writerow(i)

def shuffle_roster():
    csv_list = []

    with open("internal_data/roster.csv", 'r') as i:
        csvreader = csv.reader(i)
        csv_list = [row for row in csvreader][1:]

    random.shuffle(csv_list)

    with open("internal_data/roster.csv", 'w', newline='') as o:
        csvwriter = csv.writer(o, delimiter=',')
        o.write("Student#,Last_Name,First_Name,NetID,Lefty,Questions,Seat\n")
        for i in csv_list:
            csvwriter.writerow(i)