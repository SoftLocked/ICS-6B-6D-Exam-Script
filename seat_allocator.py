import json
import csv
import random

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
                if k != "A":
                    data_list.append(f"{k}{v[i]}")

    load_data("A", "R")
    load_data("A", "L")
    load_data("B", "R")
    load_data("B", "L")
    load_data("C", "R")
    load_data("C", "L")

seats = ver_a_lefty, ver_b_lefty, ver_c_lefty, ver_a_righty, ver_b_righty, ver_c_righty

with open('./roster/roster.csv') as i:
    csvreader = csv.reader(i)
    next(csvreader)

    for row in csvreader:
        id, last_name, first_name, netid, lefty = row
        lefty = True if lefty == "YES" else False

        version = None
        seat = None

        def allocate(data_list):
            choice = random.randint(0, len(data_list)-1)
            seat = data_list[choice]
            data_list.pop(choice)
            return seat

        if lefty:
            if ver_a_lefty:
                version, seat =  "A", allocate(ver_a_lefty,)
            elif ver_b_lefty:
                version, seat = "B", allocate(ver_b_lefty)
            elif ver_c_lefty:
                version, seat = "C", allocate(ver_c_lefty)
            else:
                if ver_a_righty:
                    version, seat = "A", allocate(ver_a_righty)
                elif ver_b_righty:
                    version, seat = "B", allocate(ver_b_righty)
                elif ver_c_righty:
                    version, seat = "C", allocate(ver_c_righty)
        else:
            if ver_a_righty:
                version, seat = "A", allocate(ver_a_righty)
            elif ver_b_righty:
                version, seat = "B", allocate(ver_b_righty)
            elif ver_c_righty:
                version, seat = "C", allocate(ver_c_righty)

        seat_number = int(seat[1:])
        row_number = seat[:1]

        if seat_number > 100:
            section = "middle"
        else:
            if seat_number % 2:
                section = "right"
            else:
                section = "left"

        with open(f'./exams/versions/{version}.tex', 'r') as i:
            f_name, f_netid, f_seat = False, False, False
            with open(f'./exams/tex_exams/{section}-{row_number.lower()}-{seat_number}-ver_{version.lower()}-{"righty" if not lefty else "lefty"}.tex', 'w') as o:
                for idx, line in enumerate(i):
                    new_line = line
                    if "STUDENT_NAME" in line:
                        if f_name:
                            raise ValueError(f"Too many instances of STUDENT_NAME (line: {idx})")
                        f_name = True

                        new_line = line.replace("STUDENT_NAME", f'{first_name.title()} {last_name.title()}')
                    if "STUDENT_NETID" in line:
                        if f_netid:
                            raise ValueError(f"Too many instances of STUDENT_NETID (line: {idx})")
                        f_netid = True
                        new_line = line.replace("STUDENT_NETID", f'{netid.lower()}')
                    if "SEAT_NUMBER" in line:
                        if f_seat:
                            raise ValueError(f"Too many instances of SEAT_NUMBER (line: {idx})")
                        f_seat = True
                        new_line = line.replace("SEAT_NUMBER", f'{seat}')
                    o.write(new_line)
            if not f_name:
                raise ValueError(f"Missing instance of STUDENT_NAME (line: {idx})")
            if not f_netid:
                raise ValueError(f"Missing instance of STUDENT_NETID (line: {idx})")
            if not f_seat:
                raise ValueError(f"Missing instance of SEAT_NUMBER (line: {idx})")