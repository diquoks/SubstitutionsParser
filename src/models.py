from __future__ import annotations

import enum

import pyquoks


# region Enums

class Weekday(enum.Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

    @staticmethod
    def from_string(string: str) -> Weekday:
        match string.lower():
            case "понедельник":
                return Weekday.MONDAY
            case "вторник":
                return Weekday.TUESDAY
            case "среда":
                return Weekday.WEDNESDAY
            case "четверг":
                return Weekday.THURSDAY
            case "пятница":
                return Weekday.FRIDAY
            case "суббота":
                return Weekday.SATURDAY
            case "воскресенье":
                return Weekday.SUNDAY
            case _:
                raise ValueError(f"Unknown weekday: {string!r}")


# endregion

# region Models & Containers

class PeriodModel(pyquoks.models.Model):
    _ATTRIBUTES = {
        "lecturer",
        "number",
        "room",
        "subgroup",
        "subject",
    }

    lecturer: str
    number: int
    room: str
    subgroup: int
    subject: str

    @property
    def formatted_room(self) -> str:
        if self.room.isdigit():
            return f"{self.room}к."
        else:
            return self.room

    @property
    def is_empty(self) -> bool:
        return not bool(self.lecturer and self.room and self.subject)


class DayScheduleContainer(pyquoks.models.Container):
    _ATTRIBUTES = {
        "weekday",
    }

    _DATA = {
        "schedule": PeriodModel,
    }

    schedule: list[PeriodModel]
    weekday: int

    @property
    def is_empty(self) -> bool:
        return not bool(self.schedule)


class WeekScheduleContainer(pyquoks.models.Container):
    _ATTRIBUTES = {
        "parity",
    }

    _DATA = {
        "schedule": DayScheduleContainer,
    }

    parity: bool
    schedule: list[DayScheduleContainer]


class GroupScheduleContainer(pyquoks.models.Container):
    _ATTRIBUTES = {
        "group",
    }

    _DATA = {
        "schedule": WeekScheduleContainer,
    }

    group: str
    schedule: list[WeekScheduleContainer]


class GroupSchedulesListing(pyquoks.models.Listing):
    _DATA = {
        "schedule": GroupScheduleContainer,
    }

    schedule: list[GroupScheduleContainer]


class SubstitutionModel(pyquoks.models.Model):
    _ATTRIBUTES = {
        "group",
    }

    _OBJECTS = {
        "period": PeriodModel,
        "substitution": PeriodModel,
    }

    group: str
    period: PeriodModel
    substitution: PeriodModel

    @property
    def number(self) -> int:
        return self.substitution.number

    @property
    def subgroup(self) -> int:
        return self.substitution.subgroup


class SubstitutionsListing(pyquoks.models.Listing):
    _DATA = {
        "substitutions": SubstitutionModel,
    }

    substitutions: list[SubstitutionModel]


class BellsVariantContainer(pyquoks.models.Container):
    _DATA = {
        "bells": str,
    }

    bells: list[str]

# endregion
