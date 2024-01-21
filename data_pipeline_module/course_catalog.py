import pandas as pd
import numpy as np
from static_variables_module.physical_constaints import (
    MIN_SEATS,
    MAX_SEATS,
    MAX_ROOM_NUM,
    MIN_ROOM_NUM,
)
from data_pipeline_module.course import Course


class CourseCatalog:
    def __init__(self):
        # Holds Course Class Instances
        self.courses_offered = []


def dataframe_course_catalog_from_excel(excel_path="data/Example Schedule Inputs.xlsx"):
    data = pd.read_excel(excel_path, sheet_name=1, header=0, usecols="A:I")
    if not all(data.iloc[:, [0, 1]].dtypes == "int64"):
        raise ValueError(f"Wrong Data Type Present {data.iloc[:,[0, 1]].columns}")
    if not all(data.iloc[:, [5, 6, -2]].dtypes == "float64"):
        raise ValueError(f"Wrong Data Type Present {data.iloc[:,[5,6]].columns}")
    if not all(data.iloc[:, [2, 3, 4, -1]].dtypes == "object"):
        raise ValueError(
            f"Wrong Data Type Present {data.iloc[:,[2, 3, 4, -1]].columns}"
        )
    if data.iloc[:, 0:3].isna().sum().sum() > 0:
        raise ValueError(f"Critical Input Missing {data.iloc[:,0:3].columns}")
    data.sort_values(by=[data.iloc[:, 0].name], inplace=True)
    courses_by_time_slots = [
        (clas_time, group_df)
        for clas_time, group_df in data.groupby(data.iloc[:, 0].name)
    ]

    return courses_by_time_slots


def build_course_catalog(courses_by_time_slots: list):
    course_catalog_instance = CourseCatalog()
    for class_time, course_list in courses_by_time_slots:
        if not course_list.iloc[:, 2].nunique() == course_list.shape[0]:
            raise ValueError(
                f"Duplicate Entries For Column: {course_list.iloc[:,2].name} at time {class_time}"
            )
        if any(course_list.iloc[:, 1] < 1) or any(course_list.iloc[:, 1] > MAX_SEATS):
            raise ValueError(f"Class Size Input is Out of Bounds")
    for class_time, course_list in courses_by_time_slots:
        # Process
        # for courses_at_time_t in course_list.itertuples():
        #     # Process
        #     course_instance = Course(
        #     course_catalog_instance,
        #     class_time=class_time,
        #     class_size=courses_at_time_t[],
        #     # base_group=[course_info[0], course_info[1]],
        #     # course_name=,
        #     # teacher=f,
        # )
        pass


build_course_catalog(dataframe_course_catalog_from_excel())
# print(len(dataframe_course_catalog_from_excel()))
# data_in = dataframe_course_catalog_from_excel()
# print(build_course_catalog(data_in))
