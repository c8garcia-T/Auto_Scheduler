class ClassRoom:
    # Safety Check User Input Later
    def __init__(self, class_number:int,available_seats:int):
        # Input Validation for class_number
        if not isinstance(class_number, int):
            raise ValueError("class_number must be an integer")
        if (class_number < 0) |  (class_number > 12) :
            raise ValueError("class_number does not exist")

        # Input Validation for available_seats
        if not isinstance(available_seats, int):
            raise ValueError("available_seats must be an integer")
        if (available_seats < 12 )| (available_seats > 32):
            raise ValueError("available_seats is out of bounds")
        self.class_number = class_number
        self.available_seats = available_seats
        self.in_use = False
        self.in_use_by = None


class Course:
    def __init__(self, course_name:str,class_size:int, preference_classroom_number=None,preference_seperation=None,preference_neighbor=None):
        self.course_name = course_name
        self.class_size = class_size
        self.preference_classroom_number = preference_classroom_number
        self.preference_seperation = preference_seperation
        self.preference_neighbor = preference_neighbor
        self.located_in_room = None
    def view_course_info(self):
        print(f'Course:{self.course_name} ({self.class_size } Students)')


class ClassroomAssignmentAlgorithm:
    def __init__(self):
        self.class_rooms =  None
        self.courses = None
    def sort_class_rooms(self):
        if self.class_rooms:
            self.sort_class_rooms.sort(key=lambda x:x.available_seats, reverse=True)
        else:
            raise ValueError('No Classrooms Exist')
    def run_algorithm(self):
        for course in self.courses:
            available_rooms = [i for i in self.class_rooms if not i.in_use]
            for room in available_rooms:
                if course.class_size > room.available_seats:
                    pass
                else:
                    # process
                    room.in_use_by = course.course_name
                    room.in_use = True
                    course.located_in_room = room.class_number
        if len(self.class_rooms) != len([i for i in self.class_rooms if not i.in_use]):
            print('Could Not Properly Assign Classrooms!')


