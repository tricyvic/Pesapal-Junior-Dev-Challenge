# Indexes are hash maps
class Index:
    def __init__(self,colunm):
        self.colunm = colunm
        self.index = {} # value -> set of primary keys

    def add(self, row):
        value = row[self.column]
        self.index.setdefault(value, set()).add(row["id"])

    def remove(self, row):
        value = row[self.column]
        self.index[value].remove(row["id"])
        if not self.index[value]:
            del self.index[value]

    def find(self, value):
        return self.index.get(value, set())
        