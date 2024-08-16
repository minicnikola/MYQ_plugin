from Autodesk.Revit.DB import *
from pprint import PrettyPrinter

__title__ = "Change view sheet title"
__author__ = "Me"
__doc__ = "Button"

from Snippets._select import get_sheets_by_series, get_viewports, get_view_parameter_value

pp = PrettyPrinter(indent=2)

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document
ac_view = doc.ActiveView


def change_view_sheet_name(viewport):
    detail_number = get_view_parameter_value(viewport, "Detail Number")
    viewport.GetParameters('View Sheet Title')[0].Set(detail_number)


def change_detail_number(viewport):
    detail_number = viewport.GetParameters('Detail Number')[0].AsString()

    if detail_number is not None:
        detail_number_ = str(detail_number).split(' ')
        print detail_number_
        if len(detail_number_) == 2:
            detail_number_letter = detail_number_[-1]
            print detail_number_letter
            viewport.GetParameters('Detail Number')[0].Set(detail_number_letter)


def main():
    t = Transaction(doc, "Test")
    t.Start()

    try:
        all_joinery_sheets = get_sheets_by_series("ID4000 - JOINERY")
        for sheet in all_joinery_sheets:
            sheet_viewports = get_viewports(sheet)
            for viewport in sheet_viewports:
                # change_view_sheet_name(viewport)

                sub = SubTransaction(doc)
                sub.Start()
                try:
                    # change_detail_number(viewport)
                    sub.Commit()
                except Exception as e:
                    print e
                    sub.RollBack()

    except Exception as e:
        print e

    t.Commit()


if __name__ == "__main__":
    main()
