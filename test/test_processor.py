import pytest#фреймворк для тестирования python-кода
from csv_processor.processor import apply_where, aggregate

def test_filter_numeric_gt():#Тест: фильтрация по числу
    data = [{"price": "100"}, {"price": "200"}]
    result = apply_where(data, "price>150")
    assert result == [{"price": "200"}]

def test_filter_text_eq():#Тест: фильтрация по тексту
    data = [{"brand": "apple"}, {"brand": "xiaomi"}]
    result = apply_where(data, "brand=apple")
    assert result == [{"brand": "apple"}]

def test_aggregate_avg():#Тест: агрегат avg
    data = [{"rating": "4.0"}, {"rating": "5.0"}]
    result = aggregate(data, "rating=avg")
    assert result["avg"] == 4.5

def test_aggregate_min():#Тест: агрегат min
    data = [{"rating": "4.5"}, {"rating": "4.1"}]
    result = aggregate(data, "rating=min")
    assert result["min"] == 4.1