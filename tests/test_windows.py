try:
    from views.main_window import MainWindow
except ImportError:
    assert False, "Не найдено главное окно приложения!"

try:
    from views.database_window import DatabaseWindow
except ImportError:
    assert False, "Не найдено окно базы данных!"
