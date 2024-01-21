class Course:
    def __init__(
        self,
        catalog,
        class_time: int,
        class_size: int,
        base_group: list,
        course_name: str,
        teacher: str,
        sound_level: float = None,
        preference_classroom_number=None,
        preference_seperation=False,
        days_thought: list = [],
    ):
        # Inputs
        self.class_time = class_time
        self.class_size = class_size
        self.base_group = base_group
        self.course_name = course_name
        self.teacher = teacher
        self.sound_level = sound_level
        self.preference_classroom_number = preference_classroom_number
        self.preference_seperation = preference_seperation
        self.days_thought = days_thought
        # Alorithm Manipulated Variables
        self.located_in_room = None
        self.next_course = None
        self.primary_key = self.course_name + self.teacher
        # Catalog Reference
        self.catalog = catalog
        self.catalog.courses_offered.append(self)

    def view_course_info(self):
        print(f"Course:{self.course_name} ({self.class_size } Students)")
