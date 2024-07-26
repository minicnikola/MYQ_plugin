import time

from Autodesk.Revit.DB import *
from pprint import PrettyPrinter
from pyrevit import forms

__title__ = "Col 2 - BTN 1"
__author__ = "Me"
__doc__ = "Button"

pp = PrettyPrinter(indent=2)

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document

t = Transaction(doc, "Test")
t.Start()

try:
    print ("-"*20)
    count = 1
    with forms.ProgressBar(title="Progress", height=10, steps=10) as bar:
        bar.update_progress(count, 5)
        count = count + 1
except Exception as e:
    print (e)

t.Commit()
