from Autodesk.Revit.DB import *
from pprint import PrettyPrinter

__title__ = "Annotate plan views"
__author__ = "Me"
__doc__ = "Button"

from clr import StrongBox

from Snippets._select import get_3000_plan_views, get_walls_by_type, get_text_note_by_type, get_furniture_tag_by_type, \
    get_wall_tag_by_type, get_all_walls_in_view, get_element_parameter_value
from System.Collections.Generic import List

pp = PrettyPrinter(indent=2)

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document

text_fam = get_text_note_by_type("Text", "2.0mm Arial Narrow").GetTypeId()
lines_to_delete = list()


def check_two_line_intersection(line1, line2):
    intersections = StrongBox[IntersectionResultArray]()
    intersect = line1.GeometryCurve.Intersect(line2.GeometryCurve, intersections)

    print intersect
    if intersect.ToString() == 'Disjoint':
        return False
    return True


def get_lines_intersection_point(line1, line2):
    intersection_results = StrongBox[IntersectionResultArray]()

    # Check for intersection
    result = line1.GeometryCurve.Intersect(line2.GeometryCurve, intersection_results)

    if result == SetComparisonResult.Overlap or intersection_results.Value.Count > 0:
        # Return the first intersection point
        if intersection_results.Value.Count > 0:
            intersection_point = intersection_results.Value[0][0].XYZPoint
            return intersection_point
        else:
            # Lines are coincident, handle as needed
            return None
    else:
        # Lines do not intersect
        return None


def check_if_tag_intersect_walls(tag, view):
    walls_in_view = get_all_walls_in_view(view)
    tag_head_position = tag.TagHeadPosition
    tag_location = tag.GetLeaderEnd(tag.GetTaggedReferences()[0])
    # print "Tag head position : {head}, tag location : {loc}".format(head=tag_head_position.ToString(),
    #                                                                 loc=tag_location.ToString())

    p1 = Line.CreateBound(tag_head_position, tag_location)
    oo = doc.Create.NewDetailCurve(view, p1)
    TextNote.Create(doc, view.Id, tag_head_position, '+', text_fam)
    TextNote.Create(doc, view.Id, tag_location, '-', text_fam)
    lines_to_delete.append(oo)

    for w in walls_in_view:
        # print w
        wall_type = get_element_parameter_value(w, 'Family and Type')
        # print wall_type

        if type(w.Location) != LocationCurve:
            continue

        wall_curve = w.Location.Curve
        wall_direction = wall_curve.Direction
        wall_origin = wall_curve.Origin
        wall_length = wall_curve.Length

        wall_end_point = wall_origin + wall_direction * wall_length
        wall_line_bound = Line.CreateBound(wall_origin, wall_end_point)
        wall_line_constructed = doc.Create.NewDetailCurve(view, wall_line_bound)

        lines_to_delete.append(wall_line_constructed)
        if check_two_line_intersection(wall_line_constructed, oo):
            get_lines_intersection_point(wall_line_constructed, oo)

            return w.Id
            # TextNote.Create(doc, view.Id, )
            # tag.Location.Move(XYZ(0, 3, 0))

        # TextNote.Create(doc, view.Id, wall_origin, wall_origin.ToString(), text_fam)
        # TextNote.Create(doc, view.Id, wall_end_point, 'end point', text_fam)
        # print "Origin : {origin}, direction : {direction}, length : {length}".format(origin=wall_origin,
        #                                                                              direction=wall_direction,
        #                                                                              length=wall_length)
    return None


def tag_walls(view):
    all_interior_walls = get_walls_by_type("I_FIN_Gyp Brd 12.5mm", view_id=view.Id)
    for w in all_interior_walls:
        wall_ref = Reference(w)
        wall_mid_point = w.Location.Curve.Evaluate(0.5, True)
        tag_point = XYZ(wall_mid_point.X, wall_mid_point.Y, wall_mid_point.Z)
        wall_tag_type_id = get_wall_tag_by_type("ALEA_AD_Wall Tag", "Boxed")

        if wall_tag_type_id is None:
            print 'Error ------------'

        tag = IndependentTag.Create(doc,
                                    wall_tag_type_id.Id,
                                    view.Id,
                                    wall_ref,
                                    True,
                                    TagOrientation.Horizontal,
                                    tag_point)
        tag.HasLeader = True
        tag.LeaderEndCondition = LeaderEndCondition.Free
        tag_location = tag.Location
        # print dir(tag_location)
        # print tag_location
        # print tag.GetLeaderEnd(wall_ref)
        bbox = tag.BoundingBox[view]
        # print bbox.Max.X - bbox.Min.X
        # print bbox.Max.Y - bbox.Min.Y
        x = tag.TagHeadPosition
        y = tag.GetLeaderEnd(wall_ref)
        hor_offset = (x - y).X
        ver_offset = (x - y).Y

        rounded_hor_offset = round(hor_offset, 2)
        rounded_ver_offset = round(ver_offset, 2)

        furniture_tag = get_furniture_tag_by_type("ALEA_Furniture Tag", "Boxed")

        if rounded_hor_offset == 0 and rounded_ver_offset > 0:
            tt = 'vertical and top'
            # TextNote.Create(doc, view.Id, wall_mid_point, tt, text_fam)
            tag.Location.Move(XYZ(0, -1.2, 0))
            tag_end_point = tag_point + XYZ(0, 0, 0)
            tag.SetLeaderEnd(wall_ref, tag_end_point)
        elif rounded_hor_offset == 0 and rounded_ver_offset < 0:
            tt = 'vertical and bottom'
            tag.Location.Move(XYZ(0, 1.2, 0))
            tag_end_point = tag_point + XYZ(0, 0, 0)
            tag.SetLeaderEnd(wall_ref, tag_end_point)
