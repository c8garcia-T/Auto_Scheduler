from static_variables_module.physical_constaints import (
    MAX_SEATS,
    MIN_SEATS,
    MAX_ROOM_NUM,
    MIN_ROOM_NUM,
)


class ClassRoom:
    # Safety Check User Input Later
    def __init__(self, class_number: int, available_seats: int):
        # Input Validation for class_number
        if not isinstance(class_number, int):
            raise ValueError("class_number must be an integer")
        if (class_number < MIN_ROOM_NUM) | (class_number > MAX_ROOM_NUM):
            raise ValueError("class_number does not exist")

        # Input Validation for available_seats
        if not isinstance(available_seats, int):
            raise ValueError("available_seats must be an integer")
        if (available_seats < MIN_SEATS) | (available_seats > MAX_SEATS):
            raise ValueError("available_seats is out of bounds")
        # Inputs
        self.class_number = class_number
        self.available_seats = available_seats
        # Alorithm Manipulated Variables
        self.in_use = False
        self.in_use_by = None
