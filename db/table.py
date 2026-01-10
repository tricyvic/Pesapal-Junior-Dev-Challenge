class Table:
    def __init__(self,name, columns, primary_key, unique_columns):
        self.name = name
        self.columns = columns              
        self.primary_key = primary_key
        self.unique_columns = unique_columns
        self.rows = {}                      
        self.indexes = {} 
    
    def insert(self, row):
        pk = row[self.primary_key]

        if pk in self.rows:
            raise ValueError("Primary key already exists")

        for col in self.unique_columns:
            for existing in self.rows.values():
                if existing[col] == row[col]:
                    raise ValueError(f"Unique constraint violated on {col}")

        # insert row
        self.rows[pk] = row

        # update indexes
        for index in self.indexes.values():
            index.add(row)
        
    
    def select_all(self):
        return list(self.rows.values())