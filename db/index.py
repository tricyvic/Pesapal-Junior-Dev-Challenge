# Indexes are hash maps
class Index:
    def __init__(self, column, primary_key):
        self.column = column
        self.primary_key = primary_key
        self.index = {}  # value -> set of primary keys

    def add(self, row):
        value = row[self.column]
        pk = row[self.primary_key]
        self.index.setdefault(value, set()).add(pk)

    def remove(self, row):
        value = row[self.column]
        pk = row[self.primary_key]
        self.index[value].remove(pk)
        if not self.index[value]:
            del self.index[value]

    def find(self, value):
        return self.index.get(value, set())

        