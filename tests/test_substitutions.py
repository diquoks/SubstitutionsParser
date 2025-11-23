from __future__ import annotations
import openpyxl, pyquoks
import models, misc


class TestSubstitutions(pyquoks.test.TestCase):
    _MODULE_NAME = __name__

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

        cls._WORKBOOKS = [
            "substitutions",
            "substitutions_old",
        ]

    def test_parse_substitutions(self):
        for filename in self._WORKBOOKS:
            workbook = openpyxl.load_workbook(
                filename=pyquoks.utils.get_path(f"resources/tables/{filename}.xlsx"),
            )

            worksheet = workbook.worksheets[0]

            for a in list(misc.parse_substitutions(worksheet)):
                self.assert_type(
                    func_name=self.test_parse_substitutions.__name__,
                    test_data=a,
                    test_type=models.SubstitutionModel,
                )
