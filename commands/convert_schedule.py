import json
import os
import sys

import openpyxl
import pyquoks

import misc
import models


def main() -> None:
    try:
        workbook = openpyxl.load_workbook(
            filename=pyquoks.utils.get_path(sys.argv[1]),
        )
    except IndexError:
        print("Specify the path to \".xlsx\" file with schedule!")
    else:
        worksheet = workbook.worksheets[0]

        os.makedirs(pyquoks.utils.get_path("exports"), exist_ok=True)
        with open(pyquoks.utils.get_path("exports/schedule.json"), "w", encoding="utf-8") as file:
            json.dump(
                models.GroupSchedulesListing(
                    data=list(
                        map(
                            lambda i: i._data,
                            misc.parse_schedule(worksheet),
                        ),
                    ),
                )._data,
                fp=file,
                ensure_ascii=False,
                indent=2,
            )


if __name__ == "__main__":
    main()
