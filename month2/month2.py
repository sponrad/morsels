from calendar import monthrange
from dataclasses import dataclass
from datetime import date

# yanked this from a previous answer
# https://www.pythonmorsels.com/exercises/e1ba106369e24029b5723a855ae5c735/solution/
# all yanked except __sub__
@dataclass(order=True, frozen=True)
class Month:

    __slots__ = ['year', 'month']

    year: int
    month: int

    def __str__(self):
        return f"{self.year}-{self.month:02}"

    @property
    def first_day(self):
        return date(self.year, self.month, 1)

    @property
    def last_day(self):
        weekday_of_first_date, last_date = monthrange(self.year, self.month)
        return date(self.year, self.month, last_date)

    @classmethod
    def from_date(cls, date_obj):
        return cls(date_obj.year, date_obj.month)

    def strftime(self, fmt):
        return self.first_day.strftime(fmt)

    def __sub__(self, other):
        if isinstance(other, MonthDelta):
            months = (self.year * 12) + self.month - other.months
            year = int(months / 12)
            month = months % 12
            if month == 0:
                month = 12
                year -= 1
            return Month(year, month)
        elif isinstance(other, Month):
            months = self.year * 12 + self.month - other.year * 12 - other.month
            return MonthDelta(months)
        else:
            raise TypeError

@dataclass
class MonthDelta:
    months: int

    def __str__(self):
        return f"{self.months}"

    def __add__(self, other):
        if isinstance(other, Month):
            calced_month = other.month + self.months
            month = (calced_month % 12)
            year = other.year + int(calced_month / 12)
            return Month(year, month)
        else:
            raise TypeError

    __radd__ = __add__
