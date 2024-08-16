from Autodesk.Revit.DB import *
from pprint import PrettyPrinter

__title__ = "Col 2 - BTN 1"
__author__ = "Me"
__doc__ = "Button"

pp = PrettyPrinter(indent=2)

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document
ac_view = doc.ActiveView

t = Transaction(doc, "Test")
t.Start()


def get_crop_region_lines(view):
    if isinstance(view, ViewSection):
        # Get the crop box of the view
        crop_box = view.CropBox

        # Extract lines defining the crop region
        lines = list()
        lines.append(Line.CreateBound(crop_box.Min, XYZ(crop_box.Max.X, crop_box.Min.Y, 0)))
        lines.append(Line.CreateBound(XYZ(crop_box.Max.X, crop_box.Min.Y, 0), crop_box.Max))
        lines.append(Line.CreateBound(crop_box.Max, XYZ(crop_box.Min.X, crop_box.Max.Y, 0)))
        lines.append(Line.CreateBound(XYZ(crop_box.Min.X, crop_box.Max.Y, 0), crop_box.Min))

        return lines
    else:
        print("View is not a ViewSection.")
        return None

try:
    rooms = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Rooms).ToElements()
    view_types = FilteredElementCollector(doc).OfClass(ViewFamilyType).ToElements()

    view_type = None
    for ty in view_types:
        if ty.FamilyName == 'Elevation':
            par_name = ty.GetParameters("Type Name")[0].AsString()

            if par_name == 'Interior Elevation':
                print par_name
                view_type = ty
        # print ty.GetParameters("Family")

    for room in rooms:
        print room.GetParameters("Name")[0].AsString()
        bbox = room.get_BoundingBox(None)
        # mark = ElevationMarker.CreateElevationMarker(doc, view_type.Id, room.Location.Point, 20)
        # el1 = mark.CreateElevation(doc, ac_view.Id, 0)
        # el2 = mark.CreateElevation(doc, ac_view.Id, 1)
        #
        # cp = el1.CropBox
        # min_cp = cp.Min
        # max_cp = cp.Max

        # print min_cp.X
        # print min_cp.Y
        # print min_cp.Z
        #
        # print max_cp.X
        # print max_cp.Y
        # print max_cp.Z - min_cp.Z

        # for line in get_crop_region_lines(el2):
        #     x1 = line.GetEndPoint(0).X
        #     y1 = line.GetEndPoint(0).Y
        #     z1 = line.GetEndPoint(0).Z
        #     x2 = line.GetEndPoint(1).X
        #     y2 = line.GetEndPoint(1).Y
        #     z2 = line.GetEndPoint(1).Z
        #
        #     x1_conv = UnitUtils.ConvertFromInternalUnits(x1, UnitTypeId.Centimeters)
        #     y1_conv = UnitUtils.ConvertFromInternalUnits(y1, UnitTypeId.Centimeters)
        #     z1_conv = UnitUtils.ConvertFromInternalUnits(z1, UnitTypeId.Centimeters)
        #     x2_conv = UnitUtils.ConvertFromInternalUnits(x2, UnitTypeId.Centimeters)
        #     y2_conv = UnitUtils.ConvertFromInternalUnits(y2, UnitTypeId.Centimeters)
        #     z2_conv = UnitUtils.ConvertFromInternalUnits(z2, UnitTypeId.Centimeters)
        #
        #     print "Line Min: {0} Y: {1} Z: {2}".format(x1_conv, y1_conv, z1_conv)
        #     print "Line Max: {0} Y: {1} Z: {2}".format(x2_conv, y2_conv, z2_conv)
        #     break

except Exception as e:
    print (e)

t.Commit()