#             TextNote.Create(doc, view.Id, wall_mid_point, tt, text_fam)
        elif rounded_ver_offset == 0 and rounded_hor_offset > 0:
            tt = 'horizontal and right'
            tag.Location.Move(XYZ(-1, 0, 0))
            tag_end_point = tag_point + XYZ(0, 0, 0)
            tag.SetLeaderEnd(wall_ref, tag_end_point)
#             TextNote.Create(doc, view.Id, wall_mid_point, tt, text_fam)
        elif rounded_ver_offset == 0 and rounded_hor_offset < 0:
            tt = 'horizontal and left'
            tag.Location.Move(XYZ(1, 0, 0))
            tag_end_point = tag_point + XYZ(0, 0, 0)
            tag.SetLeaderEnd(wall_ref, tag_end_point)
#             TextNote.Create(doc, view.Id, wall_mid_point, tt, text_fam)

        if tag.HasLeaderElbow(wall_ref):
            print tag.GetLeaderElbow(wall_ref)

        print check_if_tag_intersect_walls(tag, view)
        # check_if_tag_intersect_walls(tag, view)
        # tag_end_point = tag_point + XYZ(-1, 0, 0)
        # tag.SetLeaderEnd(wall_ref, tag_end_point)
        #
        # tag.Location.Move(XYZ(1, 0, 0))

        # break


def tag_furniture(view):
    all_furniture_in_view = FilteredElementCollector(doc, view.Id).OfCategory(
        BuiltInCategory.OST_Furniture).ToElements()
    furniture_tag = get_furniture_tag_by_type("ALEA_Furniture Tag", "Boxed")
    kk = get_text_note_by_type("Text", "2.0mm Arial Narrow").GetTypeId()
    for fur in all_furniture_in_view:
        bbox = fur.BoundingBox[view]
        location_point = fur.Location.Point
        horizontal_mid = bbox.Max.Y - bbox.Min.Y
        vertical_mid = bbox.Max.X - bbox.Min.X
        pp = XYZ(location_point.X + vertical_mid/2, location_point.Y - horizontal_mid/2, location_point.Z)
        print location_point
        print pp

        IndependentTag.Create(doc,
                              furniture_tag.Id,
                              view.Id,
                              Reference(fur),
                              False,
                              TagOrientation.Horizontal,
                              # fur.Location.Point,
                              pp)

        TextNote.Create(doc, view.Id, location_point, location_point.ToString(), kk)

    TextNote.Create(doc, view.Id, XYZ(0, 0, 0), "0, 0, 0", kk)


def tag_floors():
    pass


def tag_doors():
    pass


def tag_light():
    pass


def get_wall_directions(wall):
    wall_location = wall.Location
    wall_curve = wall_location.Curve
    return wall_curve.Direction


def main():
    t = Transaction(doc, "Test")
    t.Start()

    try:
        floor_plan_views = get_3000_plan_views()

        for plan_view in floor_plan_views:
            plan_view_number = plan_view.Name.split(' - ')[0]

            if plan_view_number != '201':
                continue

            # print check_two_line_intersection(line1, line2)
            # tag_walls(plan_view)
            # tag_furniture(plan_view)

            print plan_view.Name
    except Exception as e:
        print (e)

    t.Commit()

    t = Transaction(doc, 'Lines delete')
    t.Start()

    try:
        for line in lines_to_delete:
            # doc.Delete(line.Id)
            pass
    except Exception as e:
        print e

    t.Commit()


if __name__ == "__main__":
    main()
