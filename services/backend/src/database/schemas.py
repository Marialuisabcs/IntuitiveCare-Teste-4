from datetime import date
from pydantic import BaseModel
from typing import Any
from pydantic.utils import GetterDict
from pydantic.schema import Optional
import peewee


class PeeweeGetterDict(GetterDict):
    def get(self, key: Any, default: Any = None):
        res = getattr(self._obj, key, default)
        if isinstance(res, peewee.ModelSelect):
            return list(res)
        return res


class RelacaoOperadorasBase(BaseModel):
    registro_ans: str
    cnpj: str
    razao_social: str
    nome_fantasia: Optional[str]
    modalidade: str
    logradouro: str
    numero: str
    complemento: Optional[str]
    bairro: str
    cidade: str
    uf: str
    cep: str
    ddd: Optional[str]
    telefone: Optional[str]
    fax: Optional[str]
    endereco_eletronico: Optional[str]
    representante: str
    cargo: str
    data: date


class RelacaoOperadoras(RelacaoOperadorasBase):
    id: int
    registro_ans: str
    cnpj: str
    razao_social: str
    nome_fantasia: Optional[str]
    modalidade: str
    logradouro: str
    numero: str
    complemento: Optional[str]
    bairro: str
    cidade: str
    uf: str
    cep: str
    ddd: Optional[str]
    telefone: Optional[str]
    fax: Optional[str]
    endereco_eletronico: Optional[str]
    representante: str
    cargo: str
    data: date

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict
