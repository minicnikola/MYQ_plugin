import pprint
from operator import itemgetter
import random

import pyrevit.forms
from Autodesk.Revit.DB import *
from pprint import PrettyPrinter

__title__ = "-"
__author__ = "Me"
__doc__ = "--------"

from Snippets._select import get_viewports, get_a2_block
from Snippets.size import get_view_size, get_scaled_size, get_viewport_dimensions
from constants import Sizes


uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document
ui_view = doc.ActiveView


def main():
    f = pyrevit.forms.alert(title="Warning", msg='Do you want to proceed')
    if not f:
        return

    t = Transaction(doc, "Test")
    t.Start()
    try:
      pass
    except Exception as e:
        print (e)

    t.Commit()


if __name__ == "__main__":
    main()

# print room_view
# if room_view[0] == 'plan':
#     create_plan_sheet(room_view, room_number)
# else:
#     create_elevation_sheet(room_views, room_number)

# if multiple_sheets(view_tuple):
#     pass
# else:
#     pass
#     # TODO this can be an issue
