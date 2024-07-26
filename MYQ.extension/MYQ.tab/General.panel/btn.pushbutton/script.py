from Autodesk.Revit.DB import *
from pprint import PrettyPrinter

__title__ = "Change Templates"
__author__ = "Me"
__doc__ = "Button"

pp = PrettyPrinter(indent=2)

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document

t = Transaction(doc, "Test")
t.Start()


try:
    print ('------')
except Exception as e:
    print (e)

t.Commit()
