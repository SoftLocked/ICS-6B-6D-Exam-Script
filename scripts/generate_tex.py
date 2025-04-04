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

        seat_char = chr(int(seat.seat_number)-1 + 65) if int(seat.seat_number) < 100 else chr(int(seat.seat_number)-101 + 65)

        file_name = f"{seat.section}-{seat.seat_letter}-{seat_char}-{seat.lefty}-{seat.aisle}-{seat.front}"

        with open(f'exam_drop/{version}.tex', encoding='utf-8') as in_file:
            with open(f'output/{random_dir}/{file_name}.tex', 'w', encoding='utf-8') as out_file:
                for line in in_file:
                    if 'STUDENTNAME' in line:
                        if name:
                            line = line.replace('STUDENTNAME', f'{student.first_name} {student.last_name}')
                        else:
                            pass
                            # line = line.replace('STUDENT_NAME', '')

                    if 'STUDENTNETID' in line:
                        if netid:
                            line = line.replace('STUDENTNETID', f'{student.netid}')
                        else:
                            pass
                            # line = line.replace('STUDENT_NETID', '')
                    
                    if 'STUDENTNUMBERID' in line:
                        if numid:
                            line = line.replace('STUDENTNUMBERID', f'{student.num_id}')
                        else:
                            pass
                            # line = line.replace('STUDENT_NUMID', '')
                    
                    if 'SEATNUMBER' in line:
                        if seat:
                            line = line.replace('SEATNUMBER', f'{student.seat}')
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
                        if 'STUDENTNAME' in line:
                            line = line.replace('STUDENTNAME', '')

                        if 'STUDENTNETID' in line:
                            line = line.replace('STUDENTNETID', '')
                        
                        if 'STUDENTNUMBERID' in line:
                            line = line.replace('STUDENTNUMBERID', '')
                        
                        if 'SEATNUMBER' in line:
                            line = line.replace('SEATNUMBER', '')

                        out_file.write(line)