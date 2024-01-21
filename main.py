class ClassroomAssignmentAlgorithm:
    def helper_func():
        pass

    def __init__(self):
        self.class_rooms = None
        self.courses = None

    def sort_class_rooms(self):
        if self.class_rooms:
            self.sort_class_rooms.sort(key=lambda x: x.available_seats, reverse=True)
        else:
            raise ValueError("No Classrooms Exist")

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
            print("Could Not Properly Assign Classrooms!")
