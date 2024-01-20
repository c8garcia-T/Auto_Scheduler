from main import CourseCatalog, Course
import pandas as pd
import pytest


@pytest.fixture
def random_course_data():
    data = pd.DataFrame()
    return data


def test_course(random_course_data):
    test_catalog = CourseCatalog()
    for row in random_course_data.itertuples():
        pass
