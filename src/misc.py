from __future__ import annotations
import typing
import openpyxl.worksheet.worksheet
import models, constants


def parse_substitutions(worksheet: openpyxl.worksheet.worksheet.Worksheet) -> typing.Generator[models.SubstitutionModel]:
    def _get_period(*args, number: int) -> models.PeriodModel:
        return models.PeriodModel(
            data={
                "lecturer": args[2],
                "number": number,
                "room": args[3],
                "subgroup": int(args[0]) if args[0] else 0,
                "subject": args[1],
            },
        )

    for row in list(worksheet.rows)[constants.TABLE_HEADER_INDEX:]:
        row = list(
            map(
                lambda cell: cell.value,
                list(row[:constants.TABLE_WIDTH]),
            )
        )

        if set(row) == {None}:
            continue

        group, period_number, *row_values = row
        period_number = int(period_number)

        yield models.SubstitutionModel(
            data={
                "group": group,
                "period": _get_period(
                    *row_values[4:],
                    number=period_number,
                )._data,
                "substitution": _get_period(
                    *row_values[:4],
                    number=period_number,
                )._data,
            },
        )
