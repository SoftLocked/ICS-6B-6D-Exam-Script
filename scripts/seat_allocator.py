import csv
from helpers import Student, Seat


class Allocator:
    def __init__(self,
                 lecture_hall,
                 deprior_front = True,
                 prior_lefty = True,
                 prior_aisle = True):
        self.lecture_hall = lecture_hall
        self.deprior_front = True
        self.prior_lefty = True
        self.prior_aisle = True
        self.allocated_set = set()

    def _assign_seat(self, netid, seat):
        '''
        Assigns a Seat to Some Student Based on netid
        '''
        csv_lines = []
        with open('internal_data/roster.csv', 'r') as in_file:
            reader = csv.reader(in_file, delimiter=',')
            csv_lines = [Student(v) if i != 0 else v for i,v in enumerate(list(reader))]
        for line in csv_lines[1:]:
            if line.netid == netid.lower():
                line.seat = seat
                break
        with open('internal_data/roster.csv', 'w', newline='') as out_file:
            writer = csv.writer(out_file, delimiter=',')
            writer.writerow(csv_lines[0])
            for line in csv_lines[1:]:
                writer.writerow(line.make_list())
        self.allocated_set.add(seat)
    
    def allocate(self):
        students = []
        with open('internal_data/roster.csv', 'r') as in_file:
            reader = csv.reader(in_file, delimiter=',')
            students = [Student(i) for i in list(reader)[1:]]
        seats = []
        with open(f'seating_maps/{self.lecture_hall}.csv', 'r') as in_file:
            reader = csv.reader(in_file, delimiter=',')
            seats = [Seat(i) for i in list(reader)[1:]]
        
        if len(students) > len(seats):
            raise RuntimeError(f"Lecture hall too small! {len(seats)} seats for {len(students)} students")

        self.allocated_set = set()

        for student_idx, student in enumerate(students):
            if student.seat != "N/A":
                continue
            
            print(f"--- Student {student_idx+1:<3} of {len(students):<3} | {100*(student_idx+1)/len(students):.2f}%", end='\r')

            # First pass...
            #   Skips First Row
            #   Assigns lefties to lefty seats
            #   Assigns question askers to aisle seats
            #   Assigns non-lefty non-question-askers non-aisle or lefty seats
            for seat in seats:
                if seat.seat_string in self.allocated_set:
                    continue

                if seat.front: # If the seat is front row, skip it for now
                    continue

                if student.lefty: # If lefty, find a lefty seat
                    if not seat.lefty:
                        continue
                    student.seat = seat.seat_string
                    self._assign_seat(student.netid, seat.seat_string)
                    break
                elif student.questions: # If not lefty but question asker, then find non-lefty aisle seat
                    if not seat.aisle:
                        continue
                    if seat.lefty:
                        continue
                    student.seat = seat.seat_string
                    self._assign_seat(student.netid, seat.seat_string)
                    break
                else: # If neither, then assign 
                    if seat.aisle or seat.lefty:
                        continue
                    student.seat = seat.seat_string
                    self._assign_seat(student.netid, seat.seat_string)
                    break

            if student.seat != "N/A":
                continue         
            
            # Second pass...
            # Assign any non-aisle seat to whoever's left
            for seat in seats:
                if seat.seat_string in self.allocated_set:
                    continue

                if seat.front: # If the seat is front row, skip it for now
                    continue
                if seat.aisle:
                    continue

                student.seat = seat.seat_string
                self._assign_seat(student.netid, seat.seat_string)
                break
            
            if student.seat != "N/A":
                continue

            # Third pass...
            # Assign any non-front row seat to whoever's left
            for seat in seats:
                if seat.seat_string in self.allocated_set:
                    continue

                if seat.front: # If the seat is front row, skip it for now
                    continue
                
                student.seat = seat.seat_string
                self._assign_seat(student.netid, seat.seat_string)
                break
            
            if student.seat != "N/A":
                continue

            # Fourth pass...
            # Assign any front row seat to whoever's left
            for seat in seats:
                if seat.seat_string in self.allocated_set:
                    continue

                student.seat = seat.seat_string
                self._assign_seat(student.netid, seat.seat_string)
                break