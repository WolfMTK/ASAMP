import pytest

try:
    from database.database import Database
except ImportError:
    pytest.fail("Не найдена база данных!")
    assert False, "Не найдена база данных!"


def test_error_get_material_with_database():
    try:
        get_material_with_database()
    except AttributeError:
        pytest.fail("Нет 'get_material_with_database' в Database!")


def get_material_with_database():
    list_material = Database().get_material_with_database
    if type(list_material) != list:
        pytest.fail("Проверьте запрос к базе данных!")
    elif len(list_material) == 0:
        pytest.fail("База данных пуста или нет данных для поля material! "
                    "Заполните данные!")


def test_error_get_type_part_with_database():
    try:
        get_type_part_with_database()
    except AttributeError:
        pytest.fail("Нет '' в Database!")


def get_type_part_with_database():
    list_type_part = Database().get_type_part_with_database
    if type(list_type_part) != list:
        pytest.fail("Проверьте запрос к базе данных!")
    elif len(list_type_part) == 0:
        pytest.fail("База данных пуста или нет данных для поля type_part! "
                    "Заполните данные!")


def test_get_brand_with_database():
    try:
        Database().get_brand_with_database("Сталь")
    except AttributeError:
        pytest.fail("Нет метода 'get_brand_with_database'")
    list_brand = Database().get_brand_with_database("Сталь")
    if type(list_brand) != list:
        pytest.fail("Проверьте запрос к базе данных!")
    elif len(list_brand) == 0:
        pytest.fail("База данных пуста! Заполните данные!")
