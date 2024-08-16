from Autodesk.Revit.DB import *
from pprint import PrettyPrinter

__title__ = "*"
__author__ = "Nikola"
__doc__ = "Button"

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document


def script():
    t = Transaction(doc, "Test")
    t.Start()

    try:
        pass
    except Exception as e:
        print (e)

    t.Commit()


if __name__ == "__main__":
    script()


# for kkki in el_t:
#     stkt = SubTransaction(doc)
#     stkt.Start()
#     parameter = kkki.LookupParameter("Scope Box")
#     if parameter:
#         parameter.Set(ElementId.InvalidElementId)
#     stkt.Commit()
#
# new_point = get_point_location(i, bb_center)
# el_mark = ElevationMarker.CreateElevationMarker(doc, k.Id, new_point, 25)
# el_kt = el_mark.CreateElevation(doc, ElementId(32), i)
# # el.CropBox = scope_box.get_BoundingBox(doc.ActiveView)
# bb = doc.GetElement(ElementId(1596828))
# # .get_BoundingBox(None))
# el_kt.GetParameters("Scope Box")[0].Set(bb.Id)
# el_t.append(el_kt)

# bbox_transform = Transform.CreateTranslation(bbox.Min)  # Translate to origin
# rotation_angle = get_rotation(bbox_transform)

# print("Rotation Angle (radians):", rotation_angle)
# print("Rotation Angle (degrees):", rotation_angle * 180 / 3.141592653589793)
#
# bbox_transform.BasisX = bbox.Max - bbox.Min  # Set X-axis direction
# bbox_transform.BasisY = XYZ.BasisY  # Set Y-axis direction
# bbox_transform.BasisZ = XYZ.BasisZ  # Set Z-axis direction
