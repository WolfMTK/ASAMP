import pytest

try:
    from database.database import Database
except ImportError:
    pytest.fail("Не найдена база данных!")
    assert False, "Не найдена база данных!"


def test_error_get_material_with_database():
    try:
        check_material_with_database()
    except AttributeError:
        pytest.fail("Нет 'get_material_with_database' в Database!")


def check_material_with_database():
    list_material = Database().materials_with_database
    if type(list_material) != list:
        pytest.fail("Проверьте запрос к базе данных!")
    elif len(list_material) == 0:
        pytest.fail("База данных пуста или нет данных для поля material! "
                    "Заполните данные!")


def test_error_get_type_part_with_database():
    try:
        check_type_part_with_database()
    except AttributeError:
        pytest.fail("Нет 'get_type_part_with_database' в Database!")


def check_type_part_with_database():
    list_type_part = Database().type_parts_with_database
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
    except TypeError:
        pytest.fail("Методу 'get_brand_with_database' не переданы аргументы!")
    list_brand = Database().get_brand_with_database("Сталь")
    if type(list_brand) != list:
        pytest.fail("Проверьте запрос к базе данных!")
    elif len(list_brand) == 0:
        pytest.fail("База данных пуста или нет данных в поле brand! "
                    "Заполните данные!")


def test_get_parameters_with_database():
    try:
        Database().get_parameters_with_database("Вал")
    except AttributeError:
        pytest.fail("Нет метода 'get_parameters_with_database'")
    list_brand = Database().get_parameters_with_database("Вал")
    if type(list_brand) != list:
        pytest.fail("Проверьте запрос к базе данных!")
    elif len(list_brand) == 0:
        pytest.fail("База данных пуста или нет данных для поля parameter! "
                    "Заполните данные!")


def test_get_patterns_with_database():
    try:
        Database().get_patterns_with_database('Сталь', 'Вал', '45')
    except AttributeError:
        pytest.fail("Нет 'get_patterns_with_database' в Database!")
    except TypeError:
        pytest.fail(
            "Методу 'get_patterns_with_database' не переданы аргументы!")
    list_patterns = Database().get_patterns_with_database(
        'Сталь', 'Вал', '45'
    )
    if type(list_patterns) != list:
        pytest.fail("Проверьте запрос к базе данных!")
    elif len(list_patterns) == 0:
        pytest.fail(
            "База данных пуста или нет данных для полей pattern и connect_text! "
            "Заполните данные!")
