from {{cookiecutter.project_slug}}.config import get_settings
from {{cookiecutter.project_slug}}.input import input
from {{cookiecutter.project_slug}}.output import output
from {{cookiecutter.project_slug}}.pipeline import pipeline

import pathway as pw

if __name__ == "__main__":
    get_settings()

    input_table = input()
    output_table = pipeline(input_table)
    output(output_table)

    pw.run(stats_monitoring_level=pw.StatsMonitoringLevel.ALL)
