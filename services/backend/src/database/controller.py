from . import models


def get_operadoras(page: int):
    return list(models.RelacaoOperadoras.select().paginate(page, paginate_by=10))


def get_by_registro(registro: str, page: int):
    return list(
        models.RelacaoOperadoras.select()
        .where(models.RelacaoOperadoras.registro_ans == registro)
        .paginate(page, paginate_by=10)
    )


def get_by_cnpj(cnpj: str, page: int):
    return list(
        models.RelacaoOperadoras.select()
        .where(models.RelacaoOperadoras.cnpj == cnpj)
        .paginate(page, paginate_by=10)
    )


def get_by_nome_fantasia(nome_fantasia: str, page: int):
    return list(
        models.RelacaoOperadoras.select()
        .where(models.RelacaoOperadoras.nome_fantasia.contains(nome_fantasia))
        .paginate(page, paginate_by=10)
    )


def get_by_representante(representante: str, page: int):
    return list(
        models.RelacaoOperadoras.select()
        .where(models.RelacaoOperadoras.representante.contains(representante))
        .paginate(page, paginate_by=10)
    )
