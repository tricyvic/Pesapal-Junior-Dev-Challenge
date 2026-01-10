from db.engine import Database

def main():
    db = Database()
    print("Welcome to Victor's pesaDB")
    while True:
        try:
            sql = input("pesaDB> ")
            if sql.lower() in ("exit", "quit"):
                break
            result = db.execute(sql)
            print(result)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
