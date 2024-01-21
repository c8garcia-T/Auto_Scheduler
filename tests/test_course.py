from data_pipeline_module.course import Course
from data_pipeline_module.course_catalog import CourseCatalog
import pytest
from static_variables_module.physical_constaints import (
    MAX_SEATS,
    MAX_ROOM_NUM,
)
import random

random.seed = 24


@pytest.fixture
def courses_at_time_t_data():
    base_groups = [f"bg_{i}" for i in range(0, 50)]
    allowed_class_sizes = [i for i in range(1, MAX_SEATS + 1)]
    possible_base_groups = [
        (base_group, None, class_size)
        for base_group in base_groups
        for class_size in allowed_class_sizes
    ]
    possible_base_group_combinations = [
        (base_group_1, base_group_2, class_size_1 + class_size_2)
        for base_group_1, _, class_size_1 in possible_base_groups
        for base_group_2, _, class_size_2 in possible_base_groups
        if (
            (base_group_1 != base_group_2)
            and ((class_size_1 + class_size_2) <= MAX_SEATS)
        )
    ]

    merged_possible_base_groups = (
        possible_base_group_combinations + possible_base_groups
    )
    random.shuffle(merged_possible_base_groups)

    base_groups_used = set()
    unique_base_group_combinations = []
    while (
        (len(base_groups_used) != len(base_groups))
        or (len(merged_possible_base_groups) == 0)
    ) and (len(unique_base_group_combinations) < MAX_ROOM_NUM):
        for base_group_1, base_group_2, class_size in merged_possible_base_groups:
            if (
                (base_group_1 not in base_groups_used)
                and ((base_group_2 not in base_groups_used) or (base_group_2 == None))
                and (len(unique_base_group_combinations) < MAX_ROOM_NUM)
            ):
                if base_group_2 == None:
                    unique_base_group_combinations.append(
                        (base_group_1, base_group_2, class_size)
                    )
                    base_groups_used.add(base_group_1)
                else:
                    unique_base_group_combinations.append(
                        (base_group_1, base_group_2, class_size)
                    )
                    base_groups_used.update({base_group_1, base_group_2})
            else:
                _ = merged_possible_base_groups.pop()
    return unique_base_group_combinations


def test_create_courses_data(courses_at_time_t_data):
    test_catalog_instance = CourseCatalog()
    for indx, course_info in enumerate(courses_at_time_t_data):
        test_course_instance = Course(
            test_catalog_instance,
            class_time=12,
            class_size=course_info[2],
            base_group=[course_info[0], course_info[1]],
            course_name=f"course_test{indx}",
            teacher=f"teacher_test{indx}",
        )
    for course_instance, test_course_data in zip(
        test_catalog_instance.courses_offered, courses_at_time_t_data
    ):
        assert course_instance.class_size == test_course_data[2]
        assert course_instance.base_group == [test_course_data[0], test_course_data[1]]
    assert len(courses_at_time_t_data) == len(test_catalog_instance.courses_offered)
