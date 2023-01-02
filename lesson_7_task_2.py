"""Реализовать проект расчёта суммарного расхода ткани на производство одежды.
 Основная сущность (класс) этого проекта — одежда, которая может иметь
 определённое название. К типам одежды в этом проекте относятся пальто и
 костюм. У этих типов одежды существуют параметры: размер (для пальто) и
 рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих
методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные
на этом уроке знания: реализовать абстрактные классы для основных классов
проекта, проверить на практике работу декоратора @property."""

from abc import ABC, abstractmethod


class abst_cloth(ABC):
    @abstractmethod
    def suit_exp(self):
        pass

    @abstractmethod
    def coat_exp(self):
        pass

    @abstractmethod
    def total_exp(self):
        pass


class Clothes(abst_cloth):
    def __init__(self, v, h):
        self.v = v
        self.h = h
        self.coat_expn = self.v / 6.5 + 0.5
        self.suit_expn = self.h * 2 + 0.3

    def suit_exp(self):
        return str(f'Расход на пальто = {self.coat_expn:.2f}')

    def coat_exp(self):
        return str(f'Расход на костюм = {self.suit_expn:.2f}')

    def total_exp(self):
        return str(f'Расход итого = {self.suit_expn + self.coat_expn:.2f}')

a = Clothes(1, 10)

print(a.suit_exp())
print(a.coat_exp())
print(a.total_exp())