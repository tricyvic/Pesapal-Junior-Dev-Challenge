import re

def parse(sql):
    sql = sql.strip().rstrip(";")

    if sql.upper().startswith("CREATE TABLE"):
        return parse_create(sql)

    if sql.upper().startswith("INSERT INTO"):
        return parse_insert(sql)

    if sql.upper().startswith("SELECT"):
        return parse_select(sql)

    raise ValueError("Unsupported SQL command")


def parse_create(sql):
    match = re.match(r"CREATE TABLE (\w+)\s*\((.+)\)", sql, re.I)
    table_name, columns_def = match.groups()

    columns = {}
    primary_key = None
    unique_columns = set()

    for col in columns_def.split(","):
        parts = col.strip().split()
        col_name = parts[0]
        col_type = parts[1]

        columns[col_name] = col_type

        if "PRIMARY" in parts:
            primary_key = col_name
        if "UNIQUE" in parts:
            unique_columns.add(col_name)

    return ("CREATE", table_name, columns, primary_key, unique_columns)


def parse_insert(sql):
    match = re.match(r"INSERT INTO (\w+) VALUES \((.+)\)", sql, re.I)
    table_name, values = match.groups()

    values = [v.strip().strip("'") for v in values.split(",")]
    return ("INSERT", table_name, values)


def parse_select(sql):
    match = re.match(r"SELECT \* FROM (\w+)(?: WHERE (\w+)=(.+))?", sql, re.I)
    table, col, val = match.groups()

    if val:
        val = val.strip().strip("'")

    return ("SELECT", table, col, val)
