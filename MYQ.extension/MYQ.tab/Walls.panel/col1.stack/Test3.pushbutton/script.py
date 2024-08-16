from Autodesk.Revit.DB import *
from pprint import PrettyPrinter
from Snippets._select import get_sheets_by_room, get_schedule_by_name, get_viewports, get_view_parameter_value, \
    get_a1_block

__title__ = "-"
__author__ = "Me"
__doc__ = "--------"

from Snippets.size import get_scaled_size, get_viewport_dimensions
from constants import Sizes

pp = PrettyPrinter(indent=2)

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document


def main():
    t = Transaction(doc, "Test")
    t.Start()

    try:
        pass

    except Exception as e:
        print (e)

    t.Commit()


if __name__ == "__main__":
    main()
