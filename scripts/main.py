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
prep_roster.clean_accom_table()
prep_roster.add_accoms()
prep_roster.shuffle_roster()
