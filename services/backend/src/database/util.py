from csv import reader
import datetime

# Insira o csv em um folder 'static' (csv privado por conter informações sensíveis)
file = "../static/Relatorio_cadop.csv"


def get_values() -> list:
    """Retrieve data from csv file

    Returns:
        list: list that contains the values of the csv file
    """
    with open(file, "r", encoding="utf-8") as f:
        rdr = reader(f, delimiter=";")
        next(rdr)
        list_of_values = list(map(list, rdr))

    list_of_values = change_date_format(list_of_values)

    return list_of_values


def change_date_format(list_of_values: list) -> list:
    """Changes the date format of the 'data' attribute (from dd/mm/yy to mm/dd/yy)

    Args:
        list_of_values (list): list of values retrieved by get_values() method

    Returns:
        list: the same list returned by get_values() eith the 'data' field formatted
    """
    for item in list_of_values:
        item[-1] = datetime.datetime.strptime(str(item[-1]), "%d/%m/%Y").strftime(
            "%m/%d/%Y"
        )
    return list_of_values
