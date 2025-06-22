import argparse


def get_args():#разбор аргументов
    parser = argparse.ArgumentParser(description='Фильтр и агрегатор')
    parser.add_argument('--file', required=True, help='Путь к CSV-файлу')
    parser.add_argument('--where', help='Фильтр в формате price=>100')
    parser.add_argument('--aggregate', help='Агрегация в формате price=avg')
    return parser.parse_args()