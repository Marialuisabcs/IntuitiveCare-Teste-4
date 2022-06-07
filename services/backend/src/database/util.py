from csv import reader

# Insira o csv em um folder 'static' (csv privado por conter informações sensíveis)
file = "static\Relatorio_cadop teste 4.csv"


def get_values(file: str) -> list:
    with open(file, "r", encoding="utf-8") as f:
        rdr = reader(f, delimiter=";")
        next(rdr)
        list_of_values = list(map(tuple, rdr))
    return list_of_values
