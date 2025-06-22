from tabulate import tabulate#Превращает списки\словари в консольные таблицы

def display_table(rows):#rows - список словарей
    print(tabulate(rows, headers="keys", tablefmt="grid"))

def display_aggregation(result):#result — словарь
    print(tabulate([result], headers="keys", tablefmt="grid"))