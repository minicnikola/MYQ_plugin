from Autodesk.Revit.DB import *
from pprint import PrettyPrinter

__title__ = "Get all tags of type"
__author__ = "Me"
__doc__ = "Button"

pp = PrettyPrinter(indent=2)

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document
ac_view = doc.ActiveView


def main():
    t = Transaction(doc, "Test")
    t.Start()

    try:
        tags = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_WallTags).WhereElementIsElementType().ToElements()
        all_views = FilteredElementCollector(doc).OfClass(View).ToElements()

        for tag in tags:
            tag_name = tag.GetParameters("Family Name")[0].AsString()
            print tag_name

            if tag_name == "ALEA_AD_Wall Tag":
                print tag

                for view in all_views:
                    if doc.GetElement(tag.Id).IsVisibleInView(view.Id):
                        print view.Id

            break

    except Exception as e:
        print (e)

    t.Commit()


if __name__ == "__main__":
    main()
