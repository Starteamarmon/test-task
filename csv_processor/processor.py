import csv #библиотека, чтобы читать csv-файлы
import operator#библиотека, С математическими функциями


#Словарь, связывает символы с функциями
ops = {
    ">": operator.gt,
    "<": operator.lt,
    "=": operator.eq,
    '<=': operator.le,
    '>=': operator.ge
}


def read_csv(path):#Открывает файлы, читает в виде словарей
    with open(path, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def parse_condition(condition):#принимает строку-условие
    for op in ops:#перебераем символы операторов
        if op in condition:#Если символ есть в строке
            col, val = condition.split(op, 1)#то разделяем строку по найденному знаку
            return col.strip(), ops[op], val.strip()#возврат колонки,функции по знаку и значения
    raise ValueError("Ошибка, неверный формат")


def apply_where(rows, condition):#фильтр строк, принимает список словарей и строку-условие
    if not condition:#eсли --where не задан,не фильтруем
        return rows
    col, op, val = parse_condition(condition)#Расклыдываю условие по переменным
    try:
        val = float(val)#Преобразую строку в число
        return [r for r in rows if op(float(r[col]), val)]#для каждой строки беру значение из нужной колонки, превращаю в число и сраввниваю со значением условия
    except ValueError:#Если не удалось преобразовать val в float — значит, это не число, а текст
        return [r for r in rows if op(r[col], val)]#сравниваю как строки


def aggregate(rows, condition):#принимает список словарей и строку-условие
    col, func = condition.split("=")#Разделение строки по символу "=" на колонку и функцию
    col, func = col.strip(), func.strip()#убираю пробелы
    values = [float(row[col]) for row in rows if row[col]]#достаю из колонки числа
    if not values:#Если в колонке нет чисел
        return {func: None} #ставляю значение пустым
    if func == "avg":#считает среднее, округление до двух знаков
        return {"avg": round(sum(values) / len(values), 2)}
    elif func == "min":#минимальное
        return {"min": min(values)}
    elif func == "max":#максимальное
        return {"max": max(values)}
    else:
        raise ValueError("Команды агрегатора 'avg','min','max'")



def sort_rows(rows, order_by):
    if not order_by:
        return rows
    col, order = order_by.split("=")
    col, order = col.strip(), order.strip()
    reverse = order.lower() == "desc"#проверка хочет ли юзер отсортировать в обратном порядке 
    try:#Если в колонке числа
        return sorted(rows, key=lambda r: float(r[col]), reverse=reverse)#сортировка строки, считая, что в колонке числа
    except ValueError:#Если строки
        return sorted(rows, key=lambda r: r[col], reverse=reverse)#сортировка строки
