from Autodesk.Revit.DB import *
from pprint import PrettyPrinter

__title__ = "Col 2 - BTN 2"
__author__ = "Me"
__doc__ = "Button"

pp = PrettyPrinter(indent=2)

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document


t = Transaction(doc, "Test")
t.Start()

try:
    print ("-" * 20)
except Exception as e:
    print (e)

t.Commit()
