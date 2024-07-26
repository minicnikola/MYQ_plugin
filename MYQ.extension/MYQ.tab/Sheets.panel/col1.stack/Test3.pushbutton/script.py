from Autodesk.Revit.DB import *
from pprint import PrettyPrinter
from Snippets._select import get_sheets_by_room, get_schedule_by_name, get_viewports, get_view_parameter_value, \
    get_a1_block

__title__ = "Place schedules on sheets"
__author__ = "Me"
__doc__ = "--------"

from Snippets.size import get_scaled_size, get_viewport_dimensions
from constants import Sizes

pp = PrettyPrinter(indent=2)

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document


def place_to_get_size(sheet):
    sub = SubTransaction(doc)
    sub.Start()
    try:
        print "Sheet number is {s}".format(s=sheet.SheetNumber)
        schedule = get_schedule_by_name("6100_LOOSE FURNITURE AND EQU_BY SHEET")
        sch_viewport = ScheduleSheetInstance.Create(doc, sheet.Id, schedule.Id, XYZ(0, 0, 0))
        sub.Commit()
        return sch_viewport

    except Exception as e:
        print e
        sub.RollBack()
        return None


def determine_schedule_placement(sheets_by_room):
    """
    check if there is a space on sheet one

    first retrieve plan view, check its position and size
    check if height of plan view and height of schedule combined is smaller than height of paper
    if that is the case, place schedule bellow the plan view
    if not, check if there is a place next to a plan view

    if schedule is placed, check if there is a space for images
    first check bellow schedule
    then check if there is space bellow elevations
    if there is no space on first sheet try placing it on second

    if on a second sheet views are one next to each other place images bellow then
    if one view is bellow another one:
    check if there is a space next to upper one, if not , try to move it
    if there is no space, try to place next to one bellow and try to move it if there is no space
    try to place it on third sheet, with same steps
    if none of this is possible raise an error_

    then check if there is a space on second sheet

    then check if there is a space on third sheet
    """
    if len(sheets_by_room) == 0:
        return None

    sheet_one = sheets_by_room[0]
    sheet_one_viewports = get_viewports(sheet_one)

    for k in sheet_one_viewports:
        view_id = k.ViewId
        view = doc.GetElement(view_id)
        family_name = get_view_parameter_value(view, "Family")
        if family_name is None:
            return None
        if family_name == 'Floor Plan':
            pl_vw, pl_vh = get_viewport_dimensions(k)
            print pl_vh
            sch_viewport = place_to_get_size(sheet_one)
            bbox = sch_viewport.BoundingBox[sheet_one]

    print sheet_one.GetParameters('Sheet Number')[0].AsString()
    return ""


def place_schedule(room_number):
    fur_sch = get_schedule_by_name("6100_LOOSE FURNITURE AND EQU")
    sanitary_sch = get_schedule_by_name("6300_SANITARY SCHEDULE BY SHEET")
    sheets_by_room = get_sheets_by_room(room_number)

    if len(sheets_by_room) == 0:
        print "Room number : {r}".format(r=room_number)
        return None

    determine_schedule_placement(sheets_by_room)
    #
    # for k in sheets_by_room:
    #     print k.GetParameters('Sheet Number')[0].AsString()

    # WARNING this should be allowed in order to differentiate between schedules
    # room_type = get_room_type(room_number)
    # print "Returned room name : {s}".format(s=room_type)
    #
    # if room_type == "Furniture":
    #     sch = fur_sch
    # else:
    #     sch = sanitary_sch

    sheet = sheets_by_room[0]
    return
    schedule_viewport = ScheduleSheetInstance.Create(doc, sheet.Id, sch.Id, XYZ(0, 0, 0))
    sch_vp = schedule_viewport.get_BoundingBox(sheet)
    sch_vp_min = sch_vp.Min
    sch_vp_max = sch_vp.Max

    sch_vp_width = sch_vp_max.X - sch_vp_min.X
    sch_vp_height = sch_vp_max.Y - sch_vp_min.Y

    print "Viewport width : {s}".format(s=sch_vp_width)
    print "Viewport height : {s}".format(s=sch_vp_height)

    # TODO Creating center point for moving schedule
    # schedule_viewport.Point = XYZ(sch_vp_width/2 + 0.06, sch_vp_height + 0.1, 0)
    schedule_viewport.Point = XYZ(0.1, sch_vp_height + 0.1, 0)
    # schedule_viewport = Viewport.Create(doc, sheet.Id, ElementId(int(str(sch.Id))), XYZ(0, 0, 0))


def main():
    t = Transaction(doc, "Test")
    t.Start()

    try:
        rooms = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Rooms).ToElements()
        for room in rooms:
            rr = room.GetParameters("Number")
            # if len(rr) == 0:
            #     continue
            room_number_ = room.GetParameters("Number")[0].AsString()
            # if room_number_ != '010':
            #     continue
            place_schedule(room_number_)
            # break

    except Exception as e:
        print (e)

    t.Commit()


if __name__ == "__main__":
    main()
