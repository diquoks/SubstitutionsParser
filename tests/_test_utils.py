from __future__ import annotations
import enum
import pyquoks
import models


# region models.py

class BellsVariants(enum.Enum):
    Monday = 0
    Wednesday = 1
    Other = 2


class BellsScheduleContainer(pyquoks.models.Container):
    _DATA = {
        "variants": models.BellsVariantContainer,
    }

    variants: list[models.BellsVariantContainer]

    def get_variant_by_weekday(
            self,
            weekday: models.Weekdays,
    ) -> models.BellsVariantContainer:
        match weekday:
            case models.Weekdays.Monday:
                return self.variants[BellsVariants.Monday.value]
            case models.Weekdays.Wednesday:
                return self.variants[BellsVariants.Wednesday.value]
            case models.Weekdays.Tuesday | models.Weekdays.Thursday | models.Weekdays.Friday | models.Weekdays.Saturday:
                return self.variants[BellsVariants.Other.value]
            case models.Weekdays.Sunday:
                raise ValueError


# endregion

# region data.py

class DataProvider(pyquoks.data.DataProvider):
    _OBJECTS = {
        "bells": BellsScheduleContainer
    }

    _PATH = pyquoks.utils.get_path("resources/data/")

    bells: BellsScheduleContainer

# endregion
