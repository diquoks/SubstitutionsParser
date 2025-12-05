from __future__ import annotations

import openpyxl
import pyquoks

import schedule_parser


class TestSchedule(pyquoks.test.TestCase):
    _MODULE_NAME = __name__

    def test_parse_schedule(self):
        workbook = openpyxl.load_workbook(
            filename=pyquoks.utils.get_path("resources/tables/schedule.xlsx"),
        )

        for group in list(schedule_parser.utils.parse_schedule(workbook.worksheets[0])):
            self.assert_type(
                func_name=self.test_parse_schedule.__name__,
                test_data=group,
                test_type=schedule_parser.models.GroupScheduleContainer,
            )
