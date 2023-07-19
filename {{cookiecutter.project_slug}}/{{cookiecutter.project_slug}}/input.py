import time

from {{cookiecutter.project_slug}}.config import get_settings

import pathway as pw


class InfiniteStream(pw.io.python.ConnectorSubject):
    def run(self):
        while True:
            self.next_json({"value": 1})
            time.sleep(0.100)


def input():
    class InputSchema(pw.Schema):
        value: int

    format="json"

    if get_settings().input_connector == "{{cookiecutter.prod_input}}":
        rdkafka_settings = {
            "bootstrap.servers": get_settings().{{cookiecutter.prod_input}}_bootstrap_servers,
            "security.protocol": "plaintext",
            "group.id": get_settings().{{cookiecutter.prod_input}}_group_id,
            "session.timeout.ms": get_settings().{{cookiecutter.prod_input}}_session_timeout_ms,
        }
        return pw.io.{{cookiecutter.prod_input}}.read(
            rdkafka_settings,
            topic=get_settings().{{cookiecutter.prod_input}}_topic,
            schema=InputSchema,
            format=format,
            autocommit_duration_ms=get_settings().autocommit_duration_ms,
        )
    elif get_settings().input_connector == "python":
        return pw.io.python.read(
            InfiniteStream(),
            schema=InputSchema,
            format=format,
            autocommit_duration_ms=get_settings().autocommit_duration_ms,
        )
