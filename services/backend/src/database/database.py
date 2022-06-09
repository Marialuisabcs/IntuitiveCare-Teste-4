from contextvars import ContextVar
from decouple import config
from urllib.parse import urlparse
import peewee

db_state_default = {"closed": None, "conn": None, "ctx": None, "transactions": None}
db_state = ContextVar("db_state", default=db_state_default.copy())


db_state = ContextVar("db_state", default=db_state_default.copy())


class PeeweeConnectionState(peewee._ConnectionState):
    def __init__(self, **kwargs):
        super().__setattr__("_state", db_state)
        super().__init__(**kwargs)

    def __setattr__(self, name, value):
        self._state.get()[name] = value

    def __getattr__(self, name):
        return self._state.get()[name]


def change_scheme(db_url: str):
    """Changes prefix 'postgres' to 'postgresql' for Peewee acceptance

    Args:
        db_url (str): database url to be changed

    Returns:
       db_url_updated (str): database url with 'postgresql' prefix replaced
    """
    db_url_parsed = urlparse(db_url)
    db_url_updated = db_url_parsed._replace(scheme="postgresql").geturl()
    return db_url_updated


database_url = change_scheme(config("DATABASE_URL"))

db = peewee.PostgresqlDatabase(database_url)

db._state = PeeweeConnectionState()
