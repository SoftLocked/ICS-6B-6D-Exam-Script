import prep_roster
import prep_versions
import seat_allocator as seat_allocator

import configparser
import sys

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

print("Allocating Versions...")
prep_versions.prep_versions(lecture_hall)
print()
print("Versions Allocated!")

print()

print("Allocating Seats...")
alloc = seat_allocator.Allocator(lecture_hall)
alloc.allocate()
print()
print("Seats Allocated!")


