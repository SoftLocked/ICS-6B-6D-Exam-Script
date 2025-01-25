from helpers import Student, Seat, get_versions
from pathlib import Path
import random
import string
import csv

def get_seats(search_func=lambda x: True):
        '''
        Query to Get Seats Based on search_func
        '''
        csv_lines = []
        with open(f'internal_data/seating.csv', 'r') as in_file:
            reader = csv.reader(in_file, delimiter=',')
            for line in reader:
                line = Seat(line)
                if search_func(line):
                    csv_lines.append(line)
        return csv_lines

def generate_tex(random_dir, name, netid, numid, seat):
    students = []
    with open('internal_data/roster.csv', 'r') as in_file:
        reader = csv.reader(in_file, delimiter=',')
        students = [Student(i) for i in list(reader)[1:]]
    
    versions = get_versions()

    for i, student in enumerate(students):

        print(f"--- Student {i+1:<3} of {len(students):<3} | {100*(i+1)/len(students):.2f}%", end='\r')

        version = versions[i%len(versions)].stem

        seat = get_seats(lambda x: x.seat_string == student.seat)[0]

        random_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))

        file_name = f"{'lefty' if seat.lefty else 'righty'}-{'front' if seat.front else 'notfront'}-{random_str}-{seat.seat_string}"

        with open(f'exam_drop/{version}.tex', encoding='utf-8') as in_file:
            with open(f'output/{random_dir}/{file_name}.tex', 'w', encoding='utf-8') as out_file:
                for line in in_file:
                    if 'STUDENT_NAME' in line:
                        if name:
                            line = line.replace('STUDENT_NAME', f'{student.first_name} {student.last_name}')
                        else:
                            pass
                            # line = line.replace('STUDENT_NAME', '')

                    if 'STUDENT_NETID' in line:
                        if netid:
                            line = line.replace('STUDENT_NETID', f'{student.netid}')
                        else:
                            pass
                            # line = line.replace('STUDENT_NETID', '')
                    
                    if 'STUDENT_NUMID' in line:
                        if numid:
                            line = line.replace('STUDENT_NUMID', f'{student.num_id}')
                        else:
                            pass
                            # line = line.replace('STUDENT_NUMID', '')
                    
                    if 'SEAT_NUMBER' in line:
                        if seat:
                            line = line.replace('SEAT_NUMBER', f'{student.seat}')
                        else:
                            pass
                            # line = line.replace('SEAT_NUMBER', '')

                    out_file.write(line)

def generate_reserves(directory, reserves_per_version):

    versions = get_versions()

    for i, version in enumerate(versions):
        version = version.stem
        for j in range(reserves_per_version):

            print(f"--- Reserve {(i+1)*(j+1):<3} of {reserves_per_version*len(versions):<3} | {100*((i+1)*(j+1))/(reserves_per_version*len(versions)):.2f}%", end='\r')

            with open(f'exam_drop/{version}.tex', encoding='utf-8') as in_file:
                with open(f'output/{directory}/Z_Reserve_{j}_ver{version}.tex', 'w', encoding='utf-8') as out_file:
                    for line in in_file:
                        if 'STUDENT_NAME' in line:
                            line = line.replace('STUDENT_NAME', '')

                        if 'STUDENT_NETID' in line:
                            line = line.replace('STUDENT_NETID', '')
                        
                        if 'STUDENT_NUMID' in line:
                            line = line.replace('STUDENT_NUMID', '')
                        
                        if 'SEAT_NUMBER' in line:
                            line = line.replace('SEAT_NUMBER', '')

                        out_file.write(line)