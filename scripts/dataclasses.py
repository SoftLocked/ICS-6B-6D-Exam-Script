
class Student:
    '''
    Student Data Class
    '''
    def __init__(self, student):
        self.num_id = student[0]
        self.last_name = student[1].title()
        self.first_name = student[2].title()
        self.netid = student[3].lower()
        self.lefty = True if student[4] == '1' else False
        self.questions = True if student[5] == '1' else False
        self.seat = student[6]
    
    def make_list(self):
        return [
            self.num_id,
            self.last_name,
            self.first_name,
            self.netid,
            '1' if self.lefty else '0',
            '1' if self.questions else '0',
            self.seat
        ]


class Seat:
    '''
    Seat Data Class
    '''
    def __init__(self, seat):
        self.seat_letter = seat[0]
        self.seat_number = seat[1]
        self.seat_string = ''.join([self.seat_letter, self.seat_number])
        self.section = seat[2]
        self.lefty = True if seat[3] == '1' else False
        self.aisle = True if seat[4] == '1' else False
        self.front = True if seat[5] == '1' else False

    def make_list(self):
        return [
            self.seat_letter,
            self.seat_number,
            self.section,
            '1' if self.lefty else '0',
            '1' if self.aisle else '0',
            '1' if self.front else '0'
        ]
