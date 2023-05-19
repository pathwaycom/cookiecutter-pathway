import pathway as pw


def pipeline(input_table: pw.Table) -> pw.Table:
    """Your custom logic."""

    # Example app: sum all the values on the stream
    output_table = input_table.reduce(sum=pw.reducers.sum(input_table.value))

    return output_table
