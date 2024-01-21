from data_pipeline_module.class_room import ClassRoom
import pytest
from static_variables_module.physical_constaints import (
    MAX_SEATS,
    MIN_SEATS,
    MAX_ROOM_NUM,
    MIN_ROOM_NUM,
)


def test_classroom():
    """
    Test the ClassRoom class instantiation and attributes.

    This test function generates combinations of class numbers and available seats,
    then checks whether the ClassRoom class is instantiated correctly with valid
    inputs and whether appropriate exceptions are raised for invalid inputs.

    The test covers the following scenarios:
    - Instantiate ClassRoom with valid class number and available seats.
    - Verify that the class_number attribute is set correctly.
    - Verify that the available_seats attribute is set correctly.
    - Verify that the in_use attribute is initialized as False.
    - Verify that the in_use_by attribute is initialized as None.

    The test also checks for ValueError exceptions when attempting to instantiate
    ClassRoom with invalid class numbers or available seats outside the specified
    range (MIN_ROOM_NUM, MAX_ROOM_NUM, MIN_SEATS, MAX_SEATS).

    Raises:
        ValueError: If an attempt to instantiate ClassRoom with invalid inputs is not
                    caught and results in an instance creation.
    """
    test_class_numbers = [i for i in range(-50, 50)]
    test_class_available_seats = [i for i in range(-50, 50)]
    merged_combinations = [
        (i, j) for i in test_class_numbers for j in test_class_available_seats
    ]
    for class_number, available_seats in merged_combinations:
        if not (MIN_ROOM_NUM <= class_number <= MAX_ROOM_NUM) or not (
            MIN_SEATS <= available_seats <= MAX_SEATS
        ):
            with pytest.raises(ValueError):
                class_room_instance = ClassRoom(class_number, available_seats)
        else:
            class_room_instance = ClassRoom(class_number, available_seats)
            assert class_number == class_room_instance.class_number
            assert available_seats == class_room_instance.available_seats
            assert class_room_instance.in_use == False
            assert class_room_instance.in_use_by == None
