from __future__ import annotations

import openpyxl
import pyquoks

import misc
import models


class TestSchedule(pyquoks.test.TestCase):
    _MODULE_NAME = __name__

    def test_parse_schedule(self):
        workbook = openpyxl.load_workbook(
            filename=pyquoks.utils.get_path("resources/tables/schedule.xlsx"),
        )

        worksheet = workbook.worksheets[0]

        for group in list(misc.parse_schedule(worksheet)):
            self.assert_type(
                func_name=self.test_parse_schedule.__name__,
                test_data=group,
                test_type=models.GroupScheduleContainer,
            )
