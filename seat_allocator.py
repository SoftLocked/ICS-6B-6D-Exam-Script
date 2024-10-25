import json
import csv
import random
import string

ver_a_lefty = []
ver_b_lefty = []
ver_c_lefty = []

# Righty Seats
ver_a_righty = []
ver_b_righty = []
ver_c_righty = []

with open('./seats/hslh100a.json', 'r') as file:
    data = json.load(file)

    def load_data(version, handedness):
        match (version, handedness):
            case ("A", "R"):
                global ver_a_righty
                data_list = ver_a_righty
            case ("A", "L"):
                global ver_a_lefty
                data_list = ver_a_lefty
            case ("B", "R"):
                global ver_b_righty
                data_list = ver_b_righty
            case ("B", "L"):
                global ver_b_lefty
                data_list = ver_b_lefty
            case ("C", "R"):
                global ver_c_righty
                data_list = ver_c_righty
            case ("C", "L"):
                global ver_c_lefty
                data_list = ver_c_lefty
            case _:
                raise ValueError("Version or Handedness Invalid")
        global data
        for k,v in data[f"ver_{version.lower()}"]["righty" if handedness == "R" else "lefty"].items():
            for i in range(len(v)):
                data_list.append(f"{k}{v[i]}")

    load_data("A", "R")
    load_data("A", "L")
    load_data("B", "R")
    load_data("B", "L")
    load_data("C", "R")
    load_data("C", "L")

seats = ver_a_lefty, ver_b_lefty, ver_c_lefty, ver_a_righty, ver_b_righty, ver_c_righty

def allocate(data, version, lefty):
    for seat_idx, seat in enumerate(data):
        with open(f'./exams/versions/{version}.tex', 'r') as i:
            f_name, f_netid, f_seat = False, False, False
            with open(f'./exams/tex_exams/{"lefty" if lefty else "righty"}-{"A" if seat[:1] == "A" else "B-end"}-{''.join(random.choices(string.ascii_letters, k=5))}-ver{version}-{seat}.tex', 'w') as o:
                for line_idx, line in enumerate(i):
                    new_line = line
                    if "STUDENT_NAME" in line:
                        if f_name:
                            raise ValueError(f"Too many instances of STUDENT_NAME (line: {line_idx})")
                        f_name = True

                        new_line = line.replace("STUDENT_NAME", '')
                    if "STUDENT_NETID" in line:
                        if f_netid:
                            raise ValueError(f"Too many instances of STUDENT_NETID (line: {line_idx})")
                        f_netid = True
                        new_line = line.replace("STUDENT_NETID", '')
                    if "SEAT_NUMBER" in line:
                        if f_seat:
                            raise ValueError(f"Too many instances of SEAT_NUMBER (line: {line_idx})")
                        f_seat = True
                        new_line = line.replace("SEAT_NUMBER", f'{r'\textit{' + seat + '}' if lefty else seat}')
                    o.write(new_line)
            if not f_name:
                raise ValueError(f"Missing instance of STUDENT_NAME")
            if not f_netid:
                raise ValueError(f"Missing instance of STUDENT_NETID")
            if not f_seat:
                raise ValueError(f"Missing instance of SEAT_NUMBER")

allocate(ver_a_lefty, "A", True)
allocate(ver_b_lefty, "B", True)
allocate(ver_c_lefty, "C", True)
allocate(ver_a_righty, "A", False)
allocate(ver_b_righty, "B", False)
allocate(ver_c_righty, "C", False)