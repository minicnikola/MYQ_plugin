from Autodesk.Revit.DB import *
from pprint import PrettyPrinter

__title__ = "Place joinery views"
__author__ = "Me"
__doc__ = "Button"

from Snippets._select import get_floor_plan_views, get_a2_block

pp = PrettyPrinter(indent=2)

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document
ac_view = doc.ActiveView


def create_sheet(name, number):
    sheet_ = ViewSheet.Create(doc, titleBlockTypeId=get_a2_block().Id)
    sheet_.SheetNumber = "ID-4" + str(number)
    sheet_.GetParameters("Sheet Name")[0].Set(name)
    sheet_.GetParameters("Sheet Group")[0].Set("Interior")
    sheet_.GetParameters("Sheet Sort")[0].Set('4' + str(number)[0] + "00")
    sheet_.GetParameters("Sheet series")[0].Set("ID4000 - JOINERY")
    return sheet_


def sort_views(views):
    sorted_views = dict()

    for view in views:
        view_name_split = view.GetParameters("View Name")[0].AsString().split(' - ')
        view_number = view_name_split[0]
        view_name = view_name_split[1]

        if not str(view_number).startswith('3'):
            continue

        if view_number in sorted_views:
            views_m = sorted_views[view_number]
            views_m.append(view)
            sorted_views[view_number] = views_m
        else:
            views_m = list()
            views_m.append(view)
            sorted_views[view_number] = views_m

    return sorted_views


def main():
    t = Transaction(doc, "Test")
    t.Start()

    try:
        joinery_plan_views = get_floor_plan_views("Joinery Plan")
        sorted_views = sort_views(joinery_plan_views)

        for i in sorted_views.items():
            room_number = i[0]
            views = i[1]
            print "Room number : {r}".format(r=room_number)
            k = 1
            for view in views:
                try:
                    print view
                    view_name = view.GetParameters("View Name")[0].AsString().split(' - ')[1]
                    sheet_number = room_number + "." + str(k)
                    sheet = create_sheet(view_name, sheet_number)
                    Viewport.Create(doc, sheet.Id, view.Id, XYZ(0, 0, 0))
                except Exception as e:
                    print e
                k += 1

        # for view in joinery_plan_views:
        #     v_name = view.GetParameters("View Name")[0].AsString()
        #     v_split = v_name.split(' - ')
        #
        #     if not str(v_split[0]).startswith('2'):
        #         continue
        #
        #     try:
        #         number = v_split[0]
        #         print number
        #         # sheet = create_sheet(v_split[1], v_split[0])
        #     except Exception as e:
        #         new_name = v_split[0]
        #         print new_name
        #         # sheet = create_sheet(v_split[1], v_split[0] + '.1')
        #         print e

    except Exception as e:
        print (e)

    t.Commit()


if __name__ == "__main__":
    main()
