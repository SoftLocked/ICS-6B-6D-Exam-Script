from dataclasses import Student
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
                if search_func(line):
                    csv_lines.append(line)
        return csv_lines

def generate_tex():
    random_dir = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    print(random_dir)

    students = []
    with open('internal_data/roster.csv', 'r') as in_file:
        reader = csv.reader(in_file, delimiter=',')
        students = [Student(i) for i in list(reader)[1:]]
    

    Path(f'./output/{random_dir}/a.tex').mkdir(parents=True, exist_ok=True)

    with open(f"output/{random_dir}/a.tex", 'w') as out_file:
        pass

generate_tex()