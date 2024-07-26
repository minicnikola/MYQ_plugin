from Autodesk.Revit.DB import *
from pprint import PrettyPrinter

__title__ = "Col 2 - BTN 3"
__author__ = "Me"
__doc__ = "Button"

pp = PrettyPrinter(indent=2)

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document

t = Transaction(doc, "Test")
t.Start()

try:
    views = FilteredElementCollector(doc).OfClass(ViewPlan).WhereElementIsNotElementType().ToElements()

    for view in views:
        pp = view.GetParameters("View Name")
        if len(pp) == 1:
            view_name = pp[0].AsString()
            if view_name == "GENERAL LAYOUT":
                view_name = view_name + "-1"
                new_view = view.Duplicate(ViewDuplicateOption.WithDetailing)
                el = doc.GetElement(new_view)
                el.Name = view_name
                doc.Regenerate()
except Exception as e:
    print (e)

t.Commit()
