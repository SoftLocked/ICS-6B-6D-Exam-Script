import prep_roster

import configparser

config = configparser.ConfigParser()
config.read('config.ini')
vars = config['Variables']

names_on_exam = vars['names_on_exam']
netid_on_exam = vars['netid_on_exam']
number_id_on_exam = vars['number_id_on_exam']
seat_number_on_exam = vars['seat_number_on_exam']

print("Prepping Roster...")
prep_roster.make_roster_file()
print("--- Cleaning Up input Data...")
prep_roster.clean_accom_table()
print("--- Processing Accomodations...")
prep_roster.add_accoms()
print("--- Shuffling Roster for Randomized Assignment...")
prep_roster.shuffle_roster()
print("Roster Prepared!")

print()

print("Allocating Seats...")