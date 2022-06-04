from typing import Optional
from fastapi import FastAPI, Depends, HTTPException, Query, status
from fastapi.middleware.cors import CORSMiddleware
from database.register import register
from database.controller import *
from database import schemas
from database.database import db, db_state_default

app = FastAPI()

register(app)


async def reset_db_state():
    db._state._state.set(db_state_default.copy())
    db._state.reset()


def get_db(db_state=Depends(reset_db_state)):
    try:
        db.connect()
        yield
    finally:
        if not db.is_closed():
            db.close()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get(
    "/", response_model=list[schemas.RelacaoOperadoras], dependencies=[Depends(get_db)]
)
def home(
    page: Optional[int] = 1,
    query: Optional[str] = None,
    filterBy: Optional[str] = Query(
        default=None,
        description="Possible values: registro, cnpj, nome_fantasia, representante",
    ),
):
    if filterBy is not None and query is None or filterBy is None and query is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="You must provide filterBy and query",
        )
    if filterBy is None:
        return get_operadoras(page)
    elif filterBy == "registro":
        return get_by_registro(query, page)
    elif filterBy == "cnpj":
        return get_by_cnpj(query, page)
    elif filterBy == "nome_fantasia":
        return get_by_nome_fantasia(query, page)
    elif filterBy == "representante":
        return get_by_representante(query, page)

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid filterBy value"
    )
