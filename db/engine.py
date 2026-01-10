from db.table import Table
from db.index import Index
from db.parser import parse

class Database:
    def __init__(self):
        self.tables = {}

    def execute(self, sql):
        command = parse(sql)

        if command[0] == "CREATE":
            _, name, columns, pk, unique = command
            table = Table(name, columns, pk, unique)

            # auto-create indexes for unique columns
            for col in unique:
                table.indexes[col] = Index(col, pk)


            self.tables[name] = table
            return f"Table '{name}' created"

        if command[0] == "INSERT":
            _, name, values = command
            table = self.tables[name]

            row = dict(zip(table.columns.keys(), values))
            # cast INT
            for col, typ in table.columns.items():
                if typ == "INT":
                    row[col] = int(row[col])

            table.insert(row)
            return "Row inserted"

        if command[0] == "SELECT":
            _, name, col, val = command
            table = self.tables[name]

            if col is None:
                return table.select_all()

            # indexed lookup
            if col in table.indexes:
                pks = table.indexes[col].find(val)
                return [table.rows[pk] for pk in pks]

            return [r for r in table.rows.values() if r[col] == val]
