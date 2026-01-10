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
        
        if command[0] == "SELECT_JOIN":
            # parse example:
            # SELECT * FROM orders JOIN users ON orders.user_id = users.id
            table1 = self.tables[command[1]]
            table2 = self.tables[command[2]]
            col1 = command[3]  # orders.user_id
            col2 = command[4]  # users.id

            results = []
            for row1 in table1.rows.values():
                for row2 in table2.rows.values():
                    if row1[col1.split(".")[1]] == row2[col2.split(".")[1]]:
                        combined = {**row1, **row2}
                        results.append(combined)
            return results

