from Autodesk.Revit.DB import *
from pprint import PrettyPrinter
from pyrevit import forms

__title__ = "Rename sheets"
__author__ = "Me"
__doc__ = "--------"

pp = PrettyPrinter(indent=2)

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document

t = Transaction(doc, "Test")
t.Start()



try:
    sheets = list()
    options = FilteredElementCollector(doc).OfClass(ViewSheet).ToElements()
    res = forms.SelectFromList.show(options, multiselect=True, name_attr='SheetNumber', button_name='Select Sheet')

    for i in res:
        sheet_name = i.GetParameters("Sheet Name")[0].AsString()
        sheet_number = i.GetParameters("Sheet Number")[0].AsString()
        print ("Sheet name : {s} / Sheet number : {m}".format(s=sheet_name, m=sheet_number))

        if str(sheet_number).startswith('40'):
            i.Name = 'BASEMENT'
        elif str(sheet_number).startswith('41'):
            i.Name = 'GROUND FLOOR'
        elif str(sheet_number).startswith('42'):
            i.Name = 'FIRST FLOOR'
        elif str(sheet_number).startswith('43'):
            i.Name = 'ROOF'

except Exception as e:
    print (e)

t.Commit()
