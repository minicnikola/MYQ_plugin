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


def list_imported_dwgs(doc):
    imported_dwgs = []
    collector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_ImportObjectStyles)

    for elem in collector:
        print elem
        if isinstance(elem, ImportInstance):
            if elem.IsLinked:
                continue  # Skip linked DWGs, process only imported ones
            if elem.GetOriginalFileExtension().lower() == "dwg":
                imported_dwgs.append(elem)

    return imported_dwgs

try:
    # imported = FilteredElementCollector(doc).OfClass(ImportInstance).ToElements()
    # for k in doc.Settings.Categories:
    #     # print dir(k)
    #     # print '-----'
    #     # print k.CategoryType
    #     # print k.Name
    #     name = k.Name
    #     if str(name).endswith(".dwg"):
    #         el = doc.GetElement(k.Id)
    #
    #         if el.Location is not None:
    #             print el
    #     # break
    imported_dwgs = list_imported_dwgs(doc)

    if imported_dwgs:
        print("Imported DWG Files:")
        for dwg in imported_dwgs:
            print("%s".format(s=dwg.Name))
    else:
        print("No imported DWG files found.")

except Exception as e:
    print (e)

t.Commit()
