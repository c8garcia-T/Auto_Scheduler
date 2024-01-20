from main import ClassRoom
import pytest

MAX_SEATS = 32
MIN_SEATS = 12
MAX_ROOM_NUM = 12
MIN_ROOM_NUM = 0


def test_classroom():
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
