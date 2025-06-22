import argparse #Импорт библиотеки с командами "--file" и тд...
from processor import read_csv, apply_where, aggregate, sort_rows # Импорт функций из файла processor.py
from utils import display_table, display_aggregation #Импорт функций из файла utils.py


def main():
    parser = argparse.ArgumentParser() #Парсер
    #Команды
    parser.add_argument("--file", required=True)#путь к файлу(обязателен)
    parser.add_argument("--where")#фильтрация
    parser.add_argument("--aggregate")#агрегация
    parser.add_argument("--order-by")#сортировка

    
    args = parser.parse_args()#Чтение командной строки

    rows = read_csv(args.file)#Чтение файлов, превращение таблиц в список словарей
    rows = apply_where(rows, args.where)#Если указано условие --where, фильтр строки
    rows = sort_rows(rows, args.order_by)#Если указана сортировка, то по нужной колонке

    if args.aggregate:
        result = aggregate(rows, args.aggregate)#среднее, максимум или минимум
        display_aggregation(result)#принт результата в виде таблицы
    else:
        display_table(rows)#Принт таблицы


if __name__ == "__main__":#Запуск скрипта
    main()