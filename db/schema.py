def bootstrap(db):
    db.create_table_if_not_exists(
        name="users",
        columns={
            "id": "INT",
            "email": "TEXT"
        },
        primary_key="id",
        unique_columns={"email"}
    )