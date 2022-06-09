from __future__ import annotations
from peewee import *
from database.database import db


class RelacaoOperadoras(Model):
    id = AutoField
    registro_ans = CharField(max_length=50, unique=True)
    cnpj = CharField(max_length=50)
    razao_social = CharField(max_length=255)
    nome_fantasia = CharField(max_length=255, null=True)
    modalidade = CharField(max_length=50)
    logradouro = CharField(max_length=50)
    numero = CharField(max_length=50)
    complemento = CharField(max_length=255, null=True)
    bairro = CharField(max_length=255)
    cidade = CharField(max_length=50)
    uf = CharField(max_length=2)
    cep = CharField(max_length=50)
    ddd = CharField(max_length=10, null=True)
    telefone = CharField(max_length=25, null=True)
    fax = CharField(max_length=25, null=True)
    endereco_eletronico = CharField(max_length=255, null=True)
    representante = CharField(max_length=255)
    cargo = CharField(max_length=255)
    data = DateField()

    class Meta:
        database = db
