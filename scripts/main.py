import prep_roster as prep_roster
import prep_versions as prep_versions
import seat_allocator as seat_allocator
import generate_tex as generate_tex


import configparser
import sys
import random
import string
from pathlib import Path
import subprocess

config = configparser.ConfigParser()
config.read('config.ini')
vars = config['Display Variables']

names_on_exam = True if vars['names_on_exam'] == '1' else False
netid_on_exam = True if vars['netid_on_exam'] == '1' else False
number_id_on_exam = True if vars['number_id_on_exam'] == '1' else False
seat_number_on_exam = True if vars['seat_number_on_exam'] == '1' else False

vars = config['Allocator Variables']

lecture_hall = vars['lecture_hall'].lower().strip()
prioritize_lefty_seats = True if vars['prioritize_lefty_seats'] == '1' else False
prioritize_aisle_seats = True if vars['prioritize_aisle_seats'] == '1' else False

vars = config['Generator Variables']
reserves_per_version = int(vars['reserves_per_version'])

print()
input('Press Enter to Prepare Roster')
print()

print("Prepping Roster...")
prep_roster.make_roster_file()
print("--- Cleaning Up input Data...")
prep_roster.clean_accom_table(prioritize_lefty_seats, prioritize_aisle_seats)
print("--- Processing Accomodations...")
prep_roster.add_accoms()
print("--- Shuffling Roster for Randomized Assignment...")
prep_roster.shuffle_roster()
print("Roster Prepared!")



print()
input('Press Enter to Allocate Versions')
print()



print("Allocating Versions...")
prep_versions.prep_versions(lecture_hall)
print()
print("Versions Allocated!")



print()
input('Press Enter to Allocate Seats')
print()



print("Allocating Seats...")
alloc = seat_allocator.Allocator(lecture_hall)
alloc.allocate()
print()
print("Seats Allocated!")



print()
input('Press Enter to Generate Tex Files')
print()



random_dir = sys.argv[1]
print(f"Generating Exam Tex Files in: output/{random_dir} ...")
Path(f'./output/{random_dir}').mkdir(parents=True, exist_ok=True)
generate_tex.generate_tex(random_dir,
                          name=names_on_exam,
                          netid=netid_on_exam,
                          numid=number_id_on_exam,
                          seat=seat_number_on_exam)
print()
generate_tex.generate_reserves(random_dir, reserves_per_version)
print()
print("Tex Files Generated!")

print()