from data_pipeline_module.course_catalog import CourseCatalog


def test_course_catalog():
    test_catalog_instance = CourseCatalog()
    assert not test_catalog_instance.courses_offered
