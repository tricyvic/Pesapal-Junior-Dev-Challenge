from db.engine import Database

def main():
    db = Database()
    print("Welcome to pesaDB")

    # Load existing tables
    for table in db.tables.values():
        table.load()

    try:
        while True:
            sql = input("pesaDB> ")
            if sql.lower() in ("exit", "quit"):
                break
            result = db.execute(sql)
            print(result)
    except KeyboardInterrupt:
        print("\nExiting...")

    # Save tables
    for table in db.tables.values():
        table.save()
    print("All tables saved!")

if __name__ == "__main__":
    main()
