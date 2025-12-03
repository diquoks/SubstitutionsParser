from __future__ import annotations

import enum

import pyquoks

import models


# region models.py

class BellsVariants(enum.Enum):
    Monday = 0
    Wednesday = 1
    Other = 2


class BellsScheduleListing(pyquoks.models.Listing):
    _DATA = {
        "variants": models.BellsVariantContainer,
    }

    variants: list[models.BellsVariantContainer]

    def get_variant_by_weekday(
            self,
            weekday: models.Weekday,
    ) -> models.BellsVariantContainer:
        match weekday:
            case models.Weekday.MONDAY:
                return self.variants[BellsVariants.Monday.value]
            case models.Weekday.WEDNESDAY:
                return self.variants[BellsVariants.Wednesday.value]
            case models.Weekday.TUESDAY | models.Weekday.THURSDAY | models.Weekday.FRIDAY | models.Weekday.SATURDAY:
                return self.variants[BellsVariants.Other.value]
            case models.Weekday.SUNDAY:
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
