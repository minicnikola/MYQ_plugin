from Autodesk.Revit.DB import *
from pprint import PrettyPrinter
from pyrevit import revit, DB, UI
from pyrevit import UI as pyUI

__title__ = "Create dimensions"
__author__ = "Me"
__doc__ = "Button"

pp = PrettyPrinter(indent=2)

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document
ac_view = doc.ActiveView

t = Transaction(doc, "Test")
t.Start()


def get_selected_elements():
    # Get active Revit application and document
    doc = revit.doc

    # Get current selection
    uidoc = revit.uidoc
    selection = uidoc.Selection

    # Get ElementIds of selected elements
    selected_ids = selection.GetElementIds()

    # Convert ElementIds to Revit elements
    selected_elements = []
    for element_id in selected_ids:
        element = doc.GetElement(element_id)
        if element:
            selected_elements.append(element)

    return selected_elements


try:
    selected_elements = get_selected_elements()
    lr_references = list()
    fb_references = list()

    for element in selected_elements:
        print element.Location
        # ref = element.GetReferences(FamilyInstanceReferenceType.CenterLeftRight)[0]
        # print dir(ref)
        # print ref
        # print ref.GlobalPoint
        break
        # pk = element.GetGeometryObjectFromReference(m)[0]
        # print pk
        # lr_ref = element.GetReferences(FamilyInstanceReferenceType.CenterLeftRight)
        # fb_ref = element.GetReferences(FamilyInstanceReferenceType.CenterFrontBack)
        #
        # if len(lr_ref) == 1:
        #     lr_references.append(lr_ref[0])
        #
        # if len(fb_ref) == 1:
        #     fb_references.append(fb_ref[0])

    # for k in fb_references:
    #     print k.Normal

except Exception as e:
    print (e)

t.Commit()
