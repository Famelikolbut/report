from abc import ABC, abstractmethod
from typing import List
from models.employee import Employee


class BaseReport(ABC):
    """
    Абстрактный базовый класс для всех отчётов.
    """

    @abstractmethod
    def generate(self, employees: List[Employee]) -> None:
        """
        Метод для генерации отчёта.
        """
        pass
