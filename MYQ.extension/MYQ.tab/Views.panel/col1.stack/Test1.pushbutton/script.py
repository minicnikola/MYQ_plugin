from Autodesk.Revit.DB import *
from pprint import PrettyPrinter

__title__ = "Rename joinery views"
__author__ = "Me"
__doc__ = "Button"

from Snippets._select import get_floor_plan_views

pp = PrettyPrinter(indent=2)

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document
ac_view = doc.ActiveView


def main():
    t = Transaction(doc, "Test")
    t.Start()

    try:
        joinery_plan_views = get_floor_plan_views("Joinery Plan")
        for view in joinery_plan_views:
            v_name = view.GetParameters("View Name")[0].AsString()
            # v_split = v_name.split(' - ')

            if not str(v_name).startswith("GF -"):
                continue
            # if v_name != "BF - 1002 - FURNITURE PLAN - Callout 15":
            #     continue
            print v_name

            rooms_in_view = FilteredElementCollector(doc, view.Id).OfCategory(BuiltInCategory.OST_Rooms).ToElements()
            # print rooms_in_view
            print len(rooms_in_view)

            # break
    except Exception as e:
        print (e)

    t.Commit()


if __name__ == "__main__":
    main()
