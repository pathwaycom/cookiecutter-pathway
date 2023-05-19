import pathway as pw


def output(output_table):
    pw.io.csv.write(output_table, "output.csv")
