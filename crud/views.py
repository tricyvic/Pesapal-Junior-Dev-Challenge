from django.http import HttpResponse, HttpResponseRedirect
from db.engine import Database
from db.schema import bootstrap

db = Database()
bootstrap(db)

# Load tables
for table in db.tables.values():
    table.load()

def list_users(request):
    users = db.execute("SELECT * FROM users;")
    return HttpResponse(f"Welcome {str(users)}")

def create_user(request):
    user_id = int(request.GET.get("id"))
    email = request.GET.get("email")

    db.execute(f"INSERT INTO users VALUES ({user_id}, '{email}');")

    for table in db.tables.values():
        table.save()

    return HttpResponseRedirect("/users/")

def delete_user(request, pk):
    table = db.tables["users"]
    if pk in table.rows:
        row = table.rows.pop(pk)
        for index in table.indexes.values():
            index.remove(row)
        table.save()
    return HttpResponseRedirect("/users/")
