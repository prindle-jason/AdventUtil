from abc import ABC, abstractmethod
from enum import Enum
from .DataImport import readLines, get_sample_data, InputType

class Day(ABC):
    
    def __init__(self, year, day, expected_a, expected_b):
        self.year = year
        self.day = day

        self.expected_a = expected_a
        self.expected_b = expected_b

        self.actual_a = "Unsolved"
        self.actual_b = "Unsolved"

        self._lines = []

    @property
    def lines(self):
        return self._lines

    @property
    def expected_a(self):
        return self._expected_a

    @expected_a.setter
    def expected_a(self, value):
        self._expected_a = value

    @property
    def expected_b(self):
        return self._expected_b

    @expected_b.setter
    def expected_b(self, value):
        self._expected_b = value

    @property
    def actual_a(self):
        return self._actual_a

    @actual_a.setter
    def actual_a(self, value):
        self._actual_a = value

    @property
    def actual_b(self):
        return self._actual_b

    @actual_b.setter
    def actual_b(self, value):
        self._actual_b = value
    
    @abstractmethod
    def partA():
        ...

    @abstractmethod
    def partB():
        ...

    def run(self, data=InputType.LIVE_DATA, stripped=True):
        self._lines = readLines(self.year, self.day, stripped) if data == InputType.LIVE_DATA else get_sample_data(self.year, self.day, stripped)

        self.actual_a = self.partA()
        self.actual_b = self.partB()

        if self.actual_a == self.expected_a and self.actual_b == self.expected_b:
            result = "success"             
        else:
            result = "failed"
        
        print("{y} Day {d} {r}!".format(y=self.year,d=self.day,r=result))
        self.__print_result('A', self.expected_a, self.actual_a)
        self.__print_result('B', self.expected_b, self.actual_b)

    def __print_result(self, part, expected, actual):
        print("  Part {part} expected: {exp}. Actual: {act}".format(part=part,exp=expected,act=actual))