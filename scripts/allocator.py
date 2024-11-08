import csv

class Allocator:
    def __init__(self,
                 lectue_hall,
                 deprior_front = True,
                 prior_lefty = True,
                 prior_aisle = True):
        self.lecture_hall = lectue_hall
        self.deprior_front = True
        self.prior_lefty = True
        self.prior_aisle = True
    
    def _get_seats(self, search_func=lambda x: True):
        '''
        Query to Get Seats Based on search_func
        '''
        csv_lines = []
        with open(f'seating_maps/{self.lecture_hall}.csv', 'r') as in_file:
            reader = csv.reader(in_file, delimiter=',')
            for line in reader:
                if search_func(line):
                    csv_lines.append(line)
        return csv_lines

    def _assign_seat(self, netid, seat):
        '''
        Assigns a Seat to Some Student Based on netid
        '''
        csv_lines = []
        with open('roster/roster.csv', 'r') as in_file:
            reader = csv.reader(in_file, delimiter=',')
            csv_lines = list(reader)
        for line in csv_lines:
            if line[3].lower() == netid.lower():
                line[6] = seat
                print(line)
                break
        with open('roster/roster.csv', 'w') as out_file:
            writer = csv.writer(out_file, delimiter=',')
            writer.writerows(csv_lines)
    
    def allocate(self):
        students = []
        with open('roster/roster.csv', 'r') as in_file:
            reader = csv.reader(in_file, delimiter=',')
            students = list(reader)
        seats = []
        with open(f'seating_maps/{self.lecture_hall}.csv', 'r') as in_file:
            reader = csv.reader(in_file, delimiter=',')
            seats = list(reader)
        
        allocated_seats = set()

        for student in students:
            lefty = True if student[4] == '1' else False
            questions = True if student[5] == '1' else False
            for seat in seats:
                