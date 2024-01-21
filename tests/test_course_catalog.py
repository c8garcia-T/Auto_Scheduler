from data_pipeline_module.course_catalog import (
    CourseCatalog,
    dataframe_course_catalog_from_excel,
)


def test_course_catalog():
    test_catalog_instance = CourseCatalog()
    assert not test_catalog_instance.courses_offered


def test_dataframe_course_catalog_from_excel():
    # Make Later
    pass


def test_build_course_catalog():
    # Make Later
    pass
