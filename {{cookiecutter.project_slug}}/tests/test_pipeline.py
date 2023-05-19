from {{cookiecutter.project_slug}}.pipeline import pipeline

from pathway.tests.utils import T, assert_table_equality_wo_index


def test_pipeline():
    input_table = T(
        """
            | value
        1   | 1
        2   | 2
        3   | 3
    """
    )
    output_table = pipeline(input_table)
    assert_table_equality_wo_index(
        output_table,
        T(
            """
        sum
            6
    """,
        ),
    )
