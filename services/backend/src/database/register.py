from database.database import db
from database.models import RelacaoOperadoras


def create_tables():
    db.create_tables([RelacaoOperadoras])
    print("CREATED")


def insert_data(file):
    data_count = get_data()
    if data_count != 0:
        print(f"{data_count} rows already inserted")
        return

    with open(file, "r") as sql:
        query = sql.read()
    db.execute_sql(query)


def get_data():
    cursor = db.execute_sql("select count(*) from relacaooperadoras;")
    return cursor.fetchall()[0][0]


def register(app) -> None:
    @app.on_event("startup")
    async def startup_event():
        # RelacaoOperadoras.drop_table()
        db.connect()
        create_tables()
        insert_data("static\insert_operadoras.sql")
        db.close()

    @app.on_event("shutdown")
    def shutdown_event():
        # RelacaoOperadoras.drop_table()
        print("SHUTT DOWN")
