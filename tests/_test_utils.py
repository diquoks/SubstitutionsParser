from __future__ import annotations

import enum

import pyquoks

import schedule_parser


# region models.py

class BellsVariants(enum.Enum):
    Monday = 0
    Wednesday = 1
    Other = 2


class BellsScheduleListing(schedule_parser.models.BellsScheduleListing):
    def get_variant_by_weekday(
            self,
            weekday: schedule_parser.models.Weekday,
    ) -> schedule_parser.models.BellsVariantContainer:
        match weekday:
            case schedule_parser.models.Weekday.MONDAY:
                return self.variants[BellsVariants.Monday.value]
            case schedule_parser.models.Weekday.WEDNESDAY:
                return self.variants[BellsVariants.Wednesday.value]
            case schedule_parser.models.Weekday.TUESDAY | schedule_parser.models.Weekday.THURSDAY | \
                 schedule_parser.models.Weekday.FRIDAY | schedule_parser.models.Weekday.SATURDAY:
                return self.variants[BellsVariants.Other.value]
            case schedule_parser.models.Weekday.SUNDAY:
                raise ValueError


# endregion

# region data.py

class DataProvider(pyquoks.data.DataProvider):
    _OBJECTS = {
        "bells": BellsScheduleListing
    }

    _PATH = pyquoks.utils.get_path("resources/data/")

    bells: BellsScheduleListing

# endregion
