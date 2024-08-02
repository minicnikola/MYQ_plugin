from Autodesk.Revit.DB import *
from pprint import PrettyPrinter

__title__ = "Generate joinery views"
__author__ = "Me"
__doc__ = "Button"

from Snippets._select import get_floor_plan_views

pp = PrettyPrinter(indent=2)

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document


def get_view_outlines(view):
    # Check if the view has a crop box
    # if not view.CropBox.IsValidObject:
    #     raise Exception("View does not have a valid crop box.")

    # Get the crop box transform and bounds
    crop_box = view.CropBox
    transform = view.CropBox.Transform

    # Create a bounding box for the crop box
    bounding_box = crop_box
    min_point = bounding_box.Min
    max_point = bounding_box.Max

    # Define the corners of the crop box in the view's coordinate system
    points = [
        min_point,
        XYZ(max_point.X, min_point.Y, min_point.Z),
        XYZ(max_point.X, max_point.Y, min_point.Z),
        XYZ(min_point.X, max_point.Y, min_point.Z),
        min_point
    ]

    # Create lines for the crop box edges
    lines = []
    for i in range(len(points) - 1):
        line = Line.CreateBound(points[i], points[i + 1])
        lines.append(line)

    return lines


def set_crop_box(view, new_min_point, new_max_point):
    # Ensure the view has a crop box
    # if not view.CropBox.IsValidObject:
    #     raise Exception("View does not have a valid crop box.")

    # Start a transaction to modify the view
    # Create a new BoundingBoxXYZ with the updated points
    new_crop_box = BoundingBoxXYZ()
    new_crop_box.Min = new_min_point
    new_crop_box.Max = new_max_point

    # Update the view's crop box
    view.CropBox = new_crop_box


def get_longest_line(viewport_lines):
    longest_line = None
    for line in viewport_lines:
        if longest_line is None:
            longest_line = line
        if longest_line.Length > longest_line:
            longest_line = line
    return longest_line


def create_scope_box(view):
    view_level = view.GenLevel
    print view_level.Name
    sco = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Views).ToElements()
    for c in sco:
        p_n = c.GetParameters("View Name")
        if len(p_n) == 0:
            continue
        m = p_n[0].AsString()
        print m
        print str(m).lower().find('scope')
    return ""


def main():
    t = Transaction(doc, "Test")
    t.Start()

    try:
        joinery_plan_views = get_floor_plan_views("Joinery Plan")
        for view in joinery_plan_views:
            v_name = view.Name
            v_split = v_name.split(' - ')

            if v_name != "217 - Wardrobe 1":
                continue

            # new_min_point = XYZ(0, 0, 0)
            # new_max_point = XYZ(10, 10, 10)
            # set_crop_box(view, new_min_point, new_max_point)

            # viewport_lines = get_view_outlines(view)
            # longest_line = get_longest_line(viewport_lines)
            scope_box = create_scope_box(view)
            print scope_box
            # print longest_line.Length

    except Exception as e:
        print (e)

    t.Commit()


if __name__ == "__main__":
    main()
