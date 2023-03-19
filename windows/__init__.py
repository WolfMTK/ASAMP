from typing import NewType

from .windows import MainWindow

MainWindowType = NewType("MainWindow", MainWindow)

__all__ = ["MainWindow", "MainWindowType"]
