Команды (аргументы)

- `--file` (обязательно)
  Путь к CSV-файлу.  
  **Пример:** `--file data.csv`

- `--where`  
  Фильтр строк по условию в формате `column operator value`.  
  Операторы: `>`, `<`, `=`, `>=`, `<=`.  
  **Пример:** `--where "price>=100"`

- `--order-by`  
  Сортировка по колонке в формате `column=order`, где order — `asc` или `desc`.  
  Пример: `--order-by "price=desc"`

- `--aggregate`  
  Агрегация по колонке в формате `column=operation`, где operation:  
  - `avg` — среднее  
  - `min` — минимум  
  - `max` — максимум  
  Пример: `--aggregate "rating=avg"`

---

Запуск

python main.py --file data.csv --where "price>=100" --order-by "price=desc" --aggregate "price=avg"