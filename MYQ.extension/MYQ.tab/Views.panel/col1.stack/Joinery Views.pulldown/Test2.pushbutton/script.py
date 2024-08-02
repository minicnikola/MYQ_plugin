from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Structure import StructuralType
from pprint import PrettyPrinter

__title__ = "Change detail numbers"
__author__ = "Me"
__doc__ = "Button"

from Snippets._select import get_floor_plan_views, get_sheets_by_series, get_viewports, get_generic_annotation, \
    get_view_name_from_viewport, get_viewport_parameter_value

pp = PrettyPrinter(indent=2)

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document
ac_view = doc.ActiveView


def get_detail_number(view_name):
    imp_name = str(view_name).lower()

    if imp_name.find("elevation 1") != -1 or imp_name.find("elevation a") != -1:
        detail_number = "ELEVATION A"
        return detail_number
    elif imp_name.find("elevation 2") != -1 or imp_name.find("elevation b") != -1:
        detail_number = "ELEVATION B"
        return detail_number
    elif imp_name.find("elevation 3") != -1 or imp_name.find("elevation c") != -1:
        detail_number = "ELEVATION C"
        return detail_number
    elif imp_name.find("elevation 4") != -1 or imp_name.find("elevation d") != -1:
        detail_number = "ELEVATION D"
        return detail_number
    elif imp_name.find("section 1") != -1:
        detail_number = "SECTION 1"
        return detail_number
    elif imp_name.find("section 2") != -1:
        detail_number = "SECTION 2"
        return detail_number
    elif imp_name.find("section 3") != -1:
        detail_number = "SECTION 3"
        return detail_number
    elif imp_name.find("section 4") != -1:
        detail_number = "SECTION 4"
        return detail_number
    else:
        detail_number = "PLAN"
        return detail_number


def main():
    t = Transaction(doc, "Test")
    t.Start()

    try:
        sheets = get_sheets_by_series("ID4000 - JOINERY")
        for sheet in sheets:
            sheet_number = sheet.GetParameters("Sheet Number")[0].AsString()

            print sheet_number
            print '*' * 50

            viewports = get_viewports(sheet)
            all_names = list()
            for viewport in viewports:
                view_name = get_viewport_parameter_value(viewport, "View Name")
                sub = SubTransaction(doc)
                sub.Start()
                try:
                    detail_number = get_detail_number(view_name)

                    if detail_number in all_names:
                        detail_number = detail_number + "-1"

                    all_names.append(detail_number)
                    param_a = viewport.LookupParameter("Detail Number")
                    param_a.Set(detail_number)
                    sub.Commit()
                except Exception as e:
                    print e
                    sub.RollBack()
            print all_names
    except Exception as e:
        print (e)

    t.Commit()


if __name__ == "__main__":
    main()
