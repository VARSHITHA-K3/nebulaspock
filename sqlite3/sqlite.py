import sqlite3

class Database:
    def __init__(self, db_name):
        self.name = db_name
        self.conn = sqlite3.connect('Nebula.db')
        self.conn.row_factory = sqlite3.Row
    
    def dict_from_row(self, row):
        return dict(zip(row.keys(), row))
    
    def get_data_by_category(self, category):
        #data = self.conn.execute("SELECT * FROM " + category).fetchall()
        data = self.conn.execute("SELECT * FROM appconfig WHERE category=?", (category,)).fetchall()
        list_accumulator = []
        for item in data:
            list_accumulator.append(dict(item))
        return list_accumulator

    def get_all_data(self, table):
        data = self.conn.execute("SELECT * FROM " + table).fetchall()
        #data = self.conn.execute("SELECT * FROM appconfig WHERE category=?", (category,)).fetchall()
        list_accumulator = []
        for item in data:
            list_accumulator.append(dict(item))
        return list_accumulator

db = Database('Nebula.db')
data = db.conn.execute("SELECT * FROM appconfig WHERE key='DATABASEURI'").fetchone()

list_accumulator = []
list_accumulator.append({"key": data[0]})
list_accumulator.append({"value": data[1]})
list_accumulator.append({"category": data[2]})
list_accumulator.append({"description": data[3]})

print("Only data where key = DATABASEURI")
print("data", type(data), list_accumulator)
print("\n")

print("All data")
table = 'appconfig'
list_accumulator = db.get_all_data(table)
print("data", type(data), list_accumulator)
print("\n")

print("Only MFA")
category = 'MFA'
list_accumulator = db.get_data_by_category(category)
print("data", type(data), list_accumulator)
