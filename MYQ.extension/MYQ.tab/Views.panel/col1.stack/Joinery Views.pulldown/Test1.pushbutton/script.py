from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Structure import StructuralType
from pprint import PrettyPrinter

__title__ = "Place symbol bellow views"
__author__ = "Me"
__doc__ = "Button"

from Snippets._select import get_floor_plan_views, get_sheets_by_series, get_viewports, get_generic_annotation, \
    get_view_name_from_viewport, get_viewport_parameter_value

pp = PrettyPrinter(indent=2)

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document
ac_view = doc.ActiveView


def get_annotation_on_sheet(sheet):
    pp = FilteredElementCollector(doc, sheet.Id).OfCategory(BuiltInCategory.OST_GenericAnnotation).ToElements()
    print pp


def main():
    t = Transaction(doc, "Test")
    t.Start()

    try:
        series = "ID4000 - JOINERY"
        sheets = get_sheets_by_series(series)
        g_annotation_plan = get_generic_annotation("PLAN")
        g_annotation_el_a = get_generic_annotation("ELEVATION 1")
        g_annotation_el_b = get_generic_annotation("ELEVATION 2")
        g_annotation_el_c = get_generic_annotation("ELEVATION 3")
        g_annotation_el_d = get_generic_annotation("ELEVATION 4")
        g_annotation_s_one = get_generic_annotation("SECTION 1")
        g_annotation_s_two = get_generic_annotation("SECTION 2")

        for i, sheet in enumerate(sheets):
            sheet_viewports = get_viewports(sheet)
            # print sheet.GetParameters('Sheet Name')[0].AsString()
            print sheet.GetParameters('Sheet Number')[0].AsString()

            get_annotation_on_sheet(sheet)
            break
            for viewport in sheet_viewports:
                bbox = viewport.BoundingBox[sheet]
                bbox_min = bbox.Min
                bbox_max = bbox.Max

                view_name = get_viewport_parameter_value(viewport, "View Name")

                if str(view_name).lower().find('elevation') == -1 or str(view_name).lower().find('section') == -1:
                    # place plan view icon
                    print '-------------'
                    # fam = doc.Create.NewFamilyInstance(XYZ(0, 0, 0),
                    #                                    g_annotation_plan,
                    #                                    sheet,
                    #                                    # doc.GetElement(ElementId(1175564)),
                    #                                    StructuralType.NonStructural)
                    print g_annotation_plan.Id
                    fam = Viewport.Create(doc, sheet.Id, g_annotation_plan.Id, XYZ(0, 0, 0))
                    print fam.OwnerViewId

                print "B box min : {m}, b box max : {k}".format(m=bbox_min, k=bbox_max)

            if i == 0:
                break

    except Exception as e:
        print (e)

    t.Commit()


if __name__ == "__main__":
    main()
