from __future__ import annotations
import enum
import pyquoks


# region Enums

class Weekdays(enum.Enum):
    Monday = 0
    Tuesday = 1
    Wednesday = 2
    Thursday = 3
    Friday = 4
    Saturday = 5
    Sunday = 6


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


class BellsVariantContainer(pyquoks.models.Container):
    _DATA = {
        "bells": str,
    }

    bells: list[str]

# endregion
