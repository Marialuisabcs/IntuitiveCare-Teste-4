from database.database import db
from database.models import RelacaoOperadoras
from database.util import get_values


def create_tables():
    db.create_tables([RelacaoOperadoras])
    print("CREATED")


def insert_data():
    data_count = get_data_count()

    if data_count != 0:
        print(f"{data_count} rows already inserted")
        return

    list_of_values = get_values()
    field_names = list(RelacaoOperadoras._meta.fields.keys())[1:]

    with db.atomic():
        RelacaoOperadoras.insert_many(list_of_values, fields=field_names).execute()


def get_data_count():
    cursor = db.execute_sql("select count(*) from relacaooperadoras;")
    return cursor.fetchall()[0][0]


def register(app) -> None:
    @app.on_event("startup")
    async def startup_event():
        db.connect()
        create_tables()
        insert_data()
        db.close()

    @app.on_event("shutdown")
    def shutdown_event():
        print("SHUTT DOWN")
