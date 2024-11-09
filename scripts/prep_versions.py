from pathlib import Path
import csv
from helpers import get_versions


def prep_versions(lecture_hall):
    csv_lines = []
    with open(f"seating_maps/{lecture_hall}.csv") as in_file:
        reader = csv.reader(in_file, delimiter=',')
        csv_lines = list(reader)
    
    versions = get_versions()

    if not versions:
        raise RuntimeError("No Versions Detected! Make sure there's a tex file for each version in exam_drop")

    csv_lines[1:].append('Version')

    for i in range(1, len(csv_lines)):
        print(f"--- Seat {i:<3} of {len(csv_lines)-1:<3} | {100*(i)/(len(csv_lines)-1):.2f}%", end='\r')
        ver = i%len(versions)
        csv_lines[i].append(versions[ver].stem)

    
    with open('internal_data/seating.csv', 'w', newline='') as out_file:
        writer = csv.writer(out_file, delimiter=',')
        writer.writerows(csv_lines)