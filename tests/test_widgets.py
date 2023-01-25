try:
    from widgets.central_widget import CentralWidget
except ImportError:
    assert False, "Не найден центральный виджет!"

try:
    from widgets.action_widget import ActionWidget
except ImportError:
    assert False, "Не найден виджет с действиями!"

try:
    from widgets.data_widget import DataWidget
except ImportError:
    assert False, "Не найден виджет с данными ввода!"

try:
    from widgets.parameters_widget import ParametersWidget
except ImportError:
    assert False, "Не найден виджет с параметрами!"

try:
    from widgets.result_widget import ResultWidget
except ImportError:
    assert False, "Не найден виджет с выводом результата!"

try:
    from widgets.widget import Widget
except ImportError:
    assert False, "Не найден базовый виджет!"

try:
    from widgets.control_widget import ControlWidget
except ImportError:
    assert False, "Не найден виджет управления базой данных!"

try:
    from widgets.database_widget import DatabaseWidget
except ImportError:
    assert False, "Не найден виджет вывода данных с базы данных!"
