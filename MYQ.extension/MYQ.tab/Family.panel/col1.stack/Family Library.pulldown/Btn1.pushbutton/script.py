from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Structure import StructuralType
from pprint import PrettyPrinter
import pyrevit.forms

__title__ = "Place families"
__author__ = "Me"
__doc__ = "Button"

from Snippets._select import get_floor_plan_views, get_a2_block, get_families_by_category, get_element_parameter_value

pp = PrettyPrinter(indent=2)

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document
ac_view = doc.ActiveView


def main():
    # response = pyrevit.forms.alert(title="Warning", msg='Do you want to proceed')
    # if not response:
    #     return

    t = Transaction(doc, "Test")
    t.Start()

    try:
        results = get_families_by_category(BuiltInCategory.OST_Casework)
        k = 1
        off = 1

        for i, item in enumerate(results):
            if i % 30 == 0:
                k += 1
                off = 1

            off += 1
            if isinstance(item, FamilyInstance):
                continue

            if not item.IsActive:
                item.Activate()

            fam_instance = doc.Create.NewFamilyInstance(XYZ(-150 + off*8, -20, 0), item, ac_view, StructuralType.NonStructural)
            # print get_element_parameter_value(item, 'Type Name')
            print '-' * 50

    except Exception as e:
        print (e)

    t.Commit()


if __name__ == "__main__":
    main()
