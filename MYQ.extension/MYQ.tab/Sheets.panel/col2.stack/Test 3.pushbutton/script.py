from Autodesk.Revit.DB import *
from pprint import PrettyPrinter

__title__ = "Col 2 - BTN 3"
__author__ = "Nikola"
__doc__ = "Button"

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document


def script():
    t = Transaction(doc, "Test")
    t.Start()

    def get_active_view(uidoc):
        # Get the active view
        view = uidoc.ActiveView

        return view

    def get_bounding_box_edges(element, view):
        # Get the element's bounding box
        # bounding_box = element.get_BoundingBox(view)

        # Get the corners of the bounding box
        min_point = element.Min
        max_point = element.Max

        # Define the edges of the bounding box
        edges = [
            (min_point, XYZ(min_point.X, max_point.Y, min_point.Z)),  # Bottom front-left to bottom front-right
            (XYZ(min_point.X, max_point.Y, min_point.Z), max_point),  # Bottom front-right to bottom back-right
            (max_point, XYZ(max_point.X, min_point.Y, min_point.Z)),  # Bottom back-right to bottom back-left
            (XYZ(max_point.X, min_point.Y, min_point.Z), min_point),  # Bottom back-left to bottom front-left
            (min_point, XYZ(min_point.X, min_point.Y, max_point.Z)),  # Top front-left to top front-right
            (XYZ(min_point.X, min_point.Y, max_point.Z), max_point),  # Top front-right to top back-right
            (max_point, XYZ(max_point.X, min_point.Y, max_point.Z)),  # Top back-right to top back-left
            (XYZ(max_point.X, min_point.Y, max_point.Z), min_point),  # Top back-left to top front-left
            (XYZ(min_point.X, max_point.Y, min_point.Z), XYZ(min_point.X, max_point.Y, max_point.Z)),
            # Front-left to top front-left
            (XYZ(max_point.X, max_point.Y, min_point.Z), XYZ(max_point.X, max_point.Y, max_point.Z)),
            # Front-right to top front-right
            (XYZ(max_point.X, min_point.Y, min_point.Z), XYZ(max_point.X, min_point.Y, max_point.Z)),
            # Back-right to top back-right
            (XYZ(min_point.X, min_point.Y, min_point.Z), XYZ(min_point.X, min_point.Y, max_point.Z)),
            # Back-left to top back-left
        ]

        return edges

    def get_rotation(transform):
        # Get the X, Y, Z vectors of the transformation
        x_axis = transform.BasisX
        y_axis = transform.BasisY
        z_axis = transform.BasisZ

        # Calculate the angle between the Y vector and the global Y vector
        angle = y_axis.AngleTo(XYZ.BasisY)
        return angle

    def get_point_location(i, point):
        new_point = None
        point_offset = 2

        if i == 0:
            new_point = XYZ(point.X - point_offset, point.Y, point.Z)
        elif i == 1:
            new_point = XYZ(point.X, point.Y + point_offset, point.Z)
        elif i == 2:
            new_point = XYZ(point.X + point_offset, point.Y, point.Z)
        elif i == 3:
            new_point = XYZ(point.X, point.Y - point_offset, point.Z)

        return new_point

    try:
        rooms = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Rooms).ToElements()
        # view_family = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Views).ToElements()
        view_family = FilteredElementCollector(doc).OfClass(ViewFamilyType).ToElements()
        scope_box_filter = FilteredElementCollector(doc).OfClass(View).WhereElementIsNotElementType().ToElements()

        # for scope_box in scope_box_filter:
        #     mm = scope_box.get_Parameter(BuiltInParameter.VIEW_FAMILY_AND_TYPE_SCHEDULES)
        #     print mm.AsValueString()
        #     if mm.AsValueString() == 'Scope Box':
        #         print mm.AsValueString()

        view_type = None
        for view in view_family:
            par_name = view.GetParameters("Type Name")[0].AsString()
            if par_name.lower() == 'interior elevation':
                view_type = view
        # t.Commit()
        # return
        for room in rooms:
            # print (room.GetParameters("Name")[0].AsString())
            bbox = room.get_BoundingBox(None)
            edges = get_bounding_box_edges(bbox, get_active_view(uidoc))

            set_of_lines = list()
            for line in edges:
                pt_1 = line[0]
                pt_2 = line[1]
                ll = Line.CreateBound(pt_1, pt_2)
                direction = ll.Direction

                x = direction.X
                y = direction.Y
                z = direction.Z
                n = XYZ(z - y, x - z, y - x)

                model_line = doc.Create.NewDetailCurve(doc.ActiveView, ll)
                normal = ll.Direction.Normalize()
                plane = Plane.CreateByNormalAndOrigin(n, pt_1)
                sketch_plane = SketchPlane.Create(doc, plane)
                model_curve = doc.Create.NewModelCurve(ll, sketch_plane)
                set_of_lines.append(model_curve.Id)
                print model_line

            # doc.Create.NewGroup(set_of_lines)
            bb_center = XYZ((bbox.Max.X + bbox.Min.X) / 2, (bbox.Max.Y + bbox.Min.Y) / 2, bbox.Min.Z)

            room_box = BoundingBoxXYZ()
            room_box.Min = XYZ(bbox.Min.X - 0, bbox.Min.Y - 0, bbox.Min.Z - 0)
            room_box.Max = XYZ(bbox.Max.X + 0, bbox.Max.Y + 0, bbox.Max.Z + 0)

            # print room_box.Min
            # print room_box.Max
            el_t = list()
            for i in range(4):
                sub_transition = SubTransaction(doc)
                sub_transition.Start()
                trans = Transform.Identity
                trans.Origin = room.Location.Point

                print view_type
                try:
                    new_point = get_point_location(i, bb_center)
                    el_mark = ElevationMarker.CreateElevationMarker(doc, view_type.Id, new_point, 25)
                    el_kt = el_mark.CreateElevation(doc, ElementId(32), i)
                    el_kt.CropBox = bbox
                    # bb = doc.GetElement(ElementId(1596828))
                    # .get_BoundingBox(None))
                    # el_kt.GetParameters("Scope Box")[0].Set(bb.Id)
                    el_t.append(el_kt)

                    sub_transition.Commit()
                except Exception as e:
                    print e
                    sub_transition.RollBack()

            break

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
